from pandas import (
    DataFrame,
    Series,
)
from pathlib import Path

import pandas


INPUT_FILE_PATH: Path = Path(__file__).parent.joinpath("input.csv")


def solve(input: DataFrame) -> int:
    x: Series = Series(input["x"])
    y: Series = Series(input["y"])

    sorted_x: Series = x.sort_values(ignore_index=True)
    sorted_y: Series = y.sort_values(ignore_index=True)

    sorted: DataFrame = pandas.concat([sorted_x, sorted_y], axis=1)

    sorted["distance"] = sorted.apply(lambda x: abs(x.loc["x"] - x.loc["y"]), axis=1)

    total_distance: int = sorted["distance"].sum()

    return total_distance


if __name__ == "__main__":
    input: DataFrame = pandas.read_csv(INPUT_FILE_PATH)

    answer: int = solve(input)

    print(f"answer: {answer}")
