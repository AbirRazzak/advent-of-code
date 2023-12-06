from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


def test_get_puzzle_input():
    repo = OfflinePuzzleInputRepository()

    expected = "This is a test file.\n"

    result = repo.get_puzzle_input(day=0)

    assert result == expected
