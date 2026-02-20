import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

def setup_logging():
    # create logs folder if not exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging initialized.")