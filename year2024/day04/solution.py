import year2024.utility as utility
from enum import Enum


class VectorDirection(Enum):
    RIGHT_HORIZONTAL = 1
    LEFT_HORIZONTAL = 2
    DOWNWARD_VERTICAL = 3
    UPWARD_VERTICAL = 4
    RIGHT_DOWNWARD_DIAGONAL = 5
    RIGHT_UPWARD_DIAGONAL = 6
    LEFT_DOWNWARD_DIAGONAL = 7
    LEFT_UPWARD_DIAGONAL = 8


Grid = list[str]
Coordinates = tuple[int, int]
Offset = tuple[int, int]
Vector = tuple[Offset, VectorDirection]
Match = list[tuple[Coordinates, str]]


DAY: str = "4"

WORD_SEARCH_FILE_PATH: str = r"year2024\day04\resource\input.txt"

VECTORS: list[Vector] = [
    ((0, 1), VectorDirection.RIGHT_HORIZONTAL),  # →
    ((0, -1), VectorDirection.LEFT_HORIZONTAL),  # ←
    ((1, 0), VectorDirection.DOWNWARD_VERTICAL),  # ↓
    ((-1, 0), VectorDirection.UPWARD_VERTICAL),  # ↑
    ((1, 1), VectorDirection.RIGHT_DOWNWARD_DIAGONAL),  # ↘
    ((-1, 1), VectorDirection.RIGHT_UPWARD_DIAGONAL),  # ↗
    ((-1, -1), VectorDirection.LEFT_UPWARD_DIAGONAL),  # ↖
    ((1, -1), VectorDirection.LEFT_DOWNWARD_DIAGONAL),  # ↙
]


def parse_word_search_to_grid(word_search: str) -> Grid:
    return [line for line in word_search.split("\n")]


def find_occurrences_of_x_mas(grid: Grid) -> list[Match]:
    word: str = "MAS"

    matches: list[Match] = []

    # Find matches along each diagonal:
    # M.. | S.. | ..M | ..S
    # .A. | .A. | .A. | .A.
    # ..S | ..M | S.. | M..
    diagonals: list[Offset] = [
        offset
        for offset, direction in VECTORS
        if direction
        in {
            VectorDirection.RIGHT_DOWNWARD_DIAGONAL,
            VectorDirection.RIGHT_UPWARD_DIAGONAL,
            VectorDirection.LEFT_UPWARD_DIAGONAL,
            VectorDirection.LEFT_DOWNWARD_DIAGONAL,
        }
    ]

    diagonal_matches: list[Match] = []

    for coordinates in find_occurrences_of_letter(word[0], grid):
        for offset in diagonals:
            if match := find_occurrence_of_word_along_vector(
                coordinates, word, grid, offset
            ):
                diagonal_matches.append(match)

    # Find pairs of mathes with "A"s that overlap and combine them
    for match in diagonal_matches[:]:
        other_matches: list[Match] = [
            other_match for other_match in diagonal_matches if other_match != match
        ]

        for other_match in other_matches:
            if match[1] == other_match[1]:
                matches.append(sorted(list(set(match + other_match))))

                del diagonal_matches[diagonal_matches.index(match)]

    return matches


def find_occurrences_of_xmas(grid: Grid) -> list[Match]:
    word: str = "XMAS"

    matches: list[Match] = []

    for coordinates in find_occurrences_of_letter(word[0], grid):
        for offset, _ in VECTORS:
            if match := find_occurrence_of_word_along_vector(
                coordinates, word, grid, offset
            ):
                matches.append(match)

    return matches


def find_occurrence_of_word_along_vector(
    coordinates: Coordinates,
    word: list[str],
    grid: Grid,
    offset: Offset,
    match: Match | None = None,
) -> list[Match] | None:
    if not match:
        match = [(coordinates, word[0])]
        word = word[1:]

    if not word:
        return match

    if occurrence := find_occurrence_of_letter_along_vector(
        coordinates, word[0], grid, offset
    ):
        match.append((occurrence, word[0]))
        return find_occurrence_of_word_along_vector(
            occurrence, word[1:], grid, offset, match
        )

    return None


def find_occurrences_of_letter(letter: str, grid: Grid) -> list[Coordinates]:
    return [
        (i, j)
        for i, row in enumerate(grid)
        for j, _letter in enumerate(row)
        if _letter == letter
    ]


def find_occurrence_of_letter_along_vector(
    coordinates: Coordinates, letter: str, grid: Grid, offset: Offset
) -> Coordinates | None:
    row, col = coordinates
    row_offset, col_offset = offset

    row_tally, col_tally = len(grid), len(grid[0])

    next_row, next_col = row + row_offset, col + col_offset
    if (
        next_row > -1
        and next_row < row_tally
        and next_col > -1
        and next_col < col_tally
        and grid[next_row][next_col] == letter
    ):
        return next_row, next_col


def main() -> None:
    with open(WORD_SEARCH_FILE_PATH) as word_search_file:
        word_search: str = word_search_file.read().strip()

    grid: Grid = parse_word_search_to_grid(word_search)

    part_1_answer: int = len(find_occurrences_of_xmas(grid))
    part_2_answer: int = len(find_occurrences_of_x_mas(grid))

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
