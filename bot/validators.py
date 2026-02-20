def validate_symbol(symbol: str):
    if not symbol or len(symbol) < 5:
        raise ValueError("Invalid symbol. Example: BTCUSDT")
    return symbol.upper()


def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")
        return float(price)
    return None