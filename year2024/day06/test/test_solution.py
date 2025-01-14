import pytest
import year2024.day06.solution as solution
from year2024.day06.solution import Direction, Guard, Map, Offsets, Position


MAP_FILE_PATH: str = r"year2024\day06\test\resource\map.txt"


MAP: Map = [
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

OBSTACLES: set[Position] = {
    Position(0, 4),
    Position(1, 9),
    Position(3, 2),
    Position(4, 7),
    Position(6, 1),
    Position(7, 8),
    Position(8, 0),
    Position(9, 6),
}

#   0123456789
# 0 ....#.....
# 1 ....^>>>>#
# 2 ....^...v.
# 3 ..#.^...v.
# 4 ..^>>>>#v.
# 5 ..^.^.v.v.
# 6 .#<<<<v<v.
# 7 .^>>>>>>#.
# 8 #<<<<<vv..
# 9 ......#v..
VISITED: set[Position] = {
    # ^ 5
    Position(5, 4),
    Position(4, 4),
    Position(3, 4),
    Position(2, 4),
    Position(1, 4),
    # > 4
    Position(1, 5),
    Position(1, 6),
    Position(1, 7),
    Position(1, 8),
    # v 5
    Position(2, 8),
    Position(3, 8),
    Position(4, 8),
    Position(5, 8),
    Position(6, 8),
    # < 6
    Position(6, 7),
    Position(6, 6),
    Position(6, 5),
    Position(6, 4),
    Position(6, 3),
    Position(6, 2),
    # ^ 2
    Position(5, 2),
    Position(4, 2),
    # > 4
    Position(4, 3),
    Position(4, 4),
    Position(4, 5),
    Position(4, 6),
    # v 4
    Position(5, 6),
    Position(6, 6),
    Position(7, 6),
    Position(8, 6),
    # < 5
    Position(8, 5),
    Position(8, 4),
    Position(8, 3),
    Position(8, 2),
    Position(8, 1),
    # ^ 1
    Position(7, 1),
    # > 6
    Position(7, 2),
    Position(7, 3),
    Position(7, 4),
    Position(7, 5),
    Position(7, 6),
    Position(7, 7),
    # v 2
    Position(8, 7),
    Position(9, 7),
}

PART_1_ANSWER: int = 41


@pytest.mark.parametrize(
    "direction, expected",
    [
        (Direction.UP, Offsets(-1, 0)),
        (Direction.DOWN, Offsets(1, 0)),
        (Direction.LEFT, Offsets(0, -1)),
        (Direction.RIGHT, Offsets(0, 1)),
    ],
)
def test_direction_offset(direction: Direction, expected: Offsets) -> None:
    assert direction.offsets == expected


def test_parse_map() -> None:
    assert solution.parse_map(MAP_FILE_PATH) == MAP


def test_find_guard() -> None:
    assert solution.find_guard(MAP) == Guard(Position(6, 4), Direction.UP)


def test_find_obstacles() -> None:
    assert solution.find_obstacles(MAP) == OBSTACLES


@pytest.mark.parametrize(
    "position, expected",
    [
        (
            Guard(Position(1, 4), Direction.UP),
            [
                Position(1, 4),
                Position(0, 4),
            ],
        ),
        (
            Guard(Position(1, 4), Direction.DOWN),
            [
                Position(1, 4),
                Position(2, 4),
                Position(3, 4),
                Position(4, 4),
                Position(5, 4),
                Position(6, 4),
                Position(7, 4),
                Position(8, 4),
                Position(9, 4),
            ],
        ),
        (
            Guard(Position(1, 4), Direction.LEFT),
            [
                Position(1, 4),
                Position(1, 3),
                Position(1, 2),
                Position(1, 1),
                Position(1, 0),
            ],
        ),
        (
            Guard(Position(1, 4), Direction.RIGHT),
            [
                Position(1, 4),
                Position(1, 5),
                Position(1, 6),
                Position(1, 7),
                Position(1, 8),
                Position(1, 9),
            ],
        ),
    ],
)
def test_get_path(position: Guard, expected: set[Position]) -> None:
    assert solution.get_path(MAP, position) == expected


@pytest.mark.parametrize(
    "path, direction, expected",
    [
        (
            [Position(0, 4)],
            Direction.UP,
            Position(0, 4),
        ),
        (
            [
                Position(2, 4),
                Position(3, 4),
                Position(4, 4),
                Position(5, 4),
                Position(6, 4),
                Position(7, 4),
                Position(8, 4),
                Position(9, 4),
            ],
            Direction.DOWN,
            None,
        ),
        (
            [
                Position(1, 3),
                Position(1, 2),
                Position(1, 1),
                Position(1, 0),
            ],
            Direction.LEFT,
            None,
        ),
        (
            [
                Position(1, 5),
                Position(1, 6),
                Position(1, 7),
                Position(1, 8),
                Position(1, 9),
            ],
            Direction.RIGHT,
            Position(1, 9),
        ),
    ],
)
def test_find_obstacle_in_path(path: set[Position], direction: Direction, expected: Position) -> None:
    assert solution.find_obstacle_in_path(path, direction, OBSTACLES) == expected


@pytest.mark.parametrize(
    "path, direction, obstacle, expected",
    #   0 1 2 3 4
    # 0 . . # . .
    # 1 . . . . .
    # 2 # . x . #
    # 3 . . . . .
    # 4 . . # . .
    [
        (
            [
                Position(1, 2),
                Position(0, 2),
            ],
            Direction.UP,
            Position(0, 2),
            [Position(1, 2)],
        ),
        (
            [
                Position(3, 2),
                Position(4, 2),
            ],
            Direction.DOWN,
            Position(4, 2),
            [Position(3, 2)],
        ),
        (
            [
                Position(2, 1),
                Position(2, 0),
            ],
            Direction.LEFT,
            Position(2, 0),
            [Position(2, 1)],
        ),
        (
            [
                Position(2, 3),
                Position(2, 4),
            ],
            Direction.RIGHT,
            Position(2, 4),
            [Position(2, 3)],
        ),
    ],
)
def test_get_positions_visited_in_path(
    path: set[Position],
    direction: Direction,
    obstacle: Position,
    expected: list[Position],
) -> None:
    assert solution.get_positions_visited_in_path(path, direction, obstacle) == expected


@pytest.mark.parametrize(
    "direction, expected",
    [
        (Direction.UP, Direction.RIGHT),
        (Direction.RIGHT, Direction.DOWN),
        (Direction.DOWN, Direction.LEFT),
        (Direction.LEFT, Direction.UP),
    ],
)
def test_turn_guard(direction: Direction, expected: Direction) -> None:
    assert solution.turn_guard(direction) == expected


@pytest.mark.parametrize(
    "guard, expected",
    [
        (
            Guard(Position(1, 4), Direction.UP),
            (Guard(Position(1, 4), Direction.RIGHT), {Position(1, 4)}),
        ),
        (
            Guard(Position(1, 4), Direction.DOWN),
            (
                None,
                {
                    Position(1, 4),
                    Position(2, 4),
                    Position(3, 4),
                    Position(4, 4),
                    Position(5, 4),
                    Position(6, 4),
                    Position(7, 4),
                    Position(8, 4),
                    Position(9, 4),
                },
            ),
        ),
        (
            Guard(Position(1, 4), Direction.LEFT),
            (
                None,
                {
                    Position(1, 4),
                    Position(1, 3),
                    Position(1, 2),
                    Position(1, 1),
                    Position(1, 0),
                },
            ),
        ),
        (
            Guard(Position(1, 4), Direction.RIGHT),
            (
                Guard(Position(1, 8), Direction.DOWN),
                {
                    Position(1, 4),
                    Position(1, 5),
                    Position(1, 6),
                    Position(1, 7),
                    Position(1, 8),
                },
            ),
        ),
    ],
)
def test_move_guard(guard: Guard, expected: tuple[Guard | None, set[Position]]) -> None:
    assert solution.move_guard(MAP, OBSTACLES, guard) == expected


def test_get_positions_visited() -> None:
    assert solution.get_positions_visited(MAP) == VISITED


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(MAP) == PART_1_ANSWER
