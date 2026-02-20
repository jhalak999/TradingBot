import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")


class BinanceFuturesClient:
    def __init__(self):
        try:
            if not API_KEY or not API_SECRET:
                raise ValueError("API keys not found in .env file")

            self.client = Client(API_KEY, API_SECRET)

            # IMPORTANT: connect to futures testnet
            self.client.FUTURES_URL = BASE_URL

            logging.info("Binance Futures client initialized (Testnet).")

        except Exception as e:
            logging.error(f"Error initializing Binance client: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place market or limit order on Binance Futures Testnet
        """
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price required for LIMIT order")

                params.update({
                    "price": price,
                    "timeInForce": "GTC"
                })

            logging.info(f"Sending order request: {params}")

            response = self.client.futures_create_order(**params)

            logging.info(f"Order response: {response}")
            return response

        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            raise

        except BinanceRequestException as e:
            logging.error(f"Network error: {e}")
            raise

        except Exception as e:
            logging.error(f"Unexpected error placing order: {e}")
            raise