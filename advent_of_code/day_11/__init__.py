import itertools
from copy import deepcopy

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class GalaxyDistanceDeterminer:
    empty_x: set[int]
    empty_y: set[int]
    expansion_factor: int

    def __init__(
        self,
        empty_x: set[int],
        empty_y: set[int],
    ):
        self.empty_x = empty_x
        self.empty_y = empty_y

    def get_distance_between_galaxies(
        self,
        g1: tuple[int, int],
        g2: tuple[int, int],
        expansion_factor: int = 1,  # used in part 2
    ):
        num_expanded_x = 0
        for x in self.empty_x:
            if min(g1[0], g2[0]) < x < max(g1[0], g2[0]):
                num_expanded_x += 1

        num_expanded_y = 0
        for y in self.empty_y:
            if min(g1[1], g2[1]) < y < max(g1[1], g2[1]):
                num_expanded_y += 1

        expansion = (num_expanded_x + num_expanded_y) * expansion_factor
        manhattan_distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

        return manhattan_distance + expansion


def parse_puzzle_input(
    puzzle_input: str,
) -> tuple[list[tuple[int, int]], GalaxyDistanceDeterminer]:
    max_y = len(puzzle_input.splitlines())
    max_x = len(puzzle_input.splitlines()[0])

    empty_y = set(range(max_y))
    empty_x = set(range(max_x))

    y = 0
    galaxies: list[tuple[int, int]] = []
    for line in puzzle_input.splitlines():
        x = line.find("#")
        while x != -1:
            galaxies.append((x, y))
            empty_x.discard(x)
            empty_y.discard(y)
            x = line.find("#", x + 1)

        y += 1

    return galaxies, GalaxyDistanceDeterminer(empty_x=empty_x, empty_y=empty_y)


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=11)
    galaxies, distance_determiner = parse_puzzle_input(puzzle_input=puzzle_input)

    total_distance_part_1 = 0
    total_distance_part_2 = 0
    galaxy_pairs = itertools.combinations(galaxies, 2)
    while True:
        try:
            galaxy_pair = next(galaxy_pairs)
            g1, g2 = galaxy_pair
            total_distance_part_1 += distance_determiner.get_distance_between_galaxies(
                g1=g1, g2=g2
            )
            total_distance_part_2 += distance_determiner.get_distance_between_galaxies(
                g1=g1, g2=g2, expansion_factor=1000000
            )
        except StopIteration:
            break

    print(f"Part 1 distance: {total_distance_part_1}")
    print(f"Part 2 distance: {total_distance_part_2}")


if __name__ == "__main__":
    print("Part 2 is incorrect.")  # the answer I'm getting for part 2 is incorrect.
    main()
