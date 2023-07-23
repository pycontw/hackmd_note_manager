import json
from datetime import datetime

CURRENT_TIME = datetime.now()


def create_log(log_storage_path: str, log: list, log_file_prefix: str = "") -> None:
    with open(
        log_storage_path
        + log_file_prefix
        + CURRENT_TIME.strftime("%Y%m%d-%H%M%S")
        + ".json",
        "w",
        encoding="utf-8",
    ) as json_file:
        json.dump(log, json_file, indent=4, separators=(",", ": "))
