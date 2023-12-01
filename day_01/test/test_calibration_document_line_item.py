import pytest

from day_01 import CalibrationDocumentLineItem


@pytest.mark.parametrize(
    ["raw_value", "expected_value"],
    [
        ["1abc2", 12],
        ["pqr3stu8vwx", 38],
        ["a1b2c3d4e5f", 15],
        ["treb7uchet", 77],
        ["two1nine", 29],
        ["eightwothree", 83],
        ["abcone2threexyz", 13],
        ["xtwone3four", 24],
        ["4nineeightseven2", 42],
        ["zoneight234", 14],
        ["7pqrstsixteen", 76],
        ["sevenine", 79],
        ["sevenine8", 78],
        ["eighthree", 83],
        ["asdsadnineasdasd", 99],
        ["fourvptdnbpqcxktwoone4oneone", 41],  # "one" is repeated multiple times
    ],
)
def test_get_calibration_value(raw_value: str, expected_value: int):
    line_item = CalibrationDocumentLineItem(contents=raw_value)

    result = line_item.get_calibration_value()

    assert result == expected_value
