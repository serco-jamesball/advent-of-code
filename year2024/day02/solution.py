import numpy
import pandas
import year2024.utility as utility
from pandas import DataFrame


pandas.options.mode.copy_on_write = True


DAY: str = "2"

REPORTS_FILE_PATH: str = r"year2024\day02\resource\input.csv"

NULL_VALUE: int = -1

TOLERANCE_LOWER_THRESHOLD: int = 1
TOLERANCE_UPPER_THRESHOLD: int = 3


def process_report(report: DataFrame) -> DataFrame:
    # Exclude null values
    report = report.iloc[lambda row: row.values != -1]

    # Add column with value of previous row
    report["lag"] = report.shift(periods=1, fill_value=NULL_VALUE)

    # Remove first row
    report = report.iloc[1:]

    # Add column with delta between current and previous value
    report["delta"] = abs(report["level"] - report["lag"])

    # Add column with flag for whether delta is at least 1 and no more than 3
    report["is_delta_in_tolerance"] = report.apply(
        lambda row: is_delta_in_tolerance(row["delta"]),
        axis=1,
    )

    # Add column with flag for whether level is increasing
    report["is_increasing"] = report.apply(
        lambda row: is_increasing(row["level"], row["lag"]),
        axis=1,
    )
    # Add column with flag for whether level is decreasing
    report["is_decreasing"] = report.apply(
        lambda row: is_decreasing(row["level"], row["lag"]),
        axis=1,
    )

    return report


def is_delta_in_tolerance(delta: int) -> int:
    return int(
        delta >= TOLERANCE_LOWER_THRESHOLD and delta <= TOLERANCE_UPPER_THRESHOLD
    )


def is_increasing(level: int, lag: int) -> int:
    return 1 if level > lag else 0


def is_decreasing(level: int, lag: int) -> int:
    return 1 if level < lag else 0


def is_safe(report: DataFrame) -> int:
    # Evaluate whether report is safe or unsafe
    #   When all deltas are in tolerance
    #   And all levels are increasing
    #   Or all level are decreasing
    #   Then safe
    #   Else unsafe
    return int(
        len(report.loc[report["is_delta_in_tolerance"] == 1]) == len(report)
        and (
            len(report.loc[report["is_increasing"] == 1]) == len(report)
            or len(report.loc[report["is_decreasing"] == 1]) == len(report)
        )
    )


def get_range(length: int, exclude: int) -> list[int]:
    return [i for i in range(length) if i != exclude]


def evaluate_reports(
    reports: DataFrame, is_problem_dampener_enabled: bool = False
) -> DataFrame:
    # Transform the input into a readable format
    # nb: A -1 value represents a null
    reports: DataFrame = reports.assign(is_safe=numpy.nan)
    reports = reports.replace(numpy.nan, numpy.nan_to_num(numpy.nan, nan=NULL_VALUE))
    reports = reports.astype(dtype="int64")

    columns: list[str] = [column for column in reports.columns if column != "is_safe"]

    for i, row in reports[columns].iterrows():
        report: DataFrame = row.to_frame(name="level")

        processed_report: DataFrame = process_report(report)

        _is_safe: bool = is_safe(processed_report)

        if is_problem_dampener_enabled and not _is_safe:
            for j in range(len(report)):
                processed_report: DataFrame = process_report(
                    report.iloc[get_range(len(report), j)]
                )

                _is_safe = is_safe(processed_report)

                if _is_safe:
                    break

        reports.loc[i, "is_safe"] = _is_safe

    return reports


def find_total_safe_reports(
    input: DataFrame, is_problem_dampener_mounted: bool = False
) -> int:
    evaluated_reports: DataFrame = evaluate_reports(input, is_problem_dampener_mounted)

    total_safe_reports: int = evaluated_reports["is_safe"].sum()

    return total_safe_reports


def main() -> None:
    reports: DataFrame = pandas.read_csv(
        REPORTS_FILE_PATH, names=utility.get_column_labels(REPORTS_FILE_PATH)
    )

    part_1_answer: int = find_total_safe_reports(reports)
    part_2_answer: int = find_total_safe_reports(
        reports, is_problem_dampener_mounted=True
    )

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
