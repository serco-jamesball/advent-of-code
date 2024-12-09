import pandas
import utility
from pandas import (
    DataFrame,
    Series,
)
from pathlib import Path


def solve(input: DataFrame) -> int:
    y_counts: Series = input.loc[:, ["y"]].value_counts()


def main() -> None:
    input_file_path: Path = utility.get_input_file_path(__file__)

    answer: int = solve(pandas.read_csv(input_file_path))

    day, part = utility.parse_file_name(__file__)
    message: str = utility.get_answer_message(day, part, answer)

    print(message)


if __name__ == "__main__":
    main()
