import year2024.utility as utility
from collections.abc import Callable
from operator import add, mul


cat: Callable[[str, str], str] = lambda x, y: int(str(x) + str(y))


Equation = tuple[int, tuple[int, ...]]

Operation = Callable[[int | str, int | str], int | str]


DAY: str = "7"

EQUATIONS_FILE_PATH: str = r"year2024\day07\resource\equations.txt"


def get_equations(equations_file_path: str) -> frozenset[Equation]:
    with open(equations_file_path) as equations_file:
        return frozenset(
            (
                int(equation[: equation.index(":")]),
                tuple(
                    int(number)
                    for number in equation[equation.index(":") + 2 :].split(" ")
                ),
            )
            for equation in equations_file.read().strip().split("\n")
        )


def reproduce_test_value(equation: Equation, operations: list[Operation]) -> int | None:
    answer, numbers = equation

    products: frozenset[int] = frozenset({numbers[0]})
    for y in numbers[1:]:
        products = frozenset(
            operation(x, y) for x in products for operation in operations
        )

    if answer in products:
        return answer


def get_answer(equations: frozenset[Equation], operations: list[str]) -> int:
    return sum(
        test_value
        for test_value in (
            reproduce_test_value(equation, operations) for equation in equations
        )
        if test_value is not None
    )


if __name__ == "__main__":
    equations: frozenset[Equation] = get_equations(EQUATIONS_FILE_PATH)

    part_1_answer: int = get_answer(equations, [add, mul])
    part_2_answer: int = get_answer(equations, [add, cat, mul])

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))
