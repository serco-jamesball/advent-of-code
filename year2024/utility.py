import pandas
import re
from pandas import DataFrame
from pathlib import Path
from re import Pattern


FOLDER_NAME_PATTERN: Pattern = re.compile(r"^[a-z]+([0-9]+$)")

INPUT_FILE_NAME: str = "input.csv"

ANSWER_MESSAGE: str = "day {day}: part {part}: answer: {answer}"


def get_input_file_path(file_path: str) -> Path:
    return Path(file_path).parent.joinpath('resource', INPUT_FILE_NAME)


def get_column_labels(file_path: Path) -> int:
    return list(
        range(max(open(file_path), key=lambda line: line.count(",")).count(",") + 1)
    )


def get_input(file_path: str) -> DataFrame:
    input_file_path: Path = get_input_file_path(file_path)
    return pandas.read_csv(input_file_path, names=get_column_labels(input_file_path))


def get_answer_message(day: str, **answers) -> str:
    message: str = ""
    for i, (key, value) in enumerate(answers.items(), start=1):
        message += ANSWER_MESSAGE.format(day=day, part=key.split("_")[-1], answer=str(value))
        if i < len(answers):
            message += "\n"
    return message
