import pytest
import utility
from pandas import DataFrame
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


@pytest.mark.parametrize(
    "file_path, expected",
    [
        (
            Path(r"adventofcode2024\day1\part1\input.csv"),
            [0, 1],
        ),
        (
            Path(r"adventofcode2024\day2\part1\input.csv"),
            [0, 1, 2, 3, 4, 5, 6, 7],
        ),
    ],
)
def test_get_column_labels(file_path: Path, expected: int) -> None:
    assert utility.get_column_labels(file_path) == expected


def test_get_dataframe() -> None:
    assert utility.get_dataframe(
        Path(r"adventofcode2024\day2\part1\test\input.csv")
    ).equals(
        DataFrame(
            [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ]
        )
    )
