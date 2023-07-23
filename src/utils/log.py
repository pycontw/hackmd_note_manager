import json
from datetime import datetime

from src.utils.url_processor import join_url

CURRENT_TIME = datetime.now()


def create_log(log_storage_path: str, log: list, log_file_prefix: str = "") -> None:
    log_file_name = log_file_prefix + CURRENT_TIME.strftime("%Y%m%d-%H%M%S") + ".json"
    log_file_path = join_url(base_url=log_storage_path, relative_url=log_file_name)

    with open(
        log_file_path,
        "w",
        encoding="utf-8",
    ) as json_file:
        json.dump(log, json_file, indent=4, separators=(",", ": "))
