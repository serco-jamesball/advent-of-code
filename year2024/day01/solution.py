import pandas
import year2024.utility as utility
from pandas import (
    DataFrame,
    Series,
)


DAY: str = "1"


def get_part_1_answer(input: DataFrame) -> int:
    left: Series = Series(input[0])
    right: Series = Series(input[1])

    sorted_left: Series = left.sort_values(ignore_index=True)
    sorted_right: Series = right.sort_values(ignore_index=True)

    sorted: DataFrame = pandas.concat([sorted_left, sorted_right], axis=1)

    sorted["distance"] = sorted.apply(lambda x: abs(x.loc[0] - x.loc[1]), axis=1)

    total_distance: int = sorted["distance"].sum()

    return total_distance


def get_part_2_answer(input: DataFrame) -> int:
    input["occurrences"] = [len(input[input[1] == value]) for value in input[0]]

    input["similarity"] = input["occurrences"] * input[0]

    similarity_score: int = input["similarity"].sum()

    return similarity_score


def main() -> None:
    input: DataFrame = utility.get_input(utility.get_input_file_path(__file__))

    part_1_answer: int = get_part_1_answer(input)
    part_2_answer: int = get_part_2_answer(input)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
