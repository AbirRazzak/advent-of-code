from advent_2024.day_03 import calculate_mul_instruction


def test_calculate_mul_instruction():
    input = "mul(4,5)"
    expected = 4 * 5

    result = calculate_mul_instruction(input)

    assert result == expected
