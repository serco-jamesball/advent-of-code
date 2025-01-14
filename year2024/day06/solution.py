import re
import year2024.utility as utility
from collections import namedtuple
from enum import StrEnum
from re import Pattern


DAY: str = "6"

MAP_FILE_PATH: str = r"year2024\day06\resource\map.txt"

GUARD: str = "^"
OBSTACLE: str = "#"


GridLine = list[str]
Map = list[GridLine]

Position = namedtuple("Position", ["x", "y"])
Offsets = namedtuple("Offsets", ["x", "y"])

Guard = namedtuple("Guard", ["position", "direction"])


class Direction(StrEnum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    @property
    def offsets(self) -> Offsets:
        match self.value:
            case "^":
                return Offsets(-1, 0)
            case "v":
                return Offsets(1, 0)
            case "<":
                return Offsets(0, -1)
            case ">":
                return Offsets(0, 1)


def parse_map(map_file_path: str) -> Map:
    with open(map_file_path) as map_file:
        return [line for line in map_file.read().strip().split("\n")]


def find_guard(map: Map) -> Guard | None:
    for x, grid_line in enumerate(map):
        for y, point in enumerate(grid_line):
            if point == GUARD:
                return Guard(Position(x, y), Direction.UP)


def find_obstacles(map: Map) -> set[Position]:
    return {
        Position(x, y)
        for x, grid_line in enumerate(map)
        for y, point in enumerate(grid_line)
        if point == OBSTACLE
    }


def get_path(map: Map, guard: Guard) -> list[Position]:
    path: list[Position] = []

    offset_x, offset_y = guard.position.x, guard.position.y

    while (
        offset_x > -1
        and offset_x < len(map)
        and offset_y > -1
        and offset_y < len(map[guard.position.x])
    ):
        path.append(Position(offset_x, offset_y))

        offset_x += guard.direction.offsets.x
        offset_y += guard.direction.offsets.y

    return path


def find_obstacle_in_path(
    path: list[Position], direction: Direction, obstacles: set[Position]
) -> Position | None:
    if obstacles := list(set(path) & obstacles):
        match direction:
            case Direction.UP | Direction.LEFT:
                return sorted(obstacles, reverse=True)[0]
            case Direction.DOWN | Direction.RIGHT:
                return sorted(obstacles)[0]


def get_positions_visited_in_path(
    path: list[Position], direction: Direction, obstacle: Position
) -> list[Position]:
    match direction:
        case Direction.UP:
            return [position for position in path if position.x > obstacle.x]
        case Direction.DOWN:
            return [position for position in path if position.x < obstacle.x]
        case Direction.LEFT:
            return [position for position in path if position.y > obstacle.y]
        case Direction.RIGHT:
            return [position for position in path if position.y < obstacle.y]


def turn_guard(direction: Direction) -> Direction:
    match direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP


def move_guard(
    map: Map, obstacles: set[Position], guard: Guard
) -> tuple[Guard | None, set[Position]]:
    path: list[Position] = get_path(map, guard)

    if obstacle := find_obstacle_in_path(path, guard.direction, obstacles):
        visited: list[Position] = get_positions_visited_in_path(
            path, guard.direction, obstacle
        )

        position: Position = visited[-1] if visited else guard.position
        direction: Direction = turn_guard(guard.direction)

        return Guard(position, direction), set(visited)

    return None, set(path)


def get_positions_visited(map: Map) -> set[Position]:
    guard: Guard = find_guard(map)
    obstacles: set[Position] = find_obstacles(map)

    visited: set[Position] = set()
    is_guard_in_mapped_area: bool = True

    while is_guard_in_mapped_area:
        guard, positions = move_guard(map, obstacles, guard)
        visited = visited | positions
        is_guard_in_mapped_area = guard is not None

    return visited


def get_part_1_answer(map: Map) -> int:
    return len(get_positions_visited(map))


if __name__ == "__main__":
    map: Map = parse_map(MAP_FILE_PATH)

    part_1_answer: int = get_part_1_answer(map)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))
