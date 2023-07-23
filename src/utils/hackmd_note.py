import requests

from src.config.config import settings


HEADER = {"Authorization": "Bearer " + settings.TOKEN}
API_URL_CREATE_USER_NOTE = settings.HACKMD_API_URL + "notes"
API_URL_CREATE_TEAM_NOTE = (
    settings.HACKMD_API_URL + "teams/" + settings.TEAM_PATH + "/notes"
)
API_URL_UPDATE_TEAM_NOTE = (
    settings.HACKMD_API_URL + "teams/" + settings.TEAM_PATH + "/notes/"
)


def create_hackmd_note(content: str, header=HEADER) -> dict:
    create_url = API_URL_CREATE_USER_NOTE
    data = {
        "title": None,
        "content": content,
        "readPermission": "guest",
        "writePermission": "signed_in",
        "commentPermission": "signed_in",
    }
    response = requests.post(url=create_url, headers=header, json=data)

    print(response)
    # print(response.json())

    return response.json()


def update_hackmd_note(note_id: str, content: str, header=HEADER) -> str:
    update_url = API_URL_UPDATE_TEAM_NOTE + note_id
    data = {
        "title": None,
        "content": content,
        "readPermission": "guest",
        "writePermission": "signed_in",
    }
    response = requests.patch(url=update_url, headers=header, json=data)

    print(response)
    # print(response.json())

    return response
