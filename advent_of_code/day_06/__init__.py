from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


def calculate_distance(button_held_duration: int, total_time: int):
    boat_speed = button_held_duration * 1
    remaining_time = total_time - button_held_duration
    distance_traveled = boat_speed * remaining_time

    return distance_traveled


def does_player_win(button_held_duration: int, total_time: int, distance_to_beat: int):
    distance_traveled = calculate_distance(button_held_duration, total_time)

    return distance_traveled > distance_to_beat


def find_min_button_duration_to_win(
    total_time: int,
    distance_to_beat: int,
) -> int:
    index = 1

    while not does_player_win(index, total_time, distance_to_beat):
        index += 1

    return index


def find_max_button_duration_to_win(
    total_time: int,
    distance_to_beat: int,
) -> int:
    index = total_time - 1

    while not does_player_win(index, total_time, distance_to_beat):
        index -= 1

    return index


def find_min_and_max_button_duration_to_win(
    total_time: int,
    distance_to_beat: int,
) -> tuple[int, int]:
    min_button_duration = find_min_button_duration_to_win(
        total_time=total_time,
        distance_to_beat=distance_to_beat,
    )
    max_button_duration = find_max_button_duration_to_win(
        total_time=total_time,
        distance_to_beat=distance_to_beat,
    )

    return min_button_duration, max_button_duration


def find_number_of_ways_to_win(
    total_time: int,
    distance_to_beat: int,
) -> int:
    min_button_duration, max_button_duration = find_min_and_max_button_duration_to_win(
        total_time=total_time,
        distance_to_beat=distance_to_beat,
    )

    return max_button_duration - min_button_duration + 1


class RaceInfo(BaseModel):
    total_time: int
    distance_to_beat: int


def get_race_info_part_1(puzzle_input: str) -> list[RaceInfo]:
    lines = puzzle_input.splitlines()

    total_times = [int(s) for s in lines[0].split("Time:", 1)[1].split()]
    distances_to_beat = [int(s) for s in lines[1].split("Distance:", 1)[1].split()]

    return [
        RaceInfo(total_time=total_time, distance_to_beat=distance_to_beat)
        for total_time, distance_to_beat in zip(total_times, distances_to_beat)
    ]


def get_race_info_part_2(puzzle_input: str) -> RaceInfo:
    lines = puzzle_input.splitlines()

    total_time = int(lines[0].split("Time:", 1)[1].replace(" ", ""))
    distance_to_beat = int(lines[1].split("Distance:", 1)[1].replace(" ", ""))

    return RaceInfo(total_time=total_time, distance_to_beat=distance_to_beat)


def main():
    puzzle_repo = OfflinePuzzleInputRepository()
    puzzle_input = puzzle_repo.get_puzzle_input(day=6)

    race_infos_part_1 = get_race_info_part_1(puzzle_input)
    part_1_answer = 1
    for race_info in race_infos_part_1:
        part_1_answer *= find_number_of_ways_to_win(
            total_time=race_info.total_time,
            distance_to_beat=race_info.distance_to_beat,
        )

    print(f"Part 1: {part_1_answer}")

    race_info_part_2 = get_race_info_part_2(puzzle_input)
    part_2_answer = find_number_of_ways_to_win(
        total_time=race_info_part_2.total_time,
        distance_to_beat=race_info_part_2.distance_to_beat,
    )

    print(f"Part 2: {part_2_answer}")


if __name__ == "__main__":
    main()
