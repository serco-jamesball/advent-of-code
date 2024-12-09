import pandas
import utility
from pandas import DataFrame
from pathlib import Path


def solve(input: DataFrame) -> int:
    input["occurrences"] = [len(input[input["y"] == x]) for x in input["x"]]

    input["similarity"] = input["occurrences"] * input["x"]

    similarity_score: int = input["similarity"].sum()

    return similarity_score


def main() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)
    input: DataFrame = pandas.read_csv(input_file_path)

    answer: int = solve(input)

    print(utility.get_answer_message(file_path, answer))


if __name__ == "__main__":
    main()
