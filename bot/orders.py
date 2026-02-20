import logging
from bot.client import BinanceFuturesClient

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def execute_order(self, symbol, side, order_type, quantity, price=None):
        try:
            print("\nORDER REQUEST SUMMARY")
            print(f"Symbol      : {symbol}")
            print(f"Side        : {side}")
            print(f"Order Type  : {order_type}")
            print(f"Quantity    : {quantity}")
            if price:
                print(f"Price       : {price}")

            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            print("HEY! ORDER SUCCESSFUL")
            print(f"Order ID       : {response.get('orderId')}")
            print(f"Status         : {response.get('status')}")
            print(f"Executed Qty   : {response.get('executedQty')}")
            print(f"Avg Price      : {response.get('avgPrice')}")

            logging.info(f"order has been executed successfully: {response}")

        except Exception as e:
            print(f"UH OH! ORDER FAILED: {str(e)}")
            logging.error(f"Order execution failed: {e}")