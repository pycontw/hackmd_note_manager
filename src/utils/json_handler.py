import json


def read_json(file_name: str) -> json:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
