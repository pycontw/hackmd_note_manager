from src.config.config import settings
from src.utils.program_collabwriting import ProgramCollabwriting
from src.utils.program import raed_program_from_csv, write_program_to_csv
from src.utils.hackmd_note import HackmdNote
from src.utils.url_processor import join_url


def execute_program_collabwriting_2022(hackmd_note: HackmdNote):
    PROGRAM_CSV_PATH_2022 = "note_data/WIP_ 2022 Pre-CFP empty schedule.csv"
    PROGRAM_OUTPUT_CSV_PATH_2022 = "output/WIP_ 2022 Pre-CFP empty schedule.csv"
    TEMPLATE_STORAGE_PATH_2022 = "note_template/pycon_apac_2022/"

    program_info = raed_program_from_csv(read_file_path=PROGRAM_CSV_PATH_2022)
    program_info_title = program_info.notes_title
    program_info_content = program_info.notes_content

    program_collabwriting_2022 = ProgramCollabwriting(
        hackmd_note=hackmd_note,
        template_storage_path=TEMPLATE_STORAGE_PATH_2022,
        notes_title=program_info_title,
        notes_content=program_info_content[],
    )

    program_collabwriting_2022.create_program_collabwriting()
    program_collabwriting_2022.create_program_collabwriting_toc()

    write_program_to_csv(
        output_file_path=PROGRAM_OUTPUT_CSV_PATH_2022,
        notes_content=program_collabwriting_2022.get_notes_content(),
        notes_title=program_collabwriting_2022.get_notes_title(),
    )


if __name__ == "__main__":
    HACKMD_API_USER_API_ROUTE = ""
    HACKMD_API_TEAMS_API_ROUTE = join_url(
        base_url="teams", relative_url=settings.TEAM_PATH
    )

    hackmd_note = HackmdNote(hackmd_api_route=HACKMD_API_TEAMS_API_ROUTE)

    execute_program_collabwriting_2022(hackmd_note=hackmd_note)
