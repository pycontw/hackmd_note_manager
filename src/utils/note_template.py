def get_note_template(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data
