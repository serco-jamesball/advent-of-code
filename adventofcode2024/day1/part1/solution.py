import pandas
import utility
from pandas import (
    DataFrame,
    Series,
)
from pathlib import Path


def solve(input: DataFrame) -> int:
    left: Series = Series(input[0])
    right: Series = Series(input[1])

    sorted_left: Series = left.sort_values(ignore_index=True)
    sorted_right: Series = right.sort_values(ignore_index=True)

    sorted: DataFrame = pandas.concat([sorted_left, sorted_right], axis=1)

    sorted["distance"] = sorted.apply(lambda x: abs(x.loc[0] - x.loc[1]), axis=1)

    total_distance: int = sorted["distance"].sum()

    return total_distance


def main() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)

    input: DataFrame = utility.get_dataframe(input_file_path)

    answer: int = solve(input)

    print(utility.get_answer_message(file_path, answer))


if __name__ == "__main__":
    main()
