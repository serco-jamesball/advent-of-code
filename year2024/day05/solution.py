from collections import defaultdict
import year2024.utility as utility


DAY: str = "5"

UPDATES_FILE_PATH: str = r"year2024\day05\resource\updates.txt"
PAGE_ORDERING_RULES_FILE_PATH: str = r"year2024\day05\resource\page_ordering_rules.txt"


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


def identify_correctly_ordered_updates(
    updates: list[list[int]], page_ordering_rules: dict[int, set[int]]
) -> tuple[list[list[int], tuple[list[int, int]]]]:
    correctly_ordered_updates: list[list[int]] = []
    incorrectly_ordered_updates: list[list[int]] = []

    for update in updates:
        if is_ordered_correctly(update, page_ordering_rules):
            correctly_ordered_updates.append(update)
        else:
            incorrectly_ordered_updates.append(update)

    return correctly_ordered_updates, incorrectly_ordered_updates


def is_ordered_correctly(
    update: list[int], page_ordering_rules: dict[int, set[int]]
) -> bool:
    # Given value x
    # When subsequent value y has a rule that it must precede x
    # Then the page order of the update is not correct
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and y in page_ordering_rules[x]:
                return False
    return True


def fix_incorrectly_ordered_updates(
    updates: list[list[int]], page_ordering_rules: dict[int, set[int]]
) -> list[list[int]]:
    return [correct_order(update, page_ordering_rules) for update in updates]


def correct_order(
    update: list[int], page_ordering_rules: dict[int, set[int]]
) -> list[int]:
    return [
        page
        for page, _ in sorted(
            ((page, len(page_ordering_rules[page] & set(update))) for page in update),
            key=lambda order: order[1],
        )
    ]


def sum_middle_pages(updates: list[int]) -> int:
    return sum(update[len(update) // 2] for update in updates)


if __name__ == "__main__":
    updates: list[int] = get_updates(UPDATES_FILE_PATH)
    page_ordering_rules: dict[int, set[int]] = get_page_ordering_rules(
        PAGE_ORDERING_RULES_FILE_PATH
    )

    correctly_ordered_updates, incorrectly_ordered_updates = (
        identify_correctly_ordered_updates(updates, page_ordering_rules)
    )

    corrected_updates: list[list[int]] = fix_incorrectly_ordered_updates(
        updates, page_ordering_rules
    )

    part_1_answer: int = sum_middle_pages(correctly_ordered_updates)
    part_2_answer: int = sum_middle_pages(corrected_updates)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))
