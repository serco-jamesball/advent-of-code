from day1.part1.solution import solve
from pandas import DataFrame
from pathlib import Path

import pandas


INPUT_FILE_PATH: Path = Path(__file__).parent.joinpath("input.csv")


def test_solve() -> None:
    input: DataFrame = pandas.read_csv(INPUT_FILE_PATH)

    assert solve(input) == 11
