from src.utils.csv_handler import read_csv, write_csv
from src.utils.hackmd_note import create_hackmd_note, update_hackmd_note
from src.utils.log import create_log
from src.utils.json_handler import read_json
from src.utils.note_template import get_note_template

TEMPLATE_GROUP_STORAGE_PATH = "note_template/"
NOTE_DATA_STORAGE_PATH = "note_data/"
OUTPUT_STORAGE_PATH = "output/"
LOG_STORAGE_PATH = "log/"


def raed_program_collabwriting_csv(program_collabwriting_data_file_name: str) -> dict:
    read_file_path = NOTE_DATA_STORAGE_PATH + program_collabwriting_data_file_name
    read_file_data = read_csv(file_path=read_file_path)

    program_collabwriting_title = read_file_data["title"]
    program_collabwriting_content = read_file_data["data"]

    program_collabwriting_content.sort(
        key=lambda x: (x["date"], x["begin_time"], x["type"], x["Room"])
    )

    return {
        "notes_title": program_collabwriting_title,
        "notes_content": program_collabwriting_content,
    }


def write_program_collabwriting_csv(
    output_file_name: str, notes_title: list, notes_content: list
) -> None:
    output_file_path = OUTPUT_STORAGE_PATH + output_file_name
    write_csv(file_path=output_file_path, title_items=notes_title, datas=notes_content)


def create_program_collabwriting(template_group_path: str, notes_content: list) -> list:
    log = []
    template_storage_path = TEMPLATE_GROUP_STORAGE_PATH + template_group_path

    collabwriting_template_path = template_storage_path + "collabwriting.md"

    for note_content in notes_content:
        collabwriting_content = get_note_template(
            file_path=collabwriting_template_path
        ).format(
            title=note_content["title"],
            name=note_content["name"],
            slido_1=note_content["Slido"],
            slide_link=note_content["slide"],
        )

        create_program_collabwriting_result = create_hackmd_note(
            content=collabwriting_content,
        )
        hackmd_link = create_program_collabwriting_result["publishLink"]
        note_content["HackMD"] = hackmd_link
        log.append(create_program_collabwriting_result)

        # print(collabwriting_content)

    # print(collabwriting_toc_content)
    create_log(log)

    return notes_content


def __init_last_note_content(last_note_content: dict, notes_title: list) -> None:
    for title in notes_title:
        last_note_content[title] = ""


# notes_content need to have each hacknmd_link of collabwriting that createn by creating program collabwriting
def create_program_collabwriting_toc(
    template_group_path: str, notes_title: list, notes_content: list
):
    log = []
    template_storage_path = TEMPLATE_GROUP_STORAGE_PATH + template_group_path

    collabwriting_toc_template_path = template_storage_path + "collabwriting_toc.md"
    collabwriting_toc_each_session_template_path = (
        template_storage_path + "collabwriting_toc_each_session.md"
    )
    collabwriting_toc_content = get_note_template(
        file_path=collabwriting_toc_template_path
    )

    last_note_content = {}
    __init_last_note_content(
        last_note_content=last_note_content, notes_title=notes_title
    )

    for note_content in notes_content:
        collabwriting_toc_content += get_program_collabwriting_toc_each_session(
            note_content=note_content,
            last_note_content=last_note_content,
            template_path=collabwriting_toc_each_session_template_path,
        )
        # print(collabwriting_content)
        last_note_content = note_content

    make_team_collabwriting_toc = create_hackmd_note(
        content=collabwriting_toc_content,
    )
    log.append(make_team_collabwriting_toc)

    # print(collabwriting_toc_content)
    create_log(log)


def get_program_collabwriting_toc_each_session(
    note_content: dict, last_note_content: dict, template_path: str
) -> str:
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

    return get_note_template(file_path=template_path).format(
        date=note_date,
        time=note_time,
        type=note_type,
        room=note_room,
        emoji=note_emoji,
        title=note_title,
        hackmd=note_hackmd,
    )


def update_program_collabwriting(
    notes_log_file_nane: str, template_group_path: str, notes_content: list
) -> None:
    template_storage_path = TEMPLATE_GROUP_STORAGE_PATH + template_group_path
    notes_log = read_json(LOG_STORAGE_PATH + notes_log_file_nane)

    note_quantity = len(notes_content)

    log = []

    collabwriting_template_path = template_storage_path + "collabwriting.md"

    for note_index in range(note_quantity):
        collabwriting_content = get_note_template(
            file_path=collabwriting_template_path
        ).format(
            title=notes_content[note_index]["title"],
            name=notes_content[note_index]["name"],
            slido_1=notes_content[note_index]["Slido"],
            slide_link=notes_content[note_index]["slide"],
        )
        note_id = notes_log[note_index]["shortId"]
        notes_content[note_index]["HackMD"] = notes_log[note_index]["publishLink"]
        update_team_collabwriting = update_hackmd_note(
            note_id=note_id,
            content=collabwriting_content,
        )
        notes_log[note_index]["update_status"] = str(update_team_collabwriting)
        log.append(notes_log[note_index])

    create_log(log)
