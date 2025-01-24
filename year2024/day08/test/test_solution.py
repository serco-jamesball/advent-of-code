import year2024.day08.solution as solution
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
ANTINODES: dict[Frequency, set[Position]] = {
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

PART_1_ANSWER: int = 14


def test_get_map() -> None:
    assert solution.get_map(MAP_FILE_PATH)


def test_get_bounds() -> None:
    assert solution.get_bounds(MAP) == BOUNDS


def test_get_antennas() -> None:
    assert solution.get_antennas(MAP) == ANTENNAS


def test_get_antinodes() -> None:
    assert solution.get_antinodes(ANTENNAS, BOUNDS) == ANTINODES


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(ANTINODES) == PART_1_ANSWER
