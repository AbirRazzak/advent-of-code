from __future__ import annotations

from bisect import insort
from enum import Enum

from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class CardType(str, Enum):
    five_of_a_kind = "Five of a Kind"
    four_of_a_kind = "Four of a Kind"
    full_house = "Full House"
    three_of_a_kind = "Three of a Kind"
    two_pair = "Two Pair"
    one_pair = "One Pair"
    high_card = "High Card"


CARD_TYPE_TO_VALUE_MAPPING = {
    CardType.five_of_a_kind: 70000000000,
    CardType.four_of_a_kind: 60000000000,
    CardType.full_house: 50000000000,
    CardType.three_of_a_kind: 40000000000,
    CardType.two_pair: 30000000000,
    CardType.one_pair: 20000000000,
    CardType.high_card: 10000000000,
}

CARD_TO_VALUE_MAPPING = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}


class Hand(BaseModel):
    cards: str
    bid: int
    value: int = None

    def __lt__(self, other: Hand) -> bool:
        return self.get_card_value() < other.get_card_value()

    def _get_winning_card_type(self) -> CardType:
        dict_of_characters: dict[str, int] = {}

        # count all the characters in the str
        for character in list(self.cards):
            v = dict_of_characters.setdefault(character, 0)
            dict_of_characters[character] = v + 1

        # get the max value
        max_value = max(dict_of_characters.values())

        if max_value == 5:
            return CardType.five_of_a_kind

        elif max_value == 4:
            return CardType.four_of_a_kind

        elif max_value == 3:
            if len(dict_of_characters) == 2:
                return CardType.full_house
            else:
                return CardType.three_of_a_kind

        elif max_value == 2:
            if len(dict_of_characters) == 3:
                return CardType.two_pair
            else:
                return CardType.one_pair

        else:
            return CardType.high_card

    def _get_card_hand_value(self) -> int:
        value_as_str = ""
        for character in list(self.cards):
            card_value = CARD_TO_VALUE_MAPPING[character]
            value_as_str += card_value

        return int(value_as_str)

    def get_card_value(self):
        if self.value is None:
            # Get the value of the win for the card hand
            card_winning_type = self._get_winning_card_type()
            winning_value = CARD_TYPE_TO_VALUE_MAPPING[card_winning_type]

            # Get the values of the cards in the hand in order
            card_hand_value = self._get_card_hand_value()

            self.value = winning_value + card_hand_value

        return self.value


class HandCollection(BaseModel):
    hands: list[Hand] = []

    def add_hand_to_collection(self, hand: Hand) -> None:
        # Add the hand into the hands collection, preserving the hands in value order.
        # see: https://docs.python.org/3/library/bisect.html?highlight=insort#bisect.insort
        insort(self.hands, hand)

    def get_total_winnings(self) -> int:
        total_winnings = 0

        for i in range(len(self.hands)):
            total_winnings += (i + 1) * self.hands[i].bid

        return total_winnings

    @staticmethod
    def from_puzzle_input(puzzle: str) -> HandCollection:
        hand_collection = HandCollection()

        for line in puzzle.splitlines():
            cards, bid = line.split()
            hand = Hand(cards=cards, bid=int(bid))
            hand_collection.add_hand_to_collection(hand=hand)

        return hand_collection


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=7)
    hand_collection = HandCollection.from_puzzle_input(puzzle=puzzle_input)

    print(hand_collection)

    print(f"Total winnings: {hand_collection.get_total_winnings()}")


if __name__ == "__main__":
    main()
