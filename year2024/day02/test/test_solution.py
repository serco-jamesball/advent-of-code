import pandas
import pytest
import year2024.day02.solution as solution
import year2024.utility as utility
from pandas import DataFrame


pandas.options.mode.copy_on_write = True


REPORTS_FILE_PATH: str = r"year2024\day02\test\resource\input.csv"
REPORTS: DataFrame = pandas.read_csv(
    REPORTS_FILE_PATH, names=utility.get_column_labels(REPORTS_FILE_PATH)
)


def test_process_report() -> None:
    report: DataFrame = DataFrame({"level": [1, 2, 3, solution.NULL_VALUE]})

    expected: DataFrame = DataFrame(
        {
            "level": [2, 3],
            "lag": [1, 2],
            "delta": [1, 1],
            "is_delta_in_tolerance": [1, 1],
            "is_increasing": [1, 1],
            "is_decreasing": [0, 0],
        }
    )

    assert solution.process_report(report).reset_index(drop=True).equals(expected)


@pytest.mark.parametrize("delta, expected", [(1, 1), (2, 1), (3, 1), (0, 0), (4, 0)])
def test_is_delta_in_tolerance(delta: int, expected: int) -> None:
    assert solution.is_delta_in_tolerance(delta) == expected


@pytest.mark.parametrize("level, lag, expected", [(2, 1, 1), (1, 1, 0), (0, 1, 0)])
def test_is_increasing(level: int, lag: int, expected: int) -> None:
    assert solution.is_increasing(level, lag) == expected


@pytest.mark.parametrize("level, lag, expected", [(2, 1, 0), (1, 1, 0), (0, 1, 1)])
def test_is_decreasing(level: int, lag: int, expected: int) -> None:
    assert solution.is_decreasing(level, lag) == expected


@pytest.mark.parametrize(
    "length, exclude, expected", [(3, 0, [1, 2]), (3, 1, [0, 2]), (3, 2, [0, 1])]
)
def test_get_range(length: int, exclude: int, expected: list[int]):
    assert solution.get_range(length, exclude) == expected


@pytest.mark.parametrize(
    "report, expected",
    [
        # pass: all increasing in tolerance
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 1],
                    "is_increasing": [1, 1, 1],
                    "is_decreasing": [0, 0, 0],
                }
            ),
            1,
        ),
        # pass: all decreasing in tolerance
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 1],
                    "is_increasing": [0, 0, 0],
                    "is_decreasing": [1, 1, 1],
                }
            ),
            1,
        ),
        # fail: not all increasing in tolerance
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 0],
                    "is_increasing": [1, 1, 1],
                    "is_decreasing": [0, 0, 0],
                }
            ),
            0,
        ),
        # fail: not all decreasing in tolerance
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 0],
                    "is_increasing": [0, 0, 0],
                    "is_decreasing": [1, 1, 1],
                }
            ),
            0,
        ),
        # fail: not all increasing
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 1],
                    "is_increasing": [1, 1, 0],
                    "is_decreasing": [0, 0, 1],
                }
            ),
            0,
        ),
        # fail: not all decreasing
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 1],
                    "is_increasing": [0, 0, 1],
                    "is_decreasing": [1, 1, 0],
                }
            ),
            0,
        ),
        # fail: has level neither increasing nor decreasing
        (
            DataFrame(
                {
                    "is_delta_in_tolerance": [1, 1, 0],
                    "is_increasing": [0, 0, 0],
                    "is_decreasing": [1, 1, 0],
                }
            ),
            0,
        ),
    ],
)
def test_is_safe(report: DataFrame, expected: int) -> None:
    assert solution.is_safe(report) == expected


@pytest.mark.parametrize(
    "is_problem_dampener_enabled, expected", [(False, 2), (True, 4)]
)
def test_get_answer(is_problem_dampener_enabled: bool, expected: int) -> None:

    assert (
        solution.find_total_safe_reports(REPORTS, is_problem_dampener_enabled)
        == expected
    )
