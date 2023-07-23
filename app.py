from src.utils.program_collabwriting import ProgramCollabwriting
from src.utils.program import raed_program_from_csv, write_program_to_csv

if __name__ == "__main__":
    PROGRAM_CSV_PATH = "note_data/WIP_ 2022 Pre-CFP empty schedule.csv"
    PROGRAM_OUTPUT_CSV_PATH = "output/WIP_ 2022 Pre-CFP empty schedule.csv"
    TEMPLATE_STORAGE_PATH = "note_template/pycon_apac_2022/"

    program_info = raed_program_from_csv(read_file_path=PROGRAM_CSV_PATH)
    program_info_title = program_info["notes_title"]
    program_info_content = program_info["notes_content"]

    program_collabwriting_2022 = ProgramCollabwriting(
        template_storage_path=TEMPLATE_STORAGE_PATH,
        notes_title=program_info_title,
        notes_content=program_info_content[:2],
    )

    program_collabwriting_2022.create_program_collabwriting()
    program_collabwriting_2022.create_program_collabwriting_toc()

    write_program_to_csv(
        output_file_path=PROGRAM_OUTPUT_CSV_PATH,
        notes_content=program_collabwriting_2022.get_notes_content(),
        notes_title=program_collabwriting_2022.get_notes_title(),
    )
