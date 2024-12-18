import year2024.utility as utility


Grid = list[str]
Coordinates = tuple[int, int]
Vector = tuple[int, int]
Match = list[tuple[Coordinates, str]]


DAY: str = "4"

WORD_SEARCH_FILE_PATH: str = r"year2024\day04\resource\input.txt"

WORD: str = "XMAS"

VECTORS: list[Vector] = [
    (0, 1),  # →
    (0, -1),  # ←
    (1, 0),  # ↓
    (-1, 0),  # ↑
    (1, 1),  # ↘
    (-1, -1),  # ↖
    (1, -1),  # ↙
    (-1, 1),  # ↗
]


def do_word_search(word_search: str) -> tuple[int, list[Match]]:
    grid: Grid = parse_word_search_to_grid(word_search)

    matches: list[Match] = find_occurrences_of_word(WORD, grid)

    return len(matches), matches


def parse_word_search_to_grid(word_search: str) -> Grid:
    return [line for line in word_search.split("\n")]


def find_occurrences_of_word(word: str, grid: Grid) -> list[Match]:
    matches: list[Match] = []

    if occurrences_of_first_letter := find_occurrences_of_letter(word[0], grid):
        for coordinates in occurrences_of_first_letter:
            for vector in VECTORS:
                if match := find_occurrence_of_word_along_vector(
                    coordinates, word, grid, vector
                ):
                    matches.append(match)

    return matches


def find_occurrence_of_word_along_vector(
    coordinates: Coordinates,
    word: list[str],
    grid: Grid,
    vector: Vector,
    match: Match | None = None,
) -> list[Match] | None:
    if not match:
        match = match or [(coordinates, word[0])]
        word = word[1:]

    if not word:
        return match

    if occurrences := find_occurrences_of_letter_along_vector(
        coordinates, word[0], grid, vector
    ):
        for occurrence in occurrences:
            match.append((occurrence, word[0]))
            return find_occurrence_of_word_along_vector(
                occurrence, word[1:], grid, vector, match
            )

    return None


def find_occurrences_of_letter(letter: str, grid: Grid) -> list[Coordinates]:
    return [
        (i, j)
        for i, row in enumerate(grid)
        for j, _letter in enumerate(row)
        if _letter == letter
    ]


def find_occurrences_of_letter_along_vector(
    coordinates: Coordinates, letter: str, grid: Grid, vector: Vector
) -> list[Coordinates]:
    row, col = coordinates
    row_offset, col_offset = vector

    row_tally, col_tally = len(grid), len(grid[0])

    surrounding_coordinates: list[Coordinates] = []

    next_row, next_col = row + row_offset, col + col_offset
    if (
        next_row > -1
        and next_row < row_tally
        and next_col > -1
        and next_col < col_tally
        and grid[next_row][next_col] == letter
    ):
        surrounding_coordinates.append((next_row, next_col))

    return surrounding_coordinates


if __name__ == "__main__":
    with open(WORD_SEARCH_FILE_PATH) as word_search_file:
        word_search: str = word_search_file.read().strip()

    part_1_answer, _ = do_word_search(word_search)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))
