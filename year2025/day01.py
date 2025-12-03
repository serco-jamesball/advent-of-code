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
    direction: str = rotation[0]
    distance: int = int(rotation[1:])

    # count any click that causes the dial to point at 0 during a full rotation
    points_at_0: int = (distance // 100) if any_click else 0
    distance %= 100

    end: int = (start + distance if direction == "R" else start - distance) % 100

    # count click that causes the dial to point at 0 during a partial
    # rotation not starting at 0
    if any_click and start != 0 and end != 0:
        if direction == "R" and start + distance > 99:
            points_at_0 += 1
        elif start - distance < 0:
            points_at_0 += 1

    # count click that causes the final to point at 0 at the end of a rotation
    if end == 0:
        points_at_0 += 1

    return (end, points_at_0)


def solve(any_click: bool = False) -> int:
    position: int = START_POSITION
    total_points_at_0: int = 0

    for rotation in parse_input():
        end, points_at_0 = get_new_position(position, rotation, any_click=any_click)
        position = end
        total_points_at_0 += points_at_0

    return total_points_at_0


@output_answer("2025-Day01-Part1")
def solve_puzzle_1() -> int:
    return solve()


@output_answer("22025-Day01-Part2")
def solve_puzzle_2() -> int:
    return solve(any_click=True)


if __name__ == "__main__":
    solve_puzzle_1()
    solve_puzzle_2()
