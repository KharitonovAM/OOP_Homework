import logging
from pathlib import Path

# оперделем пути к файлам
BASE_DIR = Path(__file__).parent.parent
json_file = Path(BASE_DIR, "data", "products.json")
log_file = Path(BASE_DIR, "logs", "logfile.txt")

