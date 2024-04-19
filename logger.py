import logging 
import os 
from datetime import datetime

LOG_FILE=f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.get_cwd(), 'logs')

os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    format="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("This is a test")