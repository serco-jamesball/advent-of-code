import pytest
import year2024.day04.solution as solution
from year2024.day04.solution import Coordinates, Grid, Match, Offset


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
    "coordinates, grid, expected",
    [
        # Positive cases
        ((0, 0), ["XXX", "XXX", "XXX"], [(0, 1), (1, 0), (1, 1)]),
        ((0, 1), ["XXX", "XXX", "XXX"], [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]),
        ((0, 2), ["XXX", "XXX", "XXX"], [(0, 1), (1, 1), (1, 2)]),
        ((1, 0), ["XXX", "XXX", "XXX"], [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]),
        (
            (1, 1),
            ["XXX", "XXX", "XXX"],
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
        ),
        ((1, 2), ["XXX", "XXX", "XXX"], [(0, 1), (0, 2), (1, 1), (2, 1), (2, 2)]),
        ((2, 0), ["XXX", "XXX", "XXX"], [(1, 0), (1, 1), (2, 1)]),
        ((2, 1), ["XXX", "XXX", "XXX"], [(1, 0), (1, 1), (1, 2), (2, 0), (2, 2)]),
        ((2, 2), ["XXX", "XXX", "XXX"], [(1, 1), (1, 2), (2, 1)]),
        # Negative cases
        ((1, 1), ["OOX", "OXX", "XXX"], [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]),
    ],
)
def test_find_occurrence_of_letter_along_vector(
    coordinates: Coordinates, grid: Grid, expected: list[Coordinates]
) -> None:
    letter: str = "X"
    actual: list[Coordinates] = []

    for offset, _ in solution.VECTORS:
        if result := solution.find_occurrence_of_letter_along_vector(
            coordinates, letter, grid, offset
        ):
            actual.append(result)

    assert sorted(actual) == sorted(expected)


@pytest.mark.parametrize(
    "coordinates, offset, expected",
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
    coordinates: Coordinates, offset: Offset, expected: Match
) -> None:
    assert (
        solution.find_occurrence_of_word_along_vector(
            coordinates, "XMAS", WORD_SEARCH_GRID, offset
        )
        == expected
    )


def test_find_occurrences_of_xmas() -> None:
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

    actual: list[Match] = solution.find_occurrences_of_xmas(WORD_SEARCH_GRID)

    assert sorted(actual) == sorted(expected)


def test_find_occurrences_of_x_mas() -> None:
    #   0123456789
    # 0 .M.S......
    # 1 ..A..MSMS.
    # 2 .M.S.MAA..
    # 3 ..A.ASMSM.
    # 4 .M.S.M....
    # 5 ..........
    # 6 S.S.S.S.S.
    # 7 .A.A.A.A..
    # 8 M.M.M.M.M.
    # 9 ..........
    expected: list[Match] = [
        [((0, 1), "M"), ((0, 3), "S"), ((1, 2), "A"), ((2, 1), "M"), ((2, 3), "S")],
        [((1, 5), "M"), ((1, 7), "M"), ((2, 6), "A"), ((3, 5), "S"), ((3, 7), "S")],
        [((1, 6), "S"), ((1, 8), "S"), ((2, 7), "A"), ((3, 6), "M"), ((3, 8), "M")],
        [((2, 1), "M"), ((2, 3), "S"), ((3, 2), "A"), ((4, 1), "M"), ((4, 3), "S")],
        [((2, 3), "S"), ((2, 5), "M"), ((3, 4), "A"), ((4, 3), "S"), ((4, 5), "M")],
        [((6, 0), "S"), ((6, 2), "S"), ((7, 1), "A"), ((8, 0), "M"), ((8, 2), "M")],
        [((6, 2), "S"), ((6, 4), "S"), ((7, 3), "A"), ((8, 2), "M"), ((8, 4), "M")],
        [((6, 4), "S"), ((6, 6), "S"), ((7, 5), "A"), ((8, 4), "M"), ((8, 6), "M")],
        [((6, 6), "S"), ((6, 8), "S"), ((7, 7), "A"), ((8, 6), "M"), ((8, 8), "M")],
    ]

    actual: list[Match] = solution.find_occurrences_of_x_mas(WORD_SEARCH_GRID)

    assert sorted(actual) == sorted(expected)
