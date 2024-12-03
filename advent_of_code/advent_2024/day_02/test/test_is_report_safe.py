import pytest

from advent_2024.day_02 import is_report_safe


@pytest.mark.parametrize(
    ["report", "expected"],
    [
        ["7 6 4 2 1", True],
        ["1 3 6 7 9", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", False],
        ["8 6 4 4 1", False],
        ["1 2  8 9", False],
        ["9 7 6  1", False],
    ],
)
def test_is_report_safe(report: str, expected: bool):
    result = is_report_safe(report=report)

    assert result == expected
