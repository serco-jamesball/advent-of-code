from collections import defaultdict
import pytest
import year2024.day05.solution as solution


UPDATES_FILE_PATH: str = r"year2024\day05\test\resource\updates.txt"
PAGE_ORDERING_RULES_FILE_PATH: str = (
    r"year2024\day05\test\resource\page_ordering_rules.txt"
)

PAGE_ORDERING_RULES: defaultdict[int, set[int]] = defaultdict(set)
PAGE_ORDERING_RULES[13] = {97, 75, 47, 61, 53, 29}
PAGE_ORDERING_RULES[29] = {97, 75, 47, 61, 53}
PAGE_ORDERING_RULES[53] = {97, 75, 47, 61}
PAGE_ORDERING_RULES[61] = {97, 75, 47}
PAGE_ORDERING_RULES[47] = {97, 75}
PAGE_ORDERING_RULES[75] = {97}

UPDATES: list[list[int]] = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

CORRECTLY_ORDERED_UPDATES: list[list[int]] = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
]

CORRECTED_UPDATES: list[list[int]] = [
    [97, 75, 47, 61, 53],
    [61, 29, 13],
    [97, 75, 47, 29, 13],
]

PART_1_ANSWER: int = 143
PART_2_ANSWER: int = 123


def test_get_page_ordering_rules() -> None:
    assert (
        solution.get_page_ordering_rules(PAGE_ORDERING_RULES_FILE_PATH)
        == PAGE_ORDERING_RULES
    )


def test_get_updates() -> None:
    assert solution.get_updates(UPDATES_FILE_PATH) == UPDATES


@pytest.mark.parametrize(
    "update, expected",
    [
        ([75, 47, 61, 53, 29], True),
        ([97, 61, 53, 29, 13], True),
        ([75, 29, 13], True),
        ([75, 97, 47, 61, 53], False),
        ([61, 13, 29], False),
        ([97, 13, 75, 29, 47], False),
    ],
)
def test_is_ordered_correctly(update: list[int], expected: bool) -> None:
    assert solution.is_ordered_correctly(update, PAGE_ORDERING_RULES) == expected


@pytest.mark.parametrize(
    "updates, expected",
    [
        (CORRECTLY_ORDERED_UPDATES, PART_1_ANSWER),
        (CORRECTED_UPDATES, PART_2_ANSWER),
    ],
)
def test_sum_middle_pages(updates: list[list[int]], expected: int) -> None:
    assert solution.sum_middle_pages(updates) == expected
