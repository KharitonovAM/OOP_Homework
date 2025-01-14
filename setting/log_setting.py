import logging
from setting.setting import log_file

# задаем параметры для логирования
my_log_config = logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s- %(name)s - %(message)s",
    filename=log_file,
    filemode="w",
    encoding="UTF-8",
)
