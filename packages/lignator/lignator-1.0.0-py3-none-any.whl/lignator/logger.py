import logging
import sys

logger = logging.getLogger("lignator")

logging.basicConfig(
    handlers=[
        logging.FileHandler(r'./log/main.log'),
    ],
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
