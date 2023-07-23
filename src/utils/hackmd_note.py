import requests

from src.config.config import settings
from src.utils.url_processor import join_url

HEADER = {"Authorization": "Bearer " + settings.TOKEN}
HACKMD_API_DOMAIN = "https://api.hackmd.io/v1/"


class HackmdNote:
    # hackmd_api_route https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fteam-notes-api
    # - user = ""
    # - teams = "teams/:teamPath"

    def __init__(self, hackmd_api_route: str) -> None:
        self.__hackmd_api_url = join_url(
            base_url=HACKMD_API_DOMAIN, relative_url=hackmd_api_route
        )

    def create_hackmd_note(self, content: str) -> dict:
        create_api_url = join_url(base_url=self.__hackmd_api_url, relative_url="notes")
        data = {
            "title": None,
            "content": content,
            "readPermission": "guest",
            "writePermission": "signed_in",
            "commentPermission": "signed_in",
        }
        response = requests.post(url=create_api_url, headers=HEADER, json=data)

        # print(response)
        # print(response.json())

        return response.json()

    def update_hackmd_note(self, note_id: str, content: str) -> str:
        update_api_url = join_url(
            base_url=join_url(base_url=self.__hackmd_api_url, relative_url=note_id),
            relative_url="notes",
        )
        data = {
            "title": None,
            "content": content,
            "readPermission": "guest",
            "writePermission": "signed_in",
        }
        response = requests.patch(url=update_api_url, headers=HEADER, json=data)

        # print(response)
        # print(response.json())

        return response
