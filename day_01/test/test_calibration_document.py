from day_01 import CalibrationDocument, CalibrationDocumentLineItem


def test_from_puzzle_input():
    puzzle_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    expected = CalibrationDocument(
        line_items=[
            CalibrationDocumentLineItem(contents="1abc2"),
            CalibrationDocumentLineItem(contents="pqr3stu8vwx"),
            CalibrationDocumentLineItem(contents="a1b2c3d4e5f"),
            CalibrationDocumentLineItem(contents="treb7uchet"),
        ]
    )

    result = CalibrationDocument.from_puzzle_input(puzzle_input=puzzle_input)

    assert result == expected
