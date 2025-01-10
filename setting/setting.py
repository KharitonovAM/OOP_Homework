import logging
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
json_file = Path(BASE_DIR, "data", "products.json")
log_file = Path(BASE_DIR, "logs", "logfile.txt")

my_log_config = logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s- %(name)s - %(message)s",
    filename=log_file,
    filemode="w",
    encoding="UTF-8",
)
