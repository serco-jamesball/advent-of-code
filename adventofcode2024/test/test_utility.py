import pytest
import utility
from pathlib import Path


def test_get_input_file_path() -> None:
    file_path: Path = Path(r"adventofcode2024\day1\part1\solution.py")

    assert utility.get_input_file_path(file_path) == Path(
        r"adventofcode2024\day1\part1\input.csv"
    )


@pytest.mark.parametrize(
    "file_path, expected",
    [
        (
            Path(r"adventofcode2024\day1\part1\solution.py"),
            (
                "1",
                "1",
            ),
        ),
        (
            Path(r"adventofcode2024\day24\part2\solution.py"),
            (
                "24",
                "2",
            ),
        ),
    ],
)
def test_parse_file_path(file_path: Path, expected: tuple[str, str]) -> None:
    assert utility.parse_file_path(file_path) == expected


def test_get_answer_message() -> None:
    assert (
        utility.get_answer_message(
            Path(r"adventofcode2024\day1\part1\solution.py"), "123"
        )
        == "day 1: part 1: answer: 123"
    )
