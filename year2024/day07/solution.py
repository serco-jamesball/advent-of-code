import itertools
import operator
import year2024.utility as utility
from collections.abc import Callable, Iterator


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


def reproduce_test_value(equation: Equation, operations: list[str]) -> int | None:
    answer, numbers = equation

    combinations: Iterator[tuple[Operation, ...]] = itertools.product(
        (getattr(operator, operation) for operation in operations),
        repeat=len(numbers) - 1,
    )

    for combination in combinations:
        product: int = 0

        for i in range(len(numbers)):
            if i + 1 == len(numbers):
                if product == answer:
                    return product
            else:
                x: int | str = numbers[i] if i == 0 else product
                y: int | str = numbers[i + 1]

                operation: Operation = combination[i]

                if operation is operator.concat:
                    x, y = str(x), str(y)

                product = int(operation(x, y))


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

    part_1_answer: int = get_answer(equations, ["add", "mul"])
    part_2_answer: int = get_answer(equations, ["add", "concat", "mul"])

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))
