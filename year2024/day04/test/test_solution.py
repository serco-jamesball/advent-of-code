import pytest
import year2024.day04.solution as solution
from year2024.day04.solution import Coordinates, Grid, Match, Vector, WORD


WORD_SEARCH_FILE_PATH: str = r"year2024\day04\test\resource\input.txt"

WORD_SEARCH_GRID: Grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

LETTER_X_COORDINATES: list[Coordinates] = [
    (0, 4),
    (0, 5),
    (1, 4),
    (2, 2),
    (2, 4),
    (3, 9),
    (4, 0),
    (4, 6),
    (5, 0),
    (5, 1),
    (5, 5),
    (5, 6),
    (6, 7),
    (7, 2),
    (8, 5),
    (9, 1),
    (9, 3),
    (9, 5),
    (9, 9),
]


def test_parse_word_search_to_grid() -> None:
    with open(WORD_SEARCH_FILE_PATH) as word_search_file:
        word_search: str = word_search_file.read().strip()

    assert solution.parse_word_search_to_grid(word_search) == WORD_SEARCH_GRID


def test_find_occurrences_of_letter() -> None:
    assert (
        solution.find_occurrences_of_letter("X", WORD_SEARCH_GRID)
        == LETTER_X_COORDINATES
    )


@pytest.mark.parametrize(
    "coordinates, letter, grid, expected",
    [
        # All letters are "X":
        #   0 1 2
        # 0 X X X
        # 1 X X X
        # 2 X X X
        # Top left:
        # X →
        # ↓ ↘
        ((0, 0), "X", ["XXX", "XXX", "XXX"], [(0, 1), (1, 1), (1, 0)]),
        # Middle left:
        # ↑ ↗
        # X →
        # ↓ ↘
        ((1, 0), "X", ["XXX", "XXX", "XXX"], [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]),
        # Bottom left:
        # ↑ ↗
        # X →
        ((2, 0), "X", ["XXX", "XXX", "XXX"], [(1, 0), (1, 1), (2, 1)]),
        # Top middle:
        # ← X →
        # ↙ ↓ ↘
        ((0, 1), "X", ["XXX", "XXX", "XXX"], [(0, 0), (1, 0), (0, 2), (1, 2), (1, 1)]),
        # Middle:
        # ↖ ↑ ↗
        # ← X →
        # ↙ ↓ ↘
        (
            (1, 1),
            "X",
            ["XXX", "XXX", "XXX"],
            [(0, 1), (2, 1), (0, 0), (1, 0), (2, 0), (0, 2), (1, 2), (2, 2)],
        ),
        # Bottom middle:
        # ↖ ↑ ↗
        # ← X →
        (
            (2, 1),
            "X",
            ["XXX", "XXX", "XXX"],
            [(1, 1), (1, 0), (2, 0), (1, 2), (2, 2)],
        ),
        # Top right:
        # ← X
        # ↙ ↓
        ((0, 2), "X", ["XXX", "XXX", "XXX"], [(0, 1), (1, 1), (1, 2)]),
        # Middle right:
        # ↖ ↑
        # ← X
        # ↙ ↓
        (
            (1, 2),
            "X",
            ["XXX", "XXX", "XXX"],
            [(0, 2), (2, 2), (0, 1), (1, 1), (2, 1)],
        ),
        # Bottom right:
        # ↖ ↑
        # ← X
        ((2, 2), "X", ["XXX", "XXX", "XXX"], [(1, 2), (1, 1), (2, 1)]),
        # Letters are "X" or "O":
        #   0 1 2
        # 0 X O X
        # 1 O X O
        # 2 X O X
        # Top left:
        # X
        #   ↘
        ((0, 0), "X", ["XOX", "OXO", "XOX"], [(1, 1)]),
        # Middle left:
        # ↑
        # X →
        # ↓
        ((1, 0), "X", ["XOX", "OXO", "XOX"], [(0, 0), (1, 1), (2, 0)]),
        # Bottom left:
        #   ↗
        # X
        ((2, 0), "X", ["XOX", "OXO", "XOX"], [(1, 1)]),
        # Top middle:
        # ← X →
        #   ↓
        ((0, 1), "X", ["XOX", "OXO", "XOX"], [(0, 0), (0, 2), (1, 1)]),
        # Middle:
        # ↖   ↗
        #   X
        # ↙   ↘
        ((1, 1), "X", ["XOX", "OXO", "XOX"], [(0, 0), (0, 2), (2, 0), (2, 2)]),
        # Bottom middle:
        #   ↑
        # ← X →
        (
            (2, 1),
            "X",
            ["XOX", "OXO", "XOX"],
            [(1, 1), (2, 0), (2, 2)],
        ),
        # Top right:
        #   X
        # ↙
        ((0, 2), "X", ["XOX", "OXO", "XOX"], [(1, 1)]),
        # Middle right:
        #   ↑
        # ← X
        #   ↓
        (
            (1, 2),
            "X",
            ["XOX", "OXO", "XOX"],
            [(0, 2), (1, 1), (2, 2)],
        ),
        # Bottom right:
        # ↖
        #   X
        ((2, 2), "X", ["XOX", "OXO", "XOX"], [(1, 1)]),
    ],
)
def test_find_occurrences_of_letter_along_vector(
    coordinates: Coordinates, letter: str, grid: Grid, expected: list[Coordinates]
) -> None:
    actual: list[Coordinates] = solution.find_occurrences_of_letter_along_vector(
        coordinates, letter, grid
    )

    assert sorted(actual) == sorted(expected)


@pytest.mark.parametrize(
    "coordinates, vector, expected",
    # Expected results:
    #   0123456789
    # 0 ....XXMAS.
    # 1 .SAMXMS...
    # 2 ...S..A...
    # 3 ..A.A.MS.X
    # 4 XMASAMX.MM
    # 5 X.....XA.A
    # 6 S.S.S.S.SS
    # 7 .A.A.A.A.A
    # 8 ..M.M.M.MM
    # 9 .X.X.XMASX
    [
        # ↘
        ((0, 4), (1, 1), [((0, 4), "X"), ((1, 5), "M"), ((2, 6), "A"), ((3, 7), "S")]),
        # →
        ((0, 5), (0, 1), [((0, 5), "X"), ((0, 6), "M"), ((0, 7), "A"), ((0, 8), "S")]),
        # ←
        ((1, 4), (0, -1), [((1, 4), "X"), ((1, 3), "M"), ((1, 2), "A"), ((1, 1), "S")]),
        # ↓
        ((3, 9), (1, 0), [((3, 9), "X"), ((4, 9), "M"), ((5, 9), "A"), ((6, 9), "S")]),
        # ↙
        ((3, 9), (1, -1), [((3, 9), "X"), ((4, 8), "M"), ((5, 7), "A"), ((6, 6), "S")]),
        # ↑
        ((4, 6), (-1, 0), [((4, 6), "X"), ((3, 6), "M"), ((2, 6), "A"), ((1, 6), "S")]),
        # ↗
        ((5, 0), (-1, 1), [((5, 0), "X"), ((4, 1), "M"), ((3, 2), "A"), ((2, 3), "S")]),
        # ↖
        (
            (5, 6),
            (-1, -1),
            [((5, 6), "X"), ((4, 5), "M"), ((3, 4), "A"), ((2, 3), "S")],
        ),
    ],
)
def test_find_occurrence_of_word_along_vector(
    coordinates: Coordinates, vector: Vector, expected: Match
) -> None:
    assert (
        solution.find_occurrence_of_word_along_vector(
            coordinates, solution.WORD, WORD_SEARCH_GRID, vector
        )
        == expected
    )


def test_find_occurrences_of_word() -> None:
    expected: list[Match] = [
        [((0, 4), "X"), ((1, 5), "M"), ((2, 6), "A"), ((3, 7), "S")],
        [((0, 5), "X"), ((0, 6), "M"), ((0, 7), "A"), ((0, 8), "S")],
        [((1, 4), "X"), ((1, 3), "M"), ((1, 2), "A"), ((1, 1), "S")],
        [((3, 9), "X"), ((4, 9), "M"), ((5, 9), "A"), ((6, 9), "S")],
        [((3, 9), "X"), ((4, 8), "M"), ((5, 7), "A"), ((6, 6), "S")],
        [((4, 0), "X"), ((4, 1), "M"), ((4, 2), "A"), ((4, 3), "S")],
        [((4, 6), "X"), ((4, 5), "M"), ((4, 4), "A"), ((4, 3), "S")],
        [((4, 6), "X"), ((3, 6), "M"), ((2, 6), "A"), ((1, 6), "S")],
        [((5, 0), "X"), ((4, 1), "M"), ((3, 2), "A"), ((2, 3), "S")],
        [((5, 6), "X"), ((4, 5), "M"), ((3, 4), "A"), ((2, 3), "S")],
        [((9, 1), "X"), ((8, 2), "M"), ((7, 3), "A"), ((6, 4), "S")],
        [((9, 3), "X"), ((8, 2), "M"), ((7, 1), "A"), ((6, 0), "S")],
        [((9, 3), "X"), ((8, 4), "M"), ((7, 5), "A"), ((6, 6), "S")],
        [((9, 5), "X"), ((8, 4), "M"), ((7, 3), "A"), ((6, 2), "S")],
        [((9, 5), "X"), ((8, 6), "M"), ((7, 7), "A"), ((6, 8), "S")],
        [((9, 5), "X"), ((9, 6), "M"), ((9, 7), "A"), ((9, 8), "S")],
        [((9, 9), "X"), ((8, 8), "M"), ((7, 7), "A"), ((6, 6), "S")],
        [((9, 9), "X"), ((8, 9), "M"), ((7, 9), "A"), ((6, 9), "S")],
    ]

    actual: list[Match] = solution.find_occurrences_of_word(
        solution.WORD, WORD_SEARCH_GRID
    )

    assert sorted(actual) == sorted(expected)
