import abc
import os


class PuzzleInputRepository(abc.ABC):
    @abc.abstractmethod
    def get_puzzle_input(self, day: int, year: int = 2023) -> str:
        pass


class OfflinePuzzleInputRepository(PuzzleInputRepository):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.puzzle_input_dir = os.path.join(current_dir, "data")

    def get_puzzle_input(self, day: int, year: int = 2023) -> str:
        file_path = os.path.join(self.puzzle_input_dir, f"{year}", f"day_{day}.txt")
        with open(file_path, "r") as f:
            return f.read()
