import pandas
import year2024.day01.solution as solution
import year2024.utility as utility
from pandas import DataFrame


pandas.options.mode.copy_on_write = True


LOCATION_LISTS_FILE_PATH: str = r"year2024\day01\test\resource\input.csv"
LOCATION_LISTS: DataFrame = pandas.read_csv(
    LOCATION_LISTS_FILE_PATH, names=utility.get_column_labels(LOCATION_LISTS_FILE_PATH)
)


def test_find_total_distance_between_lists() -> None:
    assert solution.find_total_distance_between_lists(LOCATION_LISTS) == 11


def test_find_similarity_score() -> None:
    assert solution.find_similarity_score(LOCATION_LISTS) == 31
