import itertools

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


def distance(v: tuple) -> int:
    a, b = v

    return b - a


def calculate_final_number_and_sum(current_numbers: list[int]) -> tuple[int, int]:
    if current_numbers[0] == 0 and set(current_numbers) == {0}:
        return 0, 0

    next_sequence = map(distance, itertools.pairwise(current_numbers))
    next_sequence_list = list(next_sequence)

    next_final_number, current_sum = calculate_final_number_and_sum(
        current_numbers=next_sequence_list
    )

    final_number = current_numbers[-1] + next_final_number
    final_sum = current_sum + final_number

    return final_number, final_sum


def get_final_number_for_puzzle_input_line(line: str) -> int:
    numbers = [int(s) for s in line.split()]
    final_number, _ = calculate_final_number_and_sum(numbers)

    return final_number


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=9)

    part_1_answer = 0
    for line in puzzle_input.splitlines():
        part_1_answer += get_final_number_for_puzzle_input_line(line)

    print(f"Part 1: {part_1_answer}")


if __name__ == "__main__":
    main()
