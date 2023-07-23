from src.collabwriting.app import (
    get_collabwriting,
    update_collabwriting,
    output_collabwriting,
)

if __name__ == "__main__":
    note_data = get_collabwriting()
    notes_title = note_data["notes_title"]
    notes_info = note_data["notes_info"]

    update_collabwriting(notes_info)

    output_collabwriting(notes_title, notes_info)
