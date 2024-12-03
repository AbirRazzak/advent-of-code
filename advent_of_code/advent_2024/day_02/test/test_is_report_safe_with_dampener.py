import pytest

from advent_2024.day_02 import is_report_safe_with_dampener


@pytest.mark.parametrize(
    ["report", "expected"],
    [
        ["7 6 4 2 1", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", True],
        ["8 6 4 4 1", True],
        ["1 3 6 7 9", True],
        ["34 32 31 29 29 27", True],
        ["64 63 64 66 67", True],
    ],
)
def test_is_report_safe_with_dampener(report: str, expected: bool):
    result = is_report_safe_with_dampener(report=report)

    assert result == expected
