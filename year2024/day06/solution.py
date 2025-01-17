import year2024.utility as utility


Map = list[str]
Position = tuple[int, int]
Positions = set[Position]
Direction = int
Step = tuple[Position, Direction]
Steps = set[Step]


DAY: str = "6"

MAP_FILE_PATH: str = r"year2024\day06\resource\map.txt"

GUARD: str = "^"
OBSTACLE: str = "#"

# 0 = up, 1 = right, 2 = down, 3 = left
DIRECTIONS: tuple[Position, ...] = ((-1, 0), (0, 1), (1, 0), (0, -1))


def get_map(map_file_path: str) -> list[str]:
    with open(map_file_path) as map_file:
        return map_file.read().split("\n")


def parse_map(map: Map) -> tuple[Position, Positions]:
    rows, cols = len(map), len(map[0])

    obstacles: Positions = set()

    for row in range(rows):
        for col in range(cols):
            if map[row][col] == GUARD:
                guard: int = (row, col)
            if map[row][col] == OBSTACLE:
                obstacles.add((row, col))

    return guard, frozenset(obstacles)


def patrol(map: Map, guard: Position, obstacles: Positions) -> Steps:
    steps: Steps = set()

    rows, cols = len(map), len(map[0])

    direction: Direction = 0
    row, col = guard

    while -1 < row < rows and -1 < col < cols:
        steps.add(((row, col), direction))

        row_offset, col_offset = DIRECTIONS[direction]
        next_row: int = row + row_offset
        next_col: int = col + col_offset

        if (next_row, next_col) in obstacles:
            direction = (direction + 1) % 4
        else:
            row, col = next_row, next_col

    return frozenset(steps)


def is_looping(map: Map, guard: Position, obstacles: Positions) -> bool:
    steps: Steps = set()

    rows, cols = len(map), len(map[0])

    direction: Direction = 0
    row, col = guard

    while -1 < row < rows and -1 < col < cols:
        if ((row, col), direction) in steps:
            return True

        steps.add(((row, col), direction))

        row_offset, col_offset = DIRECTIONS[direction]
        next_row: int = row + row_offset
        next_col: int = col + col_offset

        if (next_row, next_col) in obstacles:
            direction = (direction + 1) % 4
        else:
            row, col = next_row, next_col

    return False


def get_part_1_answer(steps: Steps) -> int:
    return len(frozenset(position for position, _ in steps))


def get_part_2_answer(
    map: Map,
    guard: Position,
    obstacles: Positions,
    steps: Steps,
) -> int:
    return sum(
        is_looping(map, guard, obstacles | frozenset({step}))
        for step in frozenset(position for position, _ in steps) - frozenset({guard})
    )


if __name__ == "__main__":
    map: Map = get_map(MAP_FILE_PATH)

    guard, obstacles = parse_map(map)

    steps = patrol(map, guard, obstacles)

    part_1_answer: int = get_part_1_answer(steps)
    part_2_answer: int = get_part_2_answer(map, guard, obstacles, steps)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))
