def create_collabwriting(note_info, last_note_info):
    note_date = ""
    note_time = ""
    note_type = ""
    note_emoji = ""
    note_room = "R" + note_info["Room"]
    note_title = note_info["title"] + " - " + note_info["name"]
    note_hackmd = note_info["HackMD"]

    if note_info["date"] != last_note_info["date"]:
        note_date = "\n# " + note_info["date"] + ""

    if (
        note_info["date"] != last_note_info["date"]
        or note_info["type"] != last_note_info["type"]
        or note_info["begin_time"] != last_note_info["begin_time"]
        or note_info["end_time"] != last_note_info["end_time"]
    ):
        if note_info["type"] != "Talk":
            note_type = " (" + note_info["type"] + ")\n"
        else:
            note_type = "\n"
        note_time = "\n## " + note_info["begin_time"] + " ~ " + note_info["end_time"]

        if note_info["type"] == "Keynote":
            note_emoji = "🔸"

    if note_info["Room"] == "Stage":
        note_room = "R0、R1、R2、R3"

    conference_template_path = TEMPLATE_PATH + "each_session.md"

    return get_note_template(conference_template_path).format(
        date=note_date,
        time=note_time,
        type=note_type,
        room=note_room,
        emoji=note_emoji,
        title=note_title,
        hackmd=note_hackmd,
    )
