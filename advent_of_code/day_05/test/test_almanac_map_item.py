import pytest

from advent_of_code.day_05 import AlmanacMapItem


def test_almanac_map_item_get_destination_for_number_when_number_not_in_range_returns_number():
    map_item = AlmanacMapItem(
        destination_range_start=1, source_range_start=2, range_length=3
    )

    result = map_item.get_destination_for_number(number=0)

    assert result == 0


@pytest.mark.parametrize(["input", "expected"], [[2, 1], [4, 3]])
def test_almanac_map_item_get_destination_for_number_when_number_in_range_returns_destination_number(
    input: int, expected: int
):
    map_item = AlmanacMapItem(
        destination_range_start=1, source_range_start=2, range_length=3
    )

    result = map_item.get_destination_for_number(number=input)

    assert result == expected
