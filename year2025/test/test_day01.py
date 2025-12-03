from importlib.resources import files

import pytest
from pytest import MonkeyPatch

from year2025.day01 import (
    get_new_position,
    parse_input,
    solve,
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

    def test_when_rotated_r25_and_any_click(self) -> None:
        expected: tuple[int, int] = (75, 0)

        actual: tuple[int, int] = get_new_position(self.position, "R25", any_click=True)

        assert actual == expected

    def test_when_rotated_l25(self) -> None:
        expected: tuple[int, int] = (25, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L25")

        assert actual == expected

    def test_when_rotated_l25_and_any_click(self) -> None:
        expected: tuple[int, int] = (25, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L25", any_click=True)

        assert actual == expected

    def test_when_rotated_r50(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R50")

        assert actual == expected

    def test_when_rotated_r50_and_any_click(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R50", any_click=True)

        assert actual == expected

    def test_when_rotated_l50(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L50")

        assert actual == expected

    def test_when_rotated_l50_and_any_click(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L50", any_click=True)

        assert actual == expected

    def test_when_rotated_r100(self) -> None:
        expected: tuple[int, int] = (50, 0)

        actual: tuple[int, int] = get_new_position(self.position, "R100")

        assert actual == expected

    def test_when_rotated_r100_and_any_click(self) -> None:
        expected: tuple[int, int] = (50, 1)

        actual: tuple[int, int] = get_new_position(
            self.position, "R100", any_click=True
        )

        assert actual == expected

    def test_when_rotated_l100(self) -> None:
        expected: tuple[int, int] = (50, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L100")

        assert actual == expected

    def test_when_rotated_l100_and_any_click(self) -> None:
        expected: tuple[int, int] = (50, 1)

        actual: tuple[int, int] = get_new_position(
            self.position, "L100", any_click=True
        )

        assert actual == expected

    def test_when_rotated_r125(self) -> None:
        expected: tuple[int, int] = (75, 0)

        actual: tuple[int, int] = get_new_position(self.position, "R125")

        assert actual == expected

    def test_when_rotated_r125_and_any_click(self) -> None:
        expected: tuple[int, int] = (75, 1)

        actual: tuple[int, int] = get_new_position(
            self.position, "R125", any_click=True
        )

        assert actual == expected

    def test_when_rotated_l125(self) -> None:
        expected: tuple[int, int] = (25, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L125")

        assert actual == expected

    def test_when_rotated_l125_any_click(self) -> None:
        expected: tuple[int, int] = (25, 1)

        actual: tuple[int, int] = get_new_position(
            self.position, "L125", any_click=True
        )

        assert actual == expected

    def test_when_rotated_r150(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "R150")

        assert actual == expected

    def test_when_rotated_r150_and_any_click(self) -> None:
        expected: tuple[int, int] = (0, 2)

        actual: tuple[int, int] = get_new_position(
            self.position, "R150", any_click=True
        )

        assert actual == expected

    def test_when_rotated_l150(self) -> None:
        expected: tuple[int, int] = (0, 1)

        actual: tuple[int, int] = get_new_position(self.position, "L150")

        assert actual == expected

    def test_when_rotated_l150_any_click(self) -> None:
        expected: tuple[int, int] = (0, 2)

        actual: tuple[int, int] = get_new_position(
            self.position, "L150", any_click=True
        )

        assert actual == expected

    def test_when_rotated_r1000(self) -> None:
        expected: tuple[int, int] = (50, 0)

        actual: tuple[int, int] = get_new_position(self.position, "R1000")

        assert actual == expected

    def test_when_rotated_r1000_and_any_click(self) -> None:
        expected: tuple[int, int] = (50, 10)

        actual: tuple[int, int] = get_new_position(
            self.position, "R1000", any_click=True
        )

        assert actual == expected

    def test_when_rotated_l1000(self) -> None:
        expected: tuple[int, int] = (50, 0)

        actual: tuple[int, int] = get_new_position(self.position, "L1000")

        assert actual == expected

    def test_when_rotated_l1000_and_any_click(self) -> None:
        expected: tuple[int, int] = (50, 10)

        actual: tuple[int, int] = get_new_position(
            self.position, "L1000", any_click=True
        )

        assert actual == expected

    def test_when_rotated_r5_from_0(self) -> None:
        expected: tuple[int, int] = (5, 0)

        actual: tuple[int, int] = get_new_position(0, "R5")

        assert actual == expected

    def test_when_rotated_r5_from_0_and_any_click(self) -> None:
        expected: tuple[int, int] = (5, 0)

        actual: tuple[int, int] = get_new_position(0, "R5", any_click=True)

        assert actual == expected

    def test_when_rotated_l5_from_0(self) -> None:
        expected: tuple[int, int] = (95, 0)

        actual: tuple[int, int] = get_new_position(0, "L5")

        assert actual == expected

    def test_when_rotated_l5_from_0_and_any_click(self) -> None:
        expected: tuple[int, int] = (95, 0)

        actual: tuple[int, int] = get_new_position(0, "L5", any_click=True)

        assert actual == expected


class TestSolve:
    def test_puzzle_1_when_test_input(self, mock_input: None) -> None:
        expected: int = 3

        actual: int = solve()

        assert actual == expected

    def test_puzzle_1_when_real_input(self) -> None:
        expected: int = 1180

        actual: int = solve()

        assert actual == expected

    def test_puzzle_2_when_test_input(self, mock_input: None) -> None:
        expected: int = 6

        actual: int = solve(any_click=True)

        assert actual == expected

    def test_puzzle_2_when_real_input(self) -> None:
        expected: int = 6892

        actual: int = solve(any_click=True)

        assert actual == expected
