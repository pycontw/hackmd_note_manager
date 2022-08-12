import json
from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TEAM_PATH = os.getenv("TEAM_PATH")
TOKEN = os.getenv("TOKEN")
HACKMD_API_URL = os.getenv("HACKMD_API_URL")

HEADER = {"Authorization": "Bearer " + TOKEN}
TEMPLATE_PATH = "note_template/pycon_apac_2022/"
NOTE_DATA = "data.json"
CURRENT_TIME = datetime.now()

API_URL_CREATE_USER_NOTE = HACKMD_API_URL + "notes"
API_URL_CREATE_TEAM_NOTE = HACKMD_API_URL + "teams/" + TEAM_PATH + "/notes"


def get_note_info(file_name: str) -> json:
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_note_template(file_name: str) -> str:
    file_path = TEMPLATE_PATH + file_name
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def create_log(log: list) -> None:
    with open(
        "log/" + CURRENT_TIME.strftime("%Y%m%d-%H%M%S") + ".json", "w", encoding="utf-8"
    ) as json_file:
        json.dump(log, json_file, indent=4, separators=(",", ": "))


def create_hackmd_note(api_url: str, content: str) -> json:

    data = {
        "title": None,
        "content": content,
        "readPermission": "owner",
        "writePermission": "owner",
        "commentPermission": "everyone",
    }
    response = requests.post(api_url, headers=HEADER, json=data)

    print(response)
    print(response.json())

    return response.json()


if __name__ == "__main__":
    note_info = get_note_info(NOTE_DATA)
    log = []

    for key, value in note_info.items():
        content = get_note_template("conference.md").format(
            title=key,
            slido_1=value["slido_1"],
            slido_2=value["slido_2"],
            ppt=value["ppt"],
            vedio=value["vedio"],
        )

        make_team_note = create_hackmd_note(API_URL_CREATE_TEAM_NOTE, content)
        log.append(make_team_note)

    create_log(log)
