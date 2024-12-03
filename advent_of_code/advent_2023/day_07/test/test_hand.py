import pytest

from advent_of_code.day_07 import Hand


@pytest.mark.parametrize(
    ["cards", "expected"],
    [
        ("2", 10000000002),
        ("A", 10000000014),
        ("AA", 20000001414),
        ("322AA", 30302021414),
        ("J22AA", 50102021414),  # jack becomes a 2/A to become a full house
        ("J32AA", 40103021414),  # jack becomes an A to become a 3-of-a-kind
        ("AAA", 40000141414),
        ("JJJJJ", 70101010101),
    ],
)
def test_get_card_value(cards, expected):
    h = Hand(cards=cards, bid=0)

    result = h.get_card_value()

    assert result == expected
