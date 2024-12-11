import year2024.day02.solution as solution
import year2024.utility as utility
from pandas import DataFrame


TEST_INPUT: DataFrame = utility.get_input(__file__)


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(TEST_INPUT) == 2
