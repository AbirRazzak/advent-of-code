import pytest

from advent_of_code.day_09 import calculate_final_number_and_sum


@pytest.mark.parametrize(
    ["numbers", "expected_number", "expected_sum"],
    [
        [
            [0, 3, 6, 9, 12, 15],
            18,
            21,
        ],
        [
            [10, 13, 16, 21, 30, 45],
            68,
            101,
        ],
    ],
)
def test_calculate_final_number_and_sum(
    numbers: list[int],
    expected_number: int,
    expected_sum: int,
):
    final_number_result, final_sum_result = calculate_final_number_and_sum(
        current_numbers=numbers
    )

    assert final_number_result == expected_number
    assert final_sum_result == expected_sum
