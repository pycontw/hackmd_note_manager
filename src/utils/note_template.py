def get_note_template(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
