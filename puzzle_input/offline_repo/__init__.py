import abc
import os


class PuzzleInputRepository(abc.ABC):
    @abc.abstractmethod
    def get_puzzle_input(self, day: int, year: int = 2023) -> str:
        pass


class OfflinePuzzleInputRepository(PuzzleInputRepository):
    def __init__(self):
        self.puzzle_input_dir = "puzzle_input/offline_repo/data"

    def get_puzzle_input(self, day: int, year: int = 2023) -> str:
        file_path = os.path.join(self.puzzle_input_dir, f"{year}", f"day_{day}.txt")
        with open(file_path, "r") as f:
            return f.read()
