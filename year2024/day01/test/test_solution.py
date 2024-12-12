import year2024.day01.solution as solution
import year2024.utility as utility
from pandas import DataFrame


TEST_INPUT: DataFrame = utility.get_input(utility.get_input_file_path(__file__))


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(TEST_INPUT) == 11


def test_get_part_2_answer() -> None:
    assert solution.get_part_2_answer(TEST_INPUT) == 31
