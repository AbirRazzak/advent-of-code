import pytest

from advent_of_code.day_06 import calculate_distance, does_player_win


@pytest.mark.parametrize(
    ["button", "total", "expected"],
    [
        [0, 7, 0],
        [1, 7, 6],
        [2, 7, 10],
        [3, 7, 12],
        [4, 7, 12],
        [5, 7, 10],
        [6, 7, 6],
        [7, 7, 0],
    ],
)
def test_calculate_distance(button: int, total: int, expected: int):
    assert calculate_distance(button_held_duration=button, total_time=total) == expected


@pytest.mark.parametrize(
    ["button", "total", "enemy", "expected"],
    [
        [0, 7, 9, False],
        [1, 7, 9, False],
        [2, 7, 9, True],
        [3, 7, 9, True],
        [4, 7, 9, True],
        [5, 7, 9, True],
        [6, 7, 9, False],
        [7, 7, 9, False],
    ],
)
def test_calculate_distance(button: int, total: int, enemy: int, expected: bool):
    assert (
        does_player_win(
            button_held_duration=button, total_time=total, distance_to_beat=enemy
        )
        == expected
    )
