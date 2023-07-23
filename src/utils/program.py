from dataclasses import dataclass

from src.utils.csv_handler import read_csv, write_csv


@dataclass
class Program:
    notes_title: list
    notes_content: list


def raed_program_from_csv(read_file_path: str) -> Program:
    read_file_data = read_csv(file_path=read_file_path)

    program_collabwriting_title = read_file_data["title"]
    program_collabwriting_content = read_file_data["data"]

    program_collabwriting_content.sort(
        key=lambda x: (x["date"], x["begin_time"], x["type"], x["Room"])
    )

    return Program(
        notes_title=program_collabwriting_title,
        notes_content=program_collabwriting_content,
    )


def write_program_to_csv(
    output_file_path: str, notes_title: list, notes_content: list
) -> None:
    write_csv(file_path=output_file_path, title_items=notes_title, datas=notes_content)
