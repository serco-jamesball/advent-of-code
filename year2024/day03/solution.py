import copy
import operator
import re
import year2024.utility as utility
from re import Pattern


DAY: str = "3"

CORRUPTED_MEMORY_FILE_PATH: str = r"year2024\day03\resource\input.txt"

# I tried and failed to parse the do() instructions using a regular expression.
# This was the closest I came:
#     ^(?<!don't\(\))(.*?)(?=don't\(\))|(?<=do\(\))(.*?)(?=don't\(\))|(?<=do\(\))(.*?)(?<!don't\(\))$
DO_INSTRUCTION: str = "do()"
DONT_INSTRUCTION: str = "don't()"


MUL_INSTRUCTION_PATTERN: Pattern = re.compile(
    r"mul\((?P<x>[0-9]{1,3}),(?P<y>[0-9]{1,3})\)"
)


DoInstruction = str
MulInstruction = tuple[int, int]


def scan_corrupted_memory(
    corrupted_memory: str, is_processing_of_do_instructions_enabled: bool
) -> list[MulInstruction]:
    if is_processing_of_do_instructions_enabled:
        return [
            mul_instruction
            for do_instruction in find_do_instructions(corrupted_memory)
            for mul_instruction in find_mul_instructions(do_instruction)
        ]
    return find_mul_instructions(corrupted_memory)


def find_do_instructions(corrupted_memory: str) -> list[DoInstruction]:
    do_instructions: list[DoInstruction] = []

    is_mul_instructions_enabled: bool = True
    i: int = 0

    copy_of_corrupted_memory: str = copy.copy(corrupted_memory)

    while True:
        if is_mul_instructions_enabled:
            if DONT_INSTRUCTION in copy_of_corrupted_memory:
                i = copy_of_corrupted_memory.find(DONT_INSTRUCTION)

                do_instructions.append(copy_of_corrupted_memory[:i])
                copy_of_corrupted_memory = copy_of_corrupted_memory[
                    i + len(DONT_INSTRUCTION) :
                ]
            else:
                do_instructions.append(copy_of_corrupted_memory[:])

                return do_instructions
        else:
            if DO_INSTRUCTION in copy_of_corrupted_memory:
                i = copy_of_corrupted_memory.find(DO_INSTRUCTION)

                copy_of_corrupted_memory = copy_of_corrupted_memory[
                    i + len(DO_INSTRUCTION) :
                ]
            else:
                return do_instructions

        is_mul_instructions_enabled = not is_mul_instructions_enabled


def find_mul_instructions(corrupted_memory: str) -> list[MulInstruction]:
    return [
        (int(_match["x"]), int(_match["y"]))
        for _match in MUL_INSTRUCTION_PATTERN.finditer(corrupted_memory)
    ]


def sum_mul_instructions(mul_instructions: list[MulInstruction]) -> int:
    return sum(operator.mul(*mul_instruction) for mul_instruction in mul_instructions)


def run_program(
    corrupted_memory_file_path: str, is_processing_of_do_instructions_enabled: bool
) -> int:
    with open(corrupted_memory_file_path) as corrupted_memory_file:
        corrupted_memory: str = corrupted_memory_file.read().strip()

    uncurropted_mul_instructions: list[MulInstruction] = scan_corrupted_memory(
        corrupted_memory, is_processing_of_do_instructions_enabled
    )

    return sum_mul_instructions(uncurropted_mul_instructions)


def main() -> None:
    part_1_answer: int = run_program(CORRUPTED_MEMORY_FILE_PATH, False)
    part_2_answer: int = run_program(CORRUPTED_MEMORY_FILE_PATH, True)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
