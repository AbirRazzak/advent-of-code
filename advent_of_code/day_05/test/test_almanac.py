from advent_of_code.day_05 import Almanac
from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


def test_part_1():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(day=5)
    almanac = Almanac.from_puzzle_input(puzzle=puzzle_input)

    result = almanac.get_lowest_location_with_a_seed()

    assert result == 88151870
