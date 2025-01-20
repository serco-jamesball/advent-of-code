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

PART_1_REPRODUCABLE_EQUATIONS: frozenset[Equation] = frozenset(
    {
        (190, (10, 19)),
        (3267, (81, 40, 27)),
        (292, (11, 6, 16, 20)),
    }
)

PART_2_REPRODUCABLE_EQUATIONS: frozenset[Equation] = frozenset(
    {
        (190, (10, 19)),
        (156, (15, 6)),
        (3267, (81, 40, 27)),
        (7290, (6, 8, 6, 15)),
        (192, (17, 8, 14)),
        (292, (11, 6, 16, 20)),
    }
)

PART_1_OPERATIONS: str = ["add", "mul"]
PART_2_OPERATIONS: str = ["add", "concat", "mul"]

PART_1_ANSWER: int = 3749
PART_2_ANSWER: int = 11387


def test_get_equations() -> None:
    assert solution.get_equations(EQUATIONS_FILE_PATH) == EQUATIONS


@pytest.mark.parametrize(
    "equation, expected",
    [
        (
            equation,
            equation[0] if equation in PART_1_REPRODUCABLE_EQUATIONS else None,
        )
        for equation in EQUATIONS
    ],
)
def test_reproduce_test_result_part_1(equation: Equation, expected: int) -> None:
    assert solution.reproduce_test_value(equation, PART_1_OPERATIONS) == expected


@pytest.mark.parametrize(
    "equation, expected",
    [
        (
            equation,
            equation[0] if equation in PART_2_REPRODUCABLE_EQUATIONS else None,
        )
        for equation in EQUATIONS
    ],
)
def test_reproduce_test_result_part_2(equation: Equation, expected: int) -> None:
    assert solution.reproduce_test_value(equation, PART_2_OPERATIONS) == expected


def test_get_answer_part_1() -> None:
    assert solution.get_answer(EQUATIONS, PART_1_OPERATIONS) == PART_1_ANSWER


def test_get_answer_part_2() -> None:
    assert solution.get_answer(EQUATIONS, PART_2_OPERATIONS) == PART_2_ANSWER
