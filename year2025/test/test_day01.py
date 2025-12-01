from importlib.resources import files

import pytest
from pytest import MonkeyPatch

from year2025.day01 import (
    get_new_position,
    parse_input,
    solve_puzzle_1,
    solve_puzzle_2,
)

RESOURCE_ANCHOR: str = "year2025.test.resources"

INPUT: str = files(RESOURCE_ANCHOR).joinpath("day01.txt").read_text()


@pytest.fixture
def mock_input(monkeypatch: MonkeyPatch) -> None:
    import year2025.day01

    monkeypatch.setattr(year2025.day01, "INPUT", INPUT)


class TestParseInput:
    def test_parse_input(self, mock_input: None) -> None:
        expected: list[str] = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]

        actual: list[str] = parse_input()

        assert actual == expected


class TestGetNewPosition:
    position: int = 50

    def test_when_rotated_r25(self) -> None:
        expected: tuple[int, int] = (75, 0)

        actual: tuple[int, int] = get_new_position(self.position, "R25")

        assert actual == expected

    def test_when_rotated_l25(self) -> None:
        expected: tuple[int, int] = (25, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L25")

        assert actual == expected

    def test_when_rotated_r50(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R50")

        assert actual == expected

    def test_when_rotated_l50(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L50")

        assert actual == expected

    def test_when_rotated_r100(self) -> None:
        expected: tuple[int, int] = (50, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R100")

        assert actual == expected

    def test_when_rotated_l100(self) -> None:
        expected: tuple[int, int] = (50, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L100")

        assert actual == expected

    def test_when_rotated_r125(self) -> None:
        expected: tuple[int, int] = (75, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R125")

        assert actual == expected

    def test_when_rotated_l125(self) -> None:
        expected: tuple[int, int] = (25, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L125")

        assert actual == expected

    def test_when_rotated_r1000(self) -> None:
        expected: tuple[int, int] = (50, 10)

        actual: tuple[int, int] = get_new_position(self.position, "R1000")

        assert actual == expected

    def test_when_rotated_l1000(self) -> None:
        expected: tuple[int, int] = (50, 10)

        actual: tuple[int, int] = get_new_position(self.position, "L1000")

        assert actual == expected

    def test_when_rotated_r5_from_0(self) -> None:
        expected: tuple[int, int] = (5, 0)

        actual: tuple[int, int] = get_new_position(0, "R5")

        assert actual == expected

    def test_when_rotated_l5_from_0(self) -> None:
        expected: tuple[int, int] = (95, 0)

        actual: tuple[int, int] = get_new_position(0, "L5")

        assert actual == expected


class TestSolvePuzzle1:
    def test_solve_puzzle_1(self, mock_input: None) -> None:
        expected: int = 3

        actual: int = solve_puzzle_1()

        assert actual == expected


class TestSolvePuzzle2:
    def test_solve_puzzle_2(self, mock_input: None) -> None:
        expected: int = 6

        actual: int = solve_puzzle_2()

        assert actual == expected
