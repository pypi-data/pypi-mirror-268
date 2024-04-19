import functools
import traceback
from inspect import signature
from datetime import datetime
from time import sleep
import asyncio
from volstreet import config
from volstreet.utils import (
    custom_round,
    notifier,
    current_time,
    filter_orderbook_by_time,
    log_error,
)
from volstreet.angel_interface.interface import (
    fetch_book,
    fetch_quotes,
    lookup_and_return,
)
from volstreet.trade_interface import cancel_pending_orders, execute_orders
from volstreet.strategies.monitoring import get_current_state_of_strategy


def prepare_exit_params(
    positions: list[dict],
    max_lot_multiplier: int = 30,
    ltp_missing: bool = True,
) -> list[dict]:
    positions = [position for position in positions if position["netqty"]]
    order_params_list = []
    if ltp_missing:
        prices = fetch_quotes(
            [position["symboltoken"] for position in positions],
            structure="dict",
            from_source=True,
        )
        positions = [
            {**position, "ltp": prices[position["symboltoken"]]["ltp"]}
            for position in positions
        ]
    for position in positions:
        net_qty = int(position["netqty"])
        lot_size = int(position["lotsize"])
        max_order_qty = max_lot_multiplier * lot_size

        if net_qty == 0:
            continue
        action = "SELL" if net_qty > 0 else "BUY"
        total_qty = abs(net_qty)

        execution_price = (
            float(position["ltp"]) * (1 - config.LIMIT_PRICE_BUFFER)
            if action == "SELL"
            else float(position["ltp"]) * (1 + config.LIMIT_PRICE_BUFFER)
        )
        execution_price = custom_round(execution_price)

        while total_qty > 0:
            order_qty = min(total_qty, max_order_qty)
            params = {
                "variety": "NORMAL",
                "ordertype": "LIMIT",
                "price": max(execution_price, 0.05),
                "tradingsymbol": position["tradingsymbol"],
                "symboltoken": position["symboltoken"],
                "transactiontype": action,
                "exchange": config.token_exchange_dict[position["symboltoken"]],
                "producttype": "CARRYFORWARD",
                "duration": "DAY",
                "quantity": int(order_qty),
                "ordertag": "Error induced exit",
            }
            order_params_list.append(params)
            total_qty -= order_qty

    return order_params_list


@log_error(notify=True, raise_error=True)
def exit_strategy(strategy: callable, execution_time: datetime, *args, **kwargs):
    sig = signature(strategy)
    bound = sig.bind_partial(*args, **kwargs)
    bound.apply_defaults()
    order_tag = bound.arguments.get("strategy_tag")
    index = bound.arguments.get("underlying").name
    order_book = fetch_book("orderbook", from_api=True)
    order_book = filter_orderbook_by_time(order_book, start_time=execution_time)
    pending_orders = lookup_and_return(
        order_book, ["ordertag", "status"], [order_tag, "open"], "orderid"
    )
    if pending_orders:
        cancel_pending_orders(pending_orders, variety="NORMAL")
    active_positions = get_current_state_of_strategy(
        order_book, index, order_tag, with_pnl=False
    )

    if active_positions.empty:
        notifier(
            f"No positions at all for strategy {strategy.__name__}",
            webhook_url=config.ERROR_NOTIFICATION_SETTINGS["url"],
        )
        return

    active_positions = active_positions.to_dict(orient="records")
    exit_params = prepare_exit_params(active_positions, ltp_missing=True)
    if not exit_params:
        notifier(
            f"No ACTIVE positions for strategy {strategy.__name__}",
            webhook_url=config.ERROR_NOTIFICATION_SETTINGS["url"],
        )
        return
    asyncio.run(execute_orders(exit_params))
    user_prefix = config.ERROR_NOTIFICATION_SETTINGS.get("user")
    user_prefix = f"{user_prefix} - " if user_prefix else ""
    notifier(
        f"{user_prefix}Exited positions for strategy {strategy.__name__}",
        webhook_url=config.ERROR_NOTIFICATION_SETTINGS["url"],
        send_whatsapp=True,
    )


def exit_on_error(strategy):
    @functools.wraps(strategy)
    def wrapper(*args, **kwargs):
        execution_time = current_time()
        try:
            return strategy(*args, **kwargs)
        except Exception as e:
            user_prefix = config.ERROR_NOTIFICATION_SETTINGS.get("user")
            user_prefix = f"{user_prefix} - " if user_prefix else ""
            sleep(4)  # Sleep for 4 seconds to allow the orders to be filled
            notifier(
                f"{user_prefix}"
                f"Error in strategy {strategy.__name__}: {e}\nTraceback:{traceback.format_exc()}\n\n"
                f"Exiting existing positions...",
                webhook_url=config.ERROR_NOTIFICATION_SETTINGS["url"],
                level="ERROR",
                send_whatsapp=True,
            )
            exit_strategy(strategy, execution_time, *args, **kwargs)

    return wrapper
