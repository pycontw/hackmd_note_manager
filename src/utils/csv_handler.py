import csv
import json


def read_csv(file_path: str) -> json:
    data = []
    with open(file_path, "r", encoding="utf-8-sig") as file:
        csvreader = list(csv.reader(file))

        titles = csvreader.pop(0)

        for row in csvreader:
            row_json = {}
            for i, title in enumerate(titles):
                try:
                    row_json[title] = row[i]
                except:
                    row_json[title] = ""
            data.append(row_json)

        return {"title": titles, "data": data}


def write_csv(file_path: str, title_items: list, datas: list):
    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        title = title_items
        csv_writer = csv.DictWriter(
            file, title, delimiter=",", quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writeheader()
        csv_writer.writerows(datas)
