from src.utils.log import create_log
from src.utils.json_handler import read_json
from src.utils.note_template import get_note_template
from src.utils.hackmd_note import HackmdNote


class ProgramCollabwriting:
    def __init__(
        self,
        hackmd_note: HackmdNote,
        template_storage_path: str,
        notes_title: list,
        notes_content: list,
        log_storage_path: str = "log/",
    ) -> None:
        self.__template_storage_path: str = template_storage_path
        self.__log_storage_path: str = log_storage_path
        self.__notes_title: list = notes_title
        self.__notes_content: list = notes_content
        self.__hackmd_note: HackmdNote = hackmd_note

    def get_notes_content(self) -> list:
        return self.__notes_content

    def get_notes_title(self) -> list:
        return self.__notes_title

    def create_program_collabwriting(self) -> None:
        log = []

        collabwriting_template_path = self.__template_storage_path + "collabwriting.md"

        for note_content in self.__notes_content:
            collabwriting_content = get_note_template(
                file_path=collabwriting_template_path
            ).format(
                title=note_content["title"],
                name=note_content["name"],
                slido_1=note_content["Slido"],
                slide_link=note_content["slide"],
            )

            create_program_collabwriting_result = self.__hackmd_note.create_hackmd_note(
                content=collabwriting_content,
            )
            hackmd_link = create_program_collabwriting_result["publishLink"]
            note_content["HackMD"] = hackmd_link
            log.append(create_program_collabwriting_result)

            # print(collabwriting_content)

        # print(collabwriting_toc_content)
        create_log(
            log_storage_path=self.__log_storage_path,
            log=log,
            log_file_prefix="program_collabwriting_",
        )

    def create_program_collabwriting_toc(self) -> None:
        log = []

        collabwriting_toc_template_path = (
            self.__template_storage_path + "collabwriting_toc.md"
        )

        collabwriting_toc_content = get_note_template(
            file_path=collabwriting_toc_template_path
        )

        last_note_content = self.__get_last_note_content()

        for note_content in self.__notes_content:
            collabwriting_toc_content += (
                self.__get_program_collabwriting_toc_each_session(
                    note_content=note_content,
                    last_note_content=last_note_content,
                )
            )
            # print(collabwriting_content)
            last_note_content = note_content

        make_team_collabwriting_toc = self.__hackmd_note.create_hackmd_note(
            content=collabwriting_toc_content,
        )
        log.append(make_team_collabwriting_toc)

        # print(collabwriting_toc_content)
        create_log(
            log_storage_path=self.__log_storage_path,
            log=log,
            log_file_prefix="program_collabwriting_toc",
        )

    def __get_last_note_content(self) -> dict:
        last_note_content = {}

        for title in self.__notes_title:
            last_note_content[title] = ""

        return last_note_content

    def __get_program_collabwriting_toc_each_session(
        self, note_content: dict, last_note_content: dict
    ) -> str:
        collabwriting_toc_each_session_template_path = (
            self.__template_storage_path + "collabwriting_toc_each_session.md"
        )

        note_date = ""
        note_time = ""
        note_type = ""
        note_emoji = ""
        note_room = "R" + note_content["Room"]
        note_title = note_content["title"] + " - " + note_content["name"]
        note_hackmd = note_content["HackMD"]

        if note_content["date"] != last_note_content["date"]:
            note_date = "\n# " + note_content["date"] + ""

        if (
            note_content["date"] != last_note_content["date"]
            or note_content["type"] != last_note_content["type"]
            or note_content["begin_time"] != last_note_content["begin_time"]
            or note_content["end_time"] != last_note_content["end_time"]
        ):
            if note_content["type"] != "Talk":
                note_type = " (" + note_content["type"] + ")\n"
            else:
                note_type = "\n"
            note_time = (
                "\n## " + note_content["begin_time"] + " ~ " + note_content["end_time"]
            )

            if note_content["type"] == "Keynote":
                note_emoji = "🔸"

        if note_content["Room"] == "Stage":
            note_room = "R0、R1、R2、R3"

        return get_note_template(
            file_path=collabwriting_toc_each_session_template_path
        ).format(
            date=note_date,
            time=note_time,
            type=note_type,
            room=note_room,
            emoji=note_emoji,
            title=note_title,
            hackmd=note_hackmd,
        )

    def update_program_collabwriting(self, notes_log_file_nane: str) -> None:
        notes_log = read_json(self.__log_storage_path + notes_log_file_nane)

        note_quantity = len(self.__notes_content)

        log = []

        collabwriting_template_path = self.__template_storage_path + "collabwriting.md"

        for note_index in range(note_quantity):
            collabwriting_content = get_note_template(
                file_path=collabwriting_template_path
            ).format(
                title=self.__notes_content[note_index]["title"],
                name=self.__notes_content[note_index]["name"],
                slido_1=self.__notes_content[note_index]["Slido"],
                slide_link=self.__notes_content[note_index]["slide"],
            )
            note_id = notes_log[note_index]["shortId"]
            self.__notes_content[note_index]["HackMD"] = notes_log[note_index][
                "publishLink"
            ]
            update_team_collabwriting = self.__hackmd_note.update_hackmd_note(
                note_id=note_id,
                content=collabwriting_content,
            )
            notes_log[note_index]["update_status"] = str(update_team_collabwriting)
            log.append(notes_log[note_index])

        create_log(
            log_storage_path=self.__log_storage_path,
            log=log,
            log_file_prefix="program_collabwriting_updated_",
        )
