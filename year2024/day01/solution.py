import pandas
import year2024.utility as utility
from pandas import (
    DataFrame,
    Series,
)


pandas.options.mode.copy_on_write = True


DAY: str = "1"

LOCATION_LISTS_FILE_PATH: str = r"year2024\day01\resource\input.csv"


def find_total_distance_between_lists(lists: DataFrame) -> int:
    left_list: Series = Series(lists[0])
    right_list: Series = Series(lists[1])

    sorted_left_list: Series = left_list.sort_values(ignore_index=True)
    sorted_right_list: Series = right_list.sort_values(ignore_index=True)

    sorted_lists: DataFrame = pandas.concat(
        [sorted_left_list, sorted_right_list], axis=1
    )

    sorted_lists["distance"] = sorted_lists.apply(
        lambda x: abs(x.loc[0] - x.loc[1]), axis=1
    )

    total_distance: int = sorted_lists["distance"].sum()

    return total_distance


def find_similarity_score(lists: DataFrame) -> int:
    lists["occurrences"] = [len(lists[lists[1] == value]) for value in lists[0]]

    lists["similarity"] = lists["occurrences"] * lists[0]

    similarity_score: int = lists["similarity"].sum()

    return similarity_score


def main() -> None:
    location_lists: DataFrame = pandas.read_csv(
        LOCATION_LISTS_FILE_PATH,
        names=utility.get_column_labels(LOCATION_LISTS_FILE_PATH),
    )

    part_1_answer: int = find_total_distance_between_lists(location_lists)
    part_2_answer: int = find_similarity_score(location_lists)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
