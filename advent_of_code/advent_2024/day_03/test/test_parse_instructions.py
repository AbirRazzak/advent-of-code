from advent_2024.day_03 import parse_instructions


# Part 1
def test_parse_instructions_part_1():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    result = parse_instructions(input)

    assert result == expected


def test_parse_instructions_part_2():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]

    result = parse_instructions(input)

    assert result == expected
