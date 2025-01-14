import year2024.utility as utility


DAY: str = "6"

MAP_FILE_PATH: str = r"year2024\day06\resource\map.txt"

GUARD: str = "^"
OBSTACLE: str = "#"

# 0 = up, 1 = right, 2 = down, 3 = left
DIRECTIONS: tuple[tuple[int, int], ...] = ((-1, 0), (0, 1), (1, 0), (0, -1))


def get_map(map_file_path: str) -> list[str]:
    with open(map_file_path) as map_file:
        return map_file.read().split("\n")


def find_guard(map: list[str]) -> tuple[int, int]:
    rows, cols = len(map), len(map[0])

    for row in range(rows):
        for col in range(cols):
            if map[row][col] == GUARD:
                return (row, col)


def find_obstacles(map: list[str]) -> frozenset[tuple[int, int]]:
    rows, cols = len(map), len(map[0])

    return frozenset(
        (row, col)
        for row in range(rows)
        for col in range(cols)
        if map[row][col] == OBSTACLE
    )


def patrol(
    map: list[str], guard: tuple[int, int], obstacles: set[tuple[int, int]]
) -> set[tuple[tuple[int, int], int]]:
    visited: set[tuple[tuple[int, int], int]] = set()

    rows, cols = len(map), len(map[0])

    direction: int = 0
    row, col = guard

    while True:
        if -1 < row < rows and -1 < col < cols:
            visited.add(((row, col), direction))

            row_offset, col_offset = DIRECTIONS[direction]

            next_row = row + row_offset
            next_col = col + col_offset

            if (next_row, next_col) in obstacles:
                direction = (direction + 1) % 4
            else:
                row, col = next_row, next_col
        else:
            return visited


def get_part_1_answer(visited: set[tuple[tuple[int, int], int]]) -> int:
    return len({position for position, _ in visited})


def get_part_2_answer() -> int:
    # Find intersections where directions are at a right angle to one another
    pass


if __name__ == "__main__":
    map: list[str] = get_map(MAP_FILE_PATH)

    start: tuple[int, int] = find_guard(map)
    obstacles: set[tuple[int, int]] = find_obstacles(map)

    visited: set[tuple[tuple[int, int], int]] = patrol(map, start, obstacles)

    part_1_answer: int = get_part_1_answer(visited)
    part_2_answer: int = get_part_1_answer()

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))
