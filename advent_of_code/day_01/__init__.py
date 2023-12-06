from __future__ import annotations

from pydantic import BaseModel

from advent_of_code.puzzle_input.offline_repo import OfflinePuzzleInputRepository


class CalibrationDocumentLineItem(BaseModel):
    contents: str

    def _convert_calibration_digits_to_value(
        self, calibration_digits_by_index: dict[int, int]
    ) -> int:
        indices = calibration_digits_by_index.keys()
        first_index = min(indices)
        last_index = max(indices)

        first_digit = calibration_digits_by_index[first_index]
        second_digit = calibration_digits_by_index[last_index]

        return int(f"{first_digit}{second_digit}")

    def _fetch_numbers_from_contents_by_index(self) -> dict[int, int]:
        numbers_by_index: dict[int, int] = {}

        for i in range(len(self.contents)):
            current_char = self.contents[i]

            try:
                current_char_as_int = int(current_char)
                numbers_by_index[i] = current_char_as_int

            except ValueError:
                pass

        return numbers_by_index

    def _fetch_words_from_contents_by_index(self) -> dict[int, int]:
        numbers_by_index: dict[int, int] = {}

        spelled_out_numbers_to_value: dict[str, int] = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        for word in spelled_out_numbers_to_value.keys():
            word_index = 0

            while word_index != -1:
                word_index = self.contents.find(
                    word, word_index
                )  # search for the word in the substring of the last time the word was found to the end of the string

                if word_index != -1:
                    numbers_by_index[word_index] = spelled_out_numbers_to_value[word]
                    word_index += 1  # bump the starting index to the next character after the word was found

        return numbers_by_index

    def get_calibration_value(self) -> int:
        calibration_digits_by_index: dict[int, int] = {}

        # Get all the numbers from the contents
        numbers_by_index = self._fetch_numbers_from_contents_by_index()
        calibration_digits_by_index.update(numbers_by_index)

        # Get all the word numbers from the contents
        words_by_index = self._fetch_words_from_contents_by_index()
        calibration_digits_by_index.update(words_by_index)

        calibration_value = self._convert_calibration_digits_to_value(
            calibration_digits_by_index=calibration_digits_by_index
        )
        return calibration_value


class CalibrationDocument(BaseModel):
    line_items: list[CalibrationDocumentLineItem]

    @staticmethod
    def from_puzzle_input(puzzle_input: str) -> CalibrationDocument:
        line_items = []

        for line in puzzle_input.splitlines():
            line_items.append(CalibrationDocumentLineItem(contents=line))

        return CalibrationDocument(line_items=line_items)


def main():
    input_repo = OfflinePuzzleInputRepository()
    puzzle_input = input_repo.get_puzzle_input(day=1)

    document = CalibrationDocument.from_puzzle_input(puzzle_input=puzzle_input)

    line_item_calibration_values_sum = 0

    for line_item in document.line_items:
        calibration_value = line_item.get_calibration_value()
        print(f"{line_item.contents} -> {calibration_value}")
        line_item_calibration_values_sum += calibration_value

    print(line_item_calibration_values_sum)


if __name__ == "__main__":
    main()
