import pandas as pd
import numpy as np
from volstreet.utils.core import parse_symbol
from volstreet.angel_interface.interface import fetch_quotes
from volstreet.strategies.tools import filter_orders_by_strategy


def get_current_state_of_strategy(
    orderbook: list,
    index: str,
    order_tag: str,
    with_pnl: bool = True,
) -> pd.DataFrame:
    """
    Returns the present state of a strategy. This is qty, tokens, and symbols for a given order tag.
    Active quantity is increased for 'BUY' transactions and decreased for 'SELL' transactions.

    :param orderbook: List of orderbook entries.
    :param index: The index to search for.
    :param order_tag: The order tag to search for.
    :param with_pnl: Whether to include PnL in the output.
    :return: A list dataframe with the following columns:
        - tradingsymbol: The symbol of the contract.
        - symboltoken: The token of the contract.
        - lotsize: The lot size of the contract.
        - netqty: The net quantity of the contract.
        - active_lots: The number of active lots.
        - underlying: The underlying of the contract.
        - expiry: The expiry of the contract.
        - strike: The strike of the contract.
        - option_type: The option type of the contract.
    """

    # Filtering orders and making a dataframe
    filtered_orders = filter_orders_by_strategy(orderbook, order_tag, index)
    if not filtered_orders:
        return pd.DataFrame()
    df = pd.DataFrame(filtered_orders)

    # Converting data types
    df["filledshares"] = df["filledshares"].astype(int)
    df["lotsize"] = df["lotsize"].astype(int)

    # Converting filledshares to a signed number
    df["filledshares"] = df["filledshares"] * np.where(
        df.transactiontype == "BUY", 1, -1
    )

    # Filtering out incomplete orders
    df = df[df["status"] == "complete"]

    if df.empty:
        return pd.DataFrame()

    grouped = df.groupby("tradingsymbol")
    state = (
        grouped.agg({"filledshares": "sum", "symboltoken": "first", "lotsize": "first"})
        .reset_index()
        .rename(columns={"filledshares": "netqty"})
    )

    state["active_lots"] = state["netqty"] // state["lotsize"]
    state[["underlying", "expiry", "strike", "option_type"]] = (
        state["tradingsymbol"].apply(parse_symbol).to_list()
    )

    if with_pnl:
        state["net_value"] = grouped.apply(
            lambda x: np.dot(x["filledshares"], x["averageprice"]), include_groups=False
        ).values
        ltp_data = fetch_quotes([tok for tok in state.symboltoken], structure="dict")
        ltp_data = {k: v["ltp"] for k, v in ltp_data.items()}
        state["ltp"] = state["symboltoken"].apply(ltp_data.get)
        state["outstanding_value"] = state["netqty"] * state["ltp"]
        state["pnl"] = state["outstanding_value"] - state["net_value"]
    return state
