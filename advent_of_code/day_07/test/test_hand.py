import pytest

from advent_of_code.day_07 import Hand


@pytest.mark.parametrize(
    ["cards", "expected"],
    [
        ("2", 10000000002),
        ("A", 10000000014),
        ("AA", 20000001414),
        ("322AA", 30302021414),
        ("AAA", 40000141414),
    ],
)
def test_get_card_value(cards, expected):
    h = Hand(cards=cards, bid=0)

    result = h.get_card_value()

    assert result == expected
