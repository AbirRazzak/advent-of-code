from __future__ import annotations

import itertools

from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class AlmanacMapItem(BaseModel):
    destination_range_start: int
    source_range_start: int
    range_length: int

    def is_number_in_range(self, number: int) -> bool:
        return (
            self.source_range_start
            <= number
            < self.source_range_start + self.range_length
        )

    def get_destination_for_number(self, number: int) -> int:
        if not self.is_number_in_range(number=number):
            raise ValueError(
                f"{number} is not a valid number within the range of {self.source_range_start}, {self.range_length}"
            )

        return self.destination_range_start + (number - self.source_range_start)


class AlmanacMap(BaseModel):
    items: list[AlmanacMapItem]
    number_to_destination_cache: dict[int, int] = {}

    def get_destination_for_number(self, number: int) -> int:
        # if number in self.number_to_destination_cache:
        #     return self.number_to_destination_cache[number]

        for i in self.items:
            if i.is_number_in_range(number=number):
                destination = i.get_destination_for_number(number=number)
                # self.number_to_destination_cache[number] = destination
                return destination

        return number


class Almanac(BaseModel):
    seeds: list[int]  # used in part 1
    seed_pairs: list[tuple[int, int]]  # used in part 2
    seed_to_soil_map: AlmanacMap
    soil_to_fertilizer_map: AlmanacMap
    fertilizer_to_water_map: AlmanacMap
    water_to_light_map: AlmanacMap
    light_to_temperature_map: AlmanacMap
    temperature_to_humidity_map: AlmanacMap
    humidity_to_location_map: AlmanacMap

    @staticmethod
    def from_puzzle_input(puzzle: str) -> Almanac:
        seeds: list[int] = []
        seed_pairs: list[tuple[int, int]] = []
        almanac_lists: list[list[AlmanacMapItem]] = [[], [], [], [], [], [], []]
        almanac_list_index = -1

        for line in puzzle.splitlines():
            if line.startswith("seeds: "):
                seeds_str = line.split(": ", maxsplit=1)[1]
                seeds = [int(x) for x in seeds_str.split()]
                seed_pairs = itertools.batched(seeds, 2)

            elif line == "":
                # first blank line should be after the seeds line, so index would be 0
                almanac_list_index += 1

            elif "map" in line:
                pass

            else:
                line_items = [int(x) for x in line.split()]
                almanac_lists[almanac_list_index].append(
                    AlmanacMapItem(
                        destination_range_start=line_items[0],
                        source_range_start=line_items[1],
                        range_length=line_items[2],
                    )
                )

        return Almanac(
            seeds=seeds,
            seed_pairs=seed_pairs,
            seed_to_soil_map=AlmanacMap(items=almanac_lists[0]),
            soil_to_fertilizer_map=AlmanacMap(items=almanac_lists[1]),
            fertilizer_to_water_map=AlmanacMap(items=almanac_lists[2]),
            water_to_light_map=AlmanacMap(items=almanac_lists[3]),
            light_to_temperature_map=AlmanacMap(items=almanac_lists[4]),
            temperature_to_humidity_map=AlmanacMap(items=almanac_lists[5]),
            humidity_to_location_map=AlmanacMap(items=almanac_lists[6]),
        )

    def get_location_for_seed(self, seed: int) -> int:
        soil = self.seed_to_soil_map.get_destination_for_number(number=seed)
        fertilizer = self.soil_to_fertilizer_map.get_destination_for_number(number=soil)
        water = self.fertilizer_to_water_map.get_destination_for_number(
            number=fertilizer
        )
        light = self.water_to_light_map.get_destination_for_number(number=water)
        temperature = self.light_to_temperature_map.get_destination_for_number(
            number=light
        )
        humidity = self.temperature_to_humidity_map.get_destination_for_number(
            number=temperature
        )
        location = self.humidity_to_location_map.get_destination_for_number(
            number=humidity
        )

        return location

    def get_locations_for_seeds(self) -> dict[int, int]:
        location_to_seed_mapping: dict[int, int] = {}

        for s in self.seeds:
            location = self.get_location_for_seed(seed=s)
            location_to_seed_mapping[location] = s

        print(location_to_seed_mapping)
        return location_to_seed_mapping

    def get_lowest_location_with_a_seed(self) -> int:
        location_to_seed_mapping = self.get_locations_for_seeds()

        lowest_location = min(location_to_seed_mapping.keys())

        return lowest_location

    def get_lowest_location_with_a_seed_from_pairs(self) -> int:
        lowest_location: int = -1
        seeds_to_check: set[int] = set()

        # for starting_number, number_range in self.seed_pairs:
        #     for number in range(starting_number, starting_number + number_range):
        #         seeds_to_check.add(number)
        #         print(seeds_to_check)
        #
        # print(seeds_to_check)
        #
        # for number in seeds_to_check:
        #     location = self.get_location_for_seed(seed=number)
        #
        #     if lowest_location == -1 or location < lowest_location:
        #         lowest_location = location

        for starting_number, number_range in self.seed_pairs:
            location_map = map(
                self.get_location_for_seed,
                range(starting_number, starting_number + number_range),
            )
            while True:
                try:
                    location = next(location_map)
                    # print(f"{location}; lowest: {lowest_location}")

                    if lowest_location == -1 or location < lowest_location:
                        lowest_location = location

                except StopIteration:
                    continue

        return lowest_location


def main():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(day=5)

    almanac = Almanac.from_puzzle_input(puzzle=puzzle_input)
    print(almanac)

    print(
        f"Part 1 - Seed with lowest location: {almanac.get_lowest_location_with_a_seed()}"
    )

    print(
        f"Part 2 - Seed with lowest location (from pairs): {almanac.get_lowest_location_with_a_seed_from_pairs()}"
    )


if __name__ == "__main__":
    main()
