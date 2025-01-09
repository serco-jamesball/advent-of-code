from collections import defaultdict
import pytest
import year2024.day05.solution as solution


PAGE_ORDERING_RULES_FILE_PATH: str = (
    r"year2024\day05\test\resource\page_ordering_rules.txt"
)
UPDATES_FILE_PATH: str = r"year2024\day05\test\resource\updates.txt"

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

UPDATES_IN_RIGHT_ORDER: list[list[int]] = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
]

PART_1_ANSWER: int = 143


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
def test_is_update_page_order_correct(update: list[int], expected: bool) -> None:
    assert (
        solution.is_update_page_order_correct(update, PAGE_ORDERING_RULES) == expected
    )


def test_get_updates_with_correct_page_order() -> None:
    assert sorted(
        solution.get_updates_with_correct_page_order(UPDATES, PAGE_ORDERING_RULES)
    ) == sorted(UPDATES_IN_RIGHT_ORDER)


def test_sum_middle_numbers() -> None:
    assert solution.sum_middle_numbers(UPDATES_IN_RIGHT_ORDER) == PART_1_ANSWER


def test_get_part_1_answer() -> None:
    page_ordering_rules: dict[int, set[int]] = solution.get_page_ordering_rules(
        PAGE_ORDERING_RULES_FILE_PATH
    )
    updates: list[int] = solution.get_updates(UPDATES_FILE_PATH)

    assert solution.get_part_1_answer(page_ordering_rules, updates) == PART_1_ANSWER
