import logging
from datetime import datetime

def get_logger():
    log_file = f'logs/test_log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()
