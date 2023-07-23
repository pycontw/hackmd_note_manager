from src.utils.program_collabwriting import (
    raed_program_collabwriting_csv,
    write_program_collabwriting_csv,
    create_program_collabwriting,
    create_program_collabwriting_toc,
    update_program_collabwriting,
)


def raed_2022_program_collabwriting_csv(
    program_collabwriting_data_file_name: str = "WIP_ 2022 Pre-CFP empty schedule.csv",
) -> dict:
    return raed_program_collabwriting_csv(
        program_collabwriting_data_file_name=program_collabwriting_data_file_name
    )


def write_2022_program_collabwriting_csv(
    notes_title: list,
    notes_content: list,
    output_file_name: str = "WIP_ 2022 Pre-CFP empty schedule.csv",
) -> None:
    write_program_collabwriting_csv(
        output_file_name=output_file_name,
        notes_title=notes_title,
        notes_content=notes_content,
    )


def create_2022_program_collabwriting(
    notes_content: list, template_group_path: str = "pycon_apac_2022/"
) -> list:
    return create_program_collabwriting(
        template_group_path=template_group_path,
        notes_content=notes_content,
    )


def create_2022_program_collabwriting_toc(
    notes_title: list,
    notes_content: list,
    template_group_path: str = "pycon_apac_2022/",
) -> None:
    create_program_collabwriting_toc(
        template_group_path=template_group_path,
        notes_title=notes_title,
        notes_content=notes_content,
    )


"20220824-234052.json"


def update_2022_program_collabwriting(
    notes_log_file_nane: str,
    notes_content: list,
    template_group_path: str = "pycon_apac_2022/",
) -> None:
    update_program_collabwriting(
        notes_log_file_nane=notes_log_file_nane,
        template_group_path=template_group_path,
        notes_content=notes_content,
    )
