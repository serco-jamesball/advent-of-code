import year2024.constant as constant
import numpy
import year2024.utility as utility
from joblib import Memory
from pandas import DataFrame


DAY: str = "2"


memory: Memory = Memory(constant.CACHE_FOLDER_PATH, verbose=0)


def evaluate_report(report: DataFrame) -> int:
    # Evaluate whether report is safe or unsafe
    #   When all deltas are in tolerance
    #   And all levels are increasing
    #   Or all level are decreasing
    #   Then safe
    #   Else unsafe
    length: int = len(report)

    return int(
        len(report.loc[report["is_delta_in_tolerance"] == 1]) == length
        and (
            len(report.loc[report["is_increasing"] == 1]) == length
            or len(report.loc[report["is_decreasing"] == 1]) == length
        )
    )


@memory.cache
def evaluate_reports(reports: DataFrame) -> DataFrame:
    # Transform the input into a readable format
    # nb: A -1 value represents a null
    reports: DataFrame = reports.assign(is_safe=numpy.nan)
    reports = reports.replace(numpy.nan, numpy.nan_to_num(numpy.nan, nan=-1))
    reports = reports.astype(dtype="int64")

    columns: list[str] = [column for column in reports.columns if column != "is_safe"]
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

        reports.loc[i, "is_safe"] = evaluate_report(report)

    return reports


def get_part_1_answer(input: DataFrame) -> int:
    evaluated_reports: DataFrame = evaluate_reports(input)

    total_safe_reports: int = evaluated_reports["is_safe"].sum()

    return total_safe_reports


def main() -> None:
    input: DataFrame = utility.get_input(__file__)

    part_1_answer: int = get_part_1_answer(input)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))


if __name__ == "__main__":
    main()

