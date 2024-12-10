import utility
from pandas import DataFrame
from pathlib import Path


def solve(input: DataFrame) -> int:
    input["occurrences"] = [len(input[input[1] == value]) for value in input[0]]

    input["similarity"] = input["occurrences"] * input[0]

    similarity_score: int = input["similarity"].sum()

    return similarity_score


def main() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)

    input: DataFrame = utility.get_dataframe(input_file_path)

    answer: int = solve(input)

    print(utility.get_answer_message(file_path, answer))


if __name__ == "__main__":
    main()
