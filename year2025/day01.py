from collections.abc import Iterator
from importlib.resources import files

from year2025.utils import output_answer

RESOURCE_ANCHOR: str = "year2025.resources"

INPUT: str = files(RESOURCE_ANCHOR).joinpath("day01.txt").read_text()


def parse_input() -> list[str]:
    return INPUT.strip().split("\n")


def get_new_position(position: int, rotation: str) -> tuple[int, int]:
    points_at_zero: int = 0

    direction: str = rotation[0]
    distance: int = int(rotation[1:])

    if distance > 99:
        points_at_zero += distance // 100
        distance %= 100

    if direction == "R":
        new_position: int = position + distance
        if new_position > 99:
            points_at_zero += 1
            new_position -= 100
    else:
        new_position: int = position - distance
        if new_position == 0:
            points_at_zero += 1
        elif new_position < 0:
            if position > 0:
                points_at_zero += 1
            new_position += 100

    return (new_position, points_at_zero)


@output_answer("2025-Day01-Part1")
def solve_puzzle_1() -> int:
    rotations: Iterator[str] = iter(parse_input())

    position: int = 50
    points_at_zero: int = 0

    while rotation := next(rotations, None):
        direction: str = rotation[0]
        distance: int = int(rotation[1:])

        if distance > 99:
            distance %= 100

        if direction == "R":
            position += distance
            if position > 99:
                position -= 100
        else:
            position -= distance
            if position < 0:
                position += 100

        if position == 0:
            points_at_zero += 1

    return points_at_zero


@output_answer("22025-Day01-Part2")
def solve_puzzle_2() -> int:
    rotations: Iterator[str] = iter(parse_input())

    position: int = 50
    points_at_zero: int = 0

    while rotation := next(rotations, None):
        _position, _points_at_zero = get_new_position(position, rotation)
        position = _position
        points_at_zero += _points_at_zero

    return points_at_zero


if __name__ == "__main__":
    solve_puzzle_1()
    solve_puzzle_2()
