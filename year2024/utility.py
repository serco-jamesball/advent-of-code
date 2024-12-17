from pathlib import Path


ANSWER_MESSAGE: str = "day {day}: part {part}: answer: {answer}"


def get_column_labels(file_path: Path) -> list[int]:
    return list(
        range(max(open(file_path), key=lambda line: line.count(",")).count(",") + 1)
    )


def get_answer_message(day: str, **answers) -> str:
    message: str = ""
    for i, (key, value) in enumerate(answers.items(), start=1):
        message += ANSWER_MESSAGE.format(
            day=day, part=key.split("_")[-1], answer=str(value)
        )
        if i < len(answers):
            message += "\n"
    return message
