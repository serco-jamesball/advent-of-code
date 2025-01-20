import itertools
import operator
import year2024.utility as utility
from collections.abc import Callable, Iterator


Equation = tuple[int, tuple[int, ...]]

Operation = str
Operator = Callable[[int, int], int]


DAY: str = "7"

EQUATIONS_FILE_PATH: str = r"year2024\day07\resource\equations.txt"

OPERATIONS: frozenset[tuple[Operation, Operator]] = frozenset(
    {
        ("+", operator.add),
        ("*", operator.mul),
    }
)


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


def reproduce_test_value(equation: Equation) -> int | None:
    answer, numbers = equation

    combinations: Iterator[tuple[Operator, ...]] = itertools.product(
        (operation for _, operation in OPERATIONS), repeat=len(numbers) - 1
    )

    for operations in combinations:
        product: int = 0

        for i in range(len(numbers)):
            if i + 1 == len(numbers):
                if product == answer:
                    return product
            else:
                x: int = numbers[i] if i == 0 else product
                y: int = numbers[i + 1]

                product = operations[i](x, y)


def get_part_1_answer(equations: frozenset[Equation]) -> int:
    return sum(filter(None, map(reproduce_test_value, equations)))


if __name__ == "__main__":
    equations: frozenset[Equation] = get_equations(EQUATIONS_FILE_PATH)

    part_1_answer: int = get_part_1_answer(equations)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))
