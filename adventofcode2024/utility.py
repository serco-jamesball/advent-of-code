import re
from pathlib import Path
from re import Pattern


FOLDER_NAME_PATTERN: Pattern = re.compile(r"^[a-z]+([0-9]+$)")

INPUT_FILE_NAME: str = "input.csv"

ANSWER_MESSAGE: str = "day {day}: part {part}: answer: {answer}"


def get_input_file_path(file_path: Path) -> Path:
    return file_path.parent.joinpath(INPUT_FILE_NAME)


def parse_file_path(file_path: Path) -> tuple[str, str]:
    day: str = re.match(FOLDER_NAME_PATTERN, file_path.parent.parent.stem).group(1)
    part: str = re.match(FOLDER_NAME_PATTERN, file_path.parent.stem).group(1)

    return (
        day,
        part,
    )


def get_answer_message(file_path: Path, answer: int) -> str:
    day, part = parse_file_path(file_path)

    return ANSWER_MESSAGE.format(day=day, part=part, answer=str(answer))
