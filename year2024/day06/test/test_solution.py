import year2024.day06.solution as solution


MAP_FILE_PATH: str = r"year2024\day06\test\resource\map.txt"

MAP: list[str] = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]

GUARD: tuple[int, int] = (6, 4)

OBSTACLES: frozenset[tuple[int, int]] = frozenset(
    {
        (0, 4),
        (1, 9),
        (3, 2),
        (4, 7),
        (6, 1),
        (7, 8),
        (8, 0),
        (9, 6),
    }
)

#   0123456789
# 0 ....#.....
# 1 ....+---+#
# 2 ....|...|.
# 3 ..#.|...|.
# 4 ..+-+-+#|.
# 5 ..|.|.|.|.
# 6 .#--^+-+.
# 7 .+----++#.
# 8 #+----+|..
# 9 ......#|..
VISITED: set[tuple[tuple[int, int], int]] = {
    # ^ 6
    ((6, 4), 0),
    ((5, 4), 0),
    ((4, 4), 0),
    ((3, 4), 0),
    ((2, 4), 0),
    ((1, 4), 0),
    # > 5
    ((1, 4), 1),
    ((1, 5), 1),
    ((1, 6), 1),
    ((1, 7), 1),
    ((1, 8), 1),
    # v 6
    ((1, 8), 2),
    ((2, 8), 2),
    ((3, 8), 2),
    ((4, 8), 2),
    ((5, 8), 2),
    ((6, 8), 2),
    # < 7
    ((6, 8), 3),
    ((6, 7), 3),
    ((6, 6), 3),
    ((6, 5), 3),
    ((6, 4), 3),
    ((6, 3), 3),
    ((6, 2), 3),
    # ^ 3
    ((6, 2), 0),
    ((5, 2), 0),
    ((4, 2), 0),
    # > 5
    ((4, 2), 1),
    ((4, 3), 1),
    ((4, 4), 1),
    ((4, 5), 1),
    ((4, 6), 1),
    # v 5
    ((4, 6), 2),
    ((5, 6), 2),
    ((6, 6), 2),
    ((7, 6), 2),
    ((8, 6), 2),
    # < 6
    ((8, 6), 3),
    ((8, 5), 3),
    ((8, 4), 3),
    ((8, 3), 3),
    ((8, 2), 3),
    ((8, 1), 3),
    # ^ 1
    ((8, 1), 0),
    ((7, 1), 0),
    # > 7
    ((7, 1), 1),
    ((7, 2), 1),
    ((7, 3), 1),
    ((7, 4), 1),
    ((7, 5), 1),
    ((7, 6), 1),
    ((7, 7), 1),
    # v 2
    ((7, 7), 2),
    ((8, 7), 2),
    ((9, 7), 2),
}

PART_1_ANSWER: int = 41
PART_2_ANSWER: int = 6


def test_get_map() -> None:
    assert solution.get_map(MAP_FILE_PATH) == MAP


def test_find_guard() -> None:
    assert solution.find_guard(MAP) == GUARD


def test_find_obstacles() -> None:
    assert solution.find_obstacles(MAP) == OBSTACLES


def test_patrol() -> None:
    assert solution.patrol(MAP, GUARD, OBSTACLES) == VISITED


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(VISITED) == PART_1_ANSWER
