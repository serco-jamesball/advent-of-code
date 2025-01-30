import pytest
import year2024.day08.solution as solution
from collections import defaultdict
from year2024.day08.solution import Frequency, Map, Position


MAP_FILE_PATH: str = r"year2024\day08\test\resource\map.txt"

MAP: Map = (
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
)

BOUNDS: tuple[int, int] = (12, 12)

ANTENNAS: dict[Frequency, set[Position]] = {
    "A": {
        (5, 6),
        (8, 8),
        (9, 9),
    },
    "0": {
        (1, 8),
        (2, 5),
        (3, 7),
        (4, 4),
    },
}

#  012345678901
# 0......#....#
# 1...#....0...
# 2....#0....#.
# 3..#....0....
# 4....0....#..
# 5.#....A.....
# 6...#........
# 7#......#....
# 8........A...
# 9.........A..
# 0..........#.
# 1..........#.
PART_1_ANTINODES: dict[Frequency, set[Position]] = {
    "A": {
        (1, 3),
        (2, 4),
        (7, 7),
        (10, 10),
        (11, 10),
    },
    "0": {
        (0, 6),
        (0, 11),
        (1, 3),
        (2, 10),
        (3, 2),
        (4, 9),
        (5, 1),
        (5, 6),
        (6, 3),
        (7, 0),
    },
}

#  012345678901
# 0##....#....#
# 1.#.#....0...
# 2..#.#0....#.
# 3..##...0....
# 4....0....#..
# 5.#...#A....#
# 6...#..#.....
# 7#....#.#....
# 8..#.....A...
# 9....#....A..
# 0.#........#.
# 1...#......##
#
# nb: Antennas are also antinodes
PART_2_ANTINODES: dict[Frequency, set[Position]] = {
    "A": {
        (0, 0),
        (1, 1),
        (1, 3),
        (2, 2),
        (2, 4),
        (3, 3),
        (4, 4),
        (5, 5),
        (5, 6),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 10),
        (11, 11),
    },
    "0": {
        (0, 1),
        (0, 6),
        (0, 11),
        (1, 3),
        (1, 8),
        (2, 5),
        (2, 10),
        (3, 2),
        (3, 7),
        (4, 4),
        (4, 9),
        (5, 1),
        (5, 6),
        (5, 11),
        (6, 3),
        (7, 0),
        (7, 5),
        (8, 2),
        (9, 4),
        (10, 1),
        (11, 3),
    },
}

PART_1_ANSWER: int = 14
PART_2_ANSWER: int = 34


def test_get_map() -> None:
    assert solution.get_map(MAP_FILE_PATH)


def test_get_bounds() -> None:
    assert solution.get_bounds(MAP) == BOUNDS


def test_get_antennas() -> None:
    assert solution.get_antennas(MAP) == ANTENNAS


@pytest.mark.parametrize(
    "is_resonant_harmonics_effect_applied, expected",
    [
        (False, PART_1_ANTINODES),
        (True, PART_2_ANTINODES),
    ],
)
def test_get_antinodes(
    is_resonant_harmonics_effect_applied: bool,
    expected: defaultdict[Frequency, set[Position]],
) -> None:
    assert (
        solution.get_antinodes(ANTENNAS, BOUNDS, is_resonant_harmonics_effect_applied)
        == expected
    )


@pytest.mark.parametrize(
    "antinodes, expected",
    [
        (PART_1_ANTINODES, PART_1_ANSWER),
        (PART_2_ANTINODES, PART_2_ANSWER),
    ],
)
def test_get_answer(
    antinodes: defaultdict[Frequency, set[Position]], expected: int
) -> None:
    assert solution.get_answer(antinodes) == expected
