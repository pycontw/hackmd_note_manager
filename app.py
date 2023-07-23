from src.api.program_collabwriting_2022.app import (
    raed_2022_program_collabwriting_csv,
    write_2022_program_collabwriting_csv,
    create_2022_program_collabwriting,
    create_2022_program_collabwriting_toc,
)

if __name__ == "__main__":
    note_data = raed_2022_program_collabwriting_csv()
    notes_title = note_data["notes_title"]
    notes_content = note_data["notes_content"]
    notes_content = create_2022_program_collabwriting(notes_content=notes_content[:2])
    write_2022_program_collabwriting_csv(
        notes_title=notes_title, notes_content=notes_content
    )
    create_2022_program_collabwriting_toc(
        notes_title=notes_title, notes_content=notes_content[:2]
    )
