import day1.part2.solution as solution
import pandas
from pandas import DataFrame
from pathlib import Path


INPUT_FILE_PATH: Path = Path(__file__).parent.joinpath("input.csv")


def test_solve() -> None:
    input: DataFrame = pandas.read_csv(INPUT_FILE_PATH)

    assert solution(input) == 31
