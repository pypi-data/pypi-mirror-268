def filter_orders_by_strategy(
    orders: list[dict], strategy_name: str, underlying: str
) -> list[dict]:
    filtered_orders = [
        order
        for order in orders
        if strategy_name.lower() in order.get("ordertag", "").lower()
        and order.get("tradingsymbol").startswith(underlying)
    ]
    return filtered_orders
