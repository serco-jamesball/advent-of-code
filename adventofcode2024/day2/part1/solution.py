import numpy
import utility
from pandas import DataFrame
from pathlib import Path


def solve(input: DataFrame) -> int:
    # Transform the input into a readable format
    # nb: A -1 value represents a null
    reports: DataFrame = input.assign(is_safe=numpy.nan)
    reports = reports.replace(numpy.nan, numpy.nan_to_num(numpy.nan, nan=-1))
    reports = reports.astype(dtype='int32')

    columns: list[str] = [
        column
        for column in reports.columns
        if column != 'is_safe'
    ]
    for i, row in reports[columns].iterrows():
        report: DataFrame = row.to_frame(name="level")

        # Exclude null values
        report = report.iloc[lambda row: row.values != -1].copy()

        # Add column with value of previous row
        report["lag"] = report.shift(periods=1, fill_value=0)

        # Remove first row, copy to avoid SettingWithCopyWarning
        report = report.iloc[1:].copy()

        # Add column with delta between current and previous value
        report["delta"] = abs(report["level"] - report["lag"])

        # Add column with flag for whether delta is at least 1 and no more than 3
        report["is_delta_in_tolerance"] = report.apply(
            lambda row: int(row["delta"] > 0 and row["delta"] < 4),
            axis=1,
        )

        # Add column with flag for whether level is increasing
        report["is_increasing"] = report.apply(
            lambda row: int(row["level"] > row["lag"]),
            axis=1,
        )
        # Add column with flag for whether level is decreasing
        report["is_decreasing"] = report.apply(
            lambda row: int(row["level"] < row["lag"]),
            axis=1,
        )

        # Evaluate whether report is safe or unsage
        #   When all deltas are in tolerance
        #   And all levels are increasing
        #   Or all level are decreasing
        #   Then safe
        #   Else unsafe
        length: int = len(report)

        reports.loc[i, "is_safe"] = int(
            len(report.loc[report["is_delta_in_tolerance"] == 1]) == length
            and (
                len(report.loc[report["is_increasing"] == 1]) == length
                or len(report.loc[report["is_decreasing"] == 1]) == length
            )
        )

    total_safe_reports: int = reports["is_safe"].sum()

    return total_safe_reports


def main() -> None:
    file_path: Path = Path(__file__)

    input_file_path: Path = utility.get_input_file_path(file_path)

    input: DataFrame = utility.get_dataframe(input_file_path)

    answer: int = solve(input)

    print(utility.get_answer_message(file_path, answer))


if __name__ == "__main__":
    main()
