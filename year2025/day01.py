from collections.abc import Iterator
from importlib.resources import files

from year2025.utils import output_answer

RESOURCE_ANCHOR: str = "year2025.resources"

INPUT: str = files(RESOURCE_ANCHOR).joinpath("day01.txt").read_text()

START_POSITION: int = 50


def parse_input() -> list[str]:
    return INPUT.strip().split("\n")


def get_new_position(
    start: int, rotation: str, any_click: bool = False
) -> tuple[int, int]:
    points_at_0: int = 0

    direction: str = rotation[0]
    distance: int = int(rotation[1:])

    # count any click that causes the dial to point at 0 during a full rotation
    if distance > 99:
        if any_click:
            points_at_0 += distance // 100
        distance_excl_full_rotations: int = distance % 100
    else:
        distance_excl_full_rotations: int = distance

    if direction == "R":
        if (i := start + distance_excl_full_rotations) > 99:
            end: int = i - 100
        else:
            end: int = i

        # count click that causes the dial to point at 0 during a partial
        # rotation not starting at 0
        if start != 0 and 0 < end < start and any_click:
            points_at_0 += 1
    else:
        if (i := start - distance_excl_full_rotations) < 0:
            end: int = i + 100
        else:
            end: int = i

        # count click that causes the dial to point at 0 during a partial
        # rotation not starting at 0
        if start != 0 and 0 < end > start and any_click:
            points_at_0 += 1

    # count click that causes the fial to point at 0 at the end of a rotation
    if end == 0:
        points_at_0 += 1

    return (end, points_at_0)


@output_answer("2025-Day01-Part1")
def solve_puzzle_1() -> int:
    rotations: Iterator[str] = iter(parse_input())

    position: int = START_POSITION
    zero_clicks: int = 0

    while rotation := next(rotations, None):
        _position, _zero_clicks = get_new_position(position, rotation)
        position = _position
        zero_clicks += _zero_clicks

    return zero_clicks


@output_answer("22025-Day01-Part2")
def solve_puzzle_2() -> int:
    rotations: Iterator[str] = iter(parse_input())

    position: int = START_POSITION
    total_points_at_zero: int = 0

    while rotation := next(rotations, None):
        end, points_at_0 = get_new_position(position, rotation, any_click=True)
        position = end
        total_points_at_zero += points_at_0

    return total_points_at_zero


if __name__ == "__main__":
    solve_puzzle_1()
    solve_puzzle_2()
