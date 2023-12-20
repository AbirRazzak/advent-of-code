import itertools

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


def distance(v: tuple) -> int:
    a, b = v

    return b - a


def calculate_first_and_final_number(current_numbers: list[int]) -> tuple[int, int]:
    if current_numbers[0] == 0 and set(current_numbers) == {0}:
        return 0, 0

    next_sequence = map(distance, itertools.pairwise(current_numbers))
    next_sequence_list = list(next_sequence)

    next_first_number, next_final_number = calculate_first_and_final_number(
        current_numbers=next_sequence_list
    )

    first_number = current_numbers[0] - next_first_number
    final_number = current_numbers[-1] + next_final_number

    return first_number, final_number


def get_first_and_final_number_for_puzzle_input_line(line: str) -> tuple[int, int]:
    numbers = [int(s) for s in line.split()]
    first_number, final_number = calculate_first_and_final_number(numbers)

    return first_number, final_number


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=9)

    part_1_answer = 0
    part_2_answer = 0
    for line in puzzle_input.splitlines():
        first_num, final_num = get_first_and_final_number_for_puzzle_input_line(line)
        part_1_answer += final_num
        part_2_answer += first_num

    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {part_2_answer}")


if __name__ == "__main__":
    main()
