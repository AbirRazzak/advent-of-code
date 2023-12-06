from __future__ import annotations

from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class GameRound(BaseModel):
    red: int
    blue: int
    green: int

    def is_round_possible(self, num_red: int, num_blue: int, num_green: int) -> bool:
        return self.red <= num_red and self.blue <= num_blue and self.green <= num_green


class Game(BaseModel):
    id: int
    rounds: list[GameRound]

    def is_game_possible(self, num_red: int, num_blue: int, num_green: int) -> bool:
        for r in self.rounds:
            if not r.is_round_possible(
                num_red=num_red, num_blue=num_blue, num_green=num_green
            ):
                return False

        return True

    def min_cubes_required_in_power(self) -> int:
        min_red = min_blue = min_green = 0

        for r in self.rounds:
            if r.red > min_red:
                min_red = r.red
            if r.blue > min_blue:
                min_blue = r.blue
            if r.green > min_green:
                min_green = r.green

        return min_red * min_blue * min_green


class GameCollection(BaseModel):
    games: list[Game]

    @staticmethod
    def from_puzzle_input(puzzle_input: str) -> GameCollection:
        games: list[Game] = []

        for line in puzzle_input.splitlines():
            game_id_info, rounds_info = line.split(":", maxsplit=1)

            # game_id_info = "Game 1"
            game_id = int(game_id_info.split(" ")[1])

            # rounds_info = " 1 red, 2 green, 6 blue; 3 green, 4 red, 5 blue"
            rounds_info_list: list[str] = rounds_info.split(";")
            rounds: list[GameRound] = []
            for individual_round_info in rounds_info_list:
                color_info = individual_round_info.split(",")
                num_red = num_green = num_blue = 0
                for individual_color_info in color_info:
                    # remove leading and trailing white spaces: " 1 red" -> "1 red"
                    individual_color_info = individual_color_info.strip()

                    # parse number in front of corresponding color: "1 red" -> 1
                    if "red" in individual_color_info:
                        num_red = int(individual_color_info.split(" ")[0])
                    elif "green" in individual_color_info:
                        num_green = int(individual_color_info.split(" ")[0])
                    elif "blue" in individual_color_info:
                        num_blue = int(individual_color_info.split(" ")[0])
                    else:
                        raise ValueError(
                            f"Invalid color: {individual_color_info}. Must be one of red, green, or blue."
                        )

                rounds.append(GameRound(red=num_red, green=num_green, blue=num_blue))

            games.append(Game(id=game_id, rounds=rounds))

        return GameCollection(games=games)


def main():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(day=2)

    game_collection = GameCollection.from_puzzle_input(puzzle_input=puzzle_input)
    print(game_collection)

    print("Part 1 - Games Possible: ", end="")
    sum_possible_game_ids = 0
    for g in game_collection.games:
        if g.is_game_possible(num_red=12, num_blue=14, num_green=13):
            print(f"{g.id} ", end="")
            sum_possible_game_ids += g.id
    print(f"\n{sum_possible_game_ids}")

    print("Part 2 - Min Cubes Required: ", end="")
    sum_min_cubes_powered = 0
    for g in game_collection.games:
        min_cubes_required_power = g.min_cubes_required_in_power()
        sum_min_cubes_powered += min_cubes_required_power
        print(f"{min_cubes_required_power} ", end="")
    print(f"\n{sum_min_cubes_powered}")


if __name__ == "__main__":
    main()
