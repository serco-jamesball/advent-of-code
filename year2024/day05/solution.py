from collections import defaultdict
import year2024.utility as utility


DAY: str = "5"

PAGE_ORDERING_RULES_FILE_PATH: str = r"year2024\day05\resource\page_ordering_rules.txt"
UPDATES_FILE_PATH: str = r"year2024\day05\resource\updates.txt"


def get_page_ordering_rules(page_ordering_rules_file_path: str) -> dict[int, set[int]]:
    with open(page_ordering_rules_file_path) as page_ordering_rules_file:
        page_ordering_rules: dict[int, set[int]] = defaultdict(set)

        for line in page_ordering_rules_file.read().strip().split("\n"):
            x, y = tuple(int(page) for page in line.split("|"))
            page_ordering_rules[y].add(x)

    return page_ordering_rules


def get_updates(updates_file_path: str) -> list[list[int]]:
    with open(updates_file_path) as updates_file:
        return [
            [int(page) for page in line.split(",")]
            for line in updates_file.read().strip().split("\n")
        ]


def is_update_page_order_correct(
    update: list[int], page_ordering_rules: dict[int, set[int]]
) -> bool:
    # Given value x
    # When a subsequent value y is found to have a rule that it must precede x
    # Then the page order of the update is not correct
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and y in page_ordering_rules[x]:
                return False
    return True


def get_updates_with_correct_page_order(
    updates: list[list[int]], page_ordering_rules: dict[int, set[int]]
) -> list[list[int]]:
    return [
        update
        for update in updates
        if is_update_page_order_correct(update, page_ordering_rules)
    ]


def sum_middle_numbers(updates: list[list[int]]) -> int:
    return sum(update[len(update) // 2] for update in updates)


def get_part_1_answer(
    page_ordering_rules: dict[int, set[int]], updates: list[int]
) -> int:
    updates_in_right_order: list[list[int]] = get_updates_with_correct_page_order(
        updates, page_ordering_rules
    )

    return sum_middle_numbers(updates_in_right_order)


if __name__ == "__main__":
    page_ordering_rules = get_page_ordering_rules(PAGE_ORDERING_RULES_FILE_PATH)
    updates: list[int] = get_updates(UPDATES_FILE_PATH)

    part_1_answer: int = get_part_1_answer(page_ordering_rules, updates)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))
