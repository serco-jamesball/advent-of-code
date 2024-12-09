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

    answer: int = solve(pandas.read_csv(input_file_path))

    day, part = utility.parse_file_name(file_path)
    message: str = utility.get_answer_message(day, part, answer)

    print(message)


if __name__ == "__main__":
    main()
