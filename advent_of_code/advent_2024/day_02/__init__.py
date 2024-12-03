from __future__ import annotations

from typing import Optional

from puzzle_input.offline_repo import OfflinePuzzleInputRepository


def is_report_safe(report: str) -> bool:
    levels = report.split()

    is_ascending: Optional[bool] = None
    for i in range(len(levels)):
        try:
            level_difference = int(levels[i + 1]) - int(levels[i])
            if is_ascending is None:
                if level_difference > 0:
                    is_ascending = True
                else:
                    is_ascending = False

            min_difference = 1 if is_ascending else -3
            max_difference = 3 if is_ascending else -1

            if min_difference <= level_difference <= max_difference:
                pass
            else:
                return False

        except:
            pass

    return True


def is_report_safe_with_dampener(report: str) -> bool:
    levels = report.split()

    is_ascending: Optional[bool] = None
    for i in range(len(levels)):
        try:
            level_difference = int(levels[i + 1]) - int(levels[i])
            if is_ascending is None:
                if level_difference > 0:
                    is_ascending = True
                else:
                    is_ascending = False

            min_difference = 1 if is_ascending else -3
            max_difference = 3 if is_ascending else -1

            if min_difference <= level_difference <= max_difference:
                pass
            else:
                new_levels_0 = levels.copy()
                new_levels_0.pop(i - 1)
                report_without_previous = " ".join(new_levels_0)

                new_levels_1 = levels.copy()
                new_levels_1.pop(i)
                report_without_current = " ".join(new_levels_1)

                new_levels_2 = levels.copy()
                new_levels_2.pop(i + 1)
                report_without_next = " ".join(new_levels_2)

                return (
                    is_report_safe(report=report_without_previous)
                    or is_report_safe(report=report_without_current)
                    or is_report_safe(report=report_without_next)
                )

        except:
            pass

    return True


def main():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(year=2024, day=2)
    reports = puzzle_input.splitlines()

    num_safe_reports = 0
    num_safe_reports_with_dampener = 0
    for report in reports:
        if is_report_safe(report=report):
            num_safe_reports += 1
            num_safe_reports_with_dampener += 1

        elif is_report_safe_with_dampener(report=report):
            num_safe_reports_with_dampener += 1

    print(f"num_safe_reports: {num_safe_reports}")
    print(f"num_safe_reports_with_dampener: {num_safe_reports_with_dampener}")


if __name__ == "__main__":
    main()
