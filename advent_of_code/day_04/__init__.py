from __future__ import annotations

from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class ScratchCard(BaseModel):
    id: int
    winning_numbers: list[int]
    card_numbers: list[int]

    def get_winning_card_numbers(self) -> list[int]:
        winning_numbers_set = set(self.winning_numbers).intersection(
            set(self.card_numbers)
        )

        return list(winning_numbers_set)

    def get_winning_card_numbers_count(self) -> int:
        return len(self.get_winning_card_numbers())

    def get_winning_card_numbers_points(self) -> int:
        if self.get_winning_card_numbers_count() == 0:
            return 0

        return pow(base=2, exp=self.get_winning_card_numbers_count() - 1)


class ScratchCardPile(BaseModel):
    cards: list[ScratchCard]

    @staticmethod
    def from_puzzle_input(puzzle: str) -> ScratchCardPile:
        cards: list[ScratchCard] = []

        for line in puzzle.splitlines():
            # line looks something like this: "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
            card_id_info, everything_else = line.split(":", maxsplit=1)

            # parse card ID
            card_id_info: str
            card_id_str = card_id_info.strip("Card ")
            card_id = int(card_id_str)

            # everything_else = " 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
            winning_numbers_info, card_numbers_info = everything_else.split(
                "|", maxsplit=1
            )

            # parse winning_numbers_info
            winning_numbers_info: str
            winning_numbers_info = winning_numbers_info.strip()
            winning_numbers_str_list = winning_numbers_info.split()
            winning_numbers = [int(x) for x in winning_numbers_str_list]

            # parse card_numbers_info
            card_numbers_info: str
            card_numbers_info = card_numbers_info.strip()
            card_numbers_str_list = card_numbers_info.split()
            card_numbers = [int(x) for x in card_numbers_str_list]

            cards.append(
                ScratchCard(
                    id=card_id,
                    winning_numbers=winning_numbers,
                    card_numbers=card_numbers,
                )
            )

        return ScratchCardPile(cards=cards)

    def get_total_points(self) -> int:
        """
        This is the solution to part 1. This method is not used in part 2.
        :return: The sum of all the points earned by all the cards in this pile.
        """

        total_points = 0

        for card in self.cards:
            total_points += card.get_winning_card_numbers_points()

        return total_points

    def get_total_scratch_cards(self) -> int:
        """
        This is the solution to part 2. This method is not used in part 1.
        :return: The total number of scratch cards (including the original 202, plus the duplicate winning cards).
        """

        total = len(self.cards)

        duplicate_cards_num_by_id: dict[int, int] = {}

        return total


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=4)

    scratch_card_pile = ScratchCardPile.from_puzzle_input(puzzle=puzzle_input)
    print(scratch_card_pile)

    print(f"Part 1 - Total points: {scratch_card_pile.get_total_points()}")
    print(f"Part 2 - Total cards: {scratch_card_pile.get_total_scratch_cards()}")


if __name__ == "__main__":
    main()
