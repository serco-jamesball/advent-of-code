import pandas
import utility
from pandas import (
    DataFrame,
    Series,
)
from pathlib import Path


def solve(input: DataFrame) -> int:
    x: Series = Series(input["x"])
    y: Series = Series(input["y"])

    sorted_x: Series = x.sort_values(ignore_index=True)
    sorted_y: Series = y.sort_values(ignore_index=True)

    sorted: DataFrame = pandas.concat([sorted_x, sorted_y], axis=1)

    sorted["distance"] = sorted.apply(lambda x: abs(x.loc["x"] - x.loc["y"]), axis=1)

    total_distance: int = sorted["distance"].sum()

    return total_distance


def main() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)

    answer: int = solve(pandas.read_csv(input_file_path))

    day, part = utility.parse_file_name(file_path)
    message: str = utility.get_answer_message(day, part, answer)

    print(message)


if __name__ == "__main__":
    main()
