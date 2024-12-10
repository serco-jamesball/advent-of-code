import day2.part1.solution as solution
import utility
from pandas import DataFrame
from pathlib import Path


def test_solve() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)

    input: DataFrame = utility.get_dataframe(input_file_path)

    assert solution.solve(input) == 2
