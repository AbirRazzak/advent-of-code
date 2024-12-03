import re

from puzzle_input.offline_repo import OfflinePuzzleInputRepository


def parse_instructions(text: str) -> list[str]:
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, text)

    return matches


def calculate_mul_instruction(instruction: str) -> int:
    numbers = [int(num) for num in instruction.strip("mul()").split(",")]

    return numbers[0] * numbers[1]


def part_1(instructions: list[str]):
    total = sum(
        calculate_mul_instruction(instruction)
        if instruction not in ["do()", "don't()"]
        else 0
        for instruction in instructions
    )
    print(f"Part 1: {total}")


def part_2(instructions: list[str]):
    is_enabled = True
    total = 0

    for i in range(len(instructions)):
        if instructions[i] == "do()":
            is_enabled = True
        elif instructions[i] == "don't()":
            is_enabled = False
        elif is_enabled:
            total += calculate_mul_instruction(instructions[i])

    print(f"Part 2: {total}")


def main():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(year=2024, day=3)
    instructions = parse_instructions(puzzle_input)
    part_1(instructions)
    part_2(instructions)


if __name__ == "__main__":
    main()
