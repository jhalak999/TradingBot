import argparse
import logging

from bot.logging_config import setup_logging
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.orders import OrderService


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--qty", required=True, type=float, help="Quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.qty)
        price = validate_price(args.price, order_type)

        service = OrderService()
        service.execute_order(symbol, side, order_type, quantity, price)

    except Exception as e:
        print(f"\nERROR: {e}")
        logging.error(f"CLI error: {e}")


if __name__ == "__main__":
    main()