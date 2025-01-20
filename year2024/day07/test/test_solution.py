import pytest
import year2024.day07.solution as solution
from year2024.day07.solution import Equation


EQUATIONS_FILE_PATH: str = r"year2024\day07\test\resource\equations.txt"

EQUATIONS: frozenset[Equation] = frozenset(
    {
        (190, (10, 19)),
        (3267, (81, 40, 27)),
        (83, (17, 5)),
        (156, (15, 6)),
        (7290, (6, 8, 6, 15)),
        (161011, (16, 10, 13)),
        (192, (17, 8, 14)),
        (21037, (9, 7, 18, 13)),
        (292, (11, 6, 16, 20)),
    }
)

REPRODUCABLE_EQUATIONS: frozenset[Equation] = frozenset(
    {
        (190, (10, 19)),
        (3267, (81, 40, 27)),
        (292, (11, 6, 16, 20)),
    }
)

TOTAL_CALIBRATION_RESULT: int = 3749


def test_get_equations() -> None:
    assert solution.get_equations(EQUATIONS_FILE_PATH) == EQUATIONS


@pytest.mark.parametrize(
    "equation, expected",
    [
        (
            equation,
            equation[0] if equation in REPRODUCABLE_EQUATIONS else None,
        )
        for equation in EQUATIONS
    ],
)
def test_reproduce_test_result(equation: Equation, expected: int) -> None:
    assert solution.reproduce_test_value(equation) == expected


def test_get_part_1_answer() -> None:
    assert solution.get_part_1_answer(EQUATIONS) == TOTAL_CALIBRATION_RESULT
