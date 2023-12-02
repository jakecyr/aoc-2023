from aoc import day_1


def test_get_calibration_sum_with_all_digit_lines() -> None:
    puzzle_input = """
    1122
    1111
    1234
    91212129
    """
    assert day_1.get_calibration_sum(puzzle_input) == 136


def test_get_calibration_sum_with_no_digit_lines() -> None:
    puzzle_input = """
    abcdef
    """
    assert day_1.get_calibration_sum(puzzle_input) == 0


def test_get_calibration_sum_with_one_digit_line() -> None:
    puzzle_input = """
    11
    """
    assert day_1.get_calibration_sum(puzzle_input) == 11


def test_get_calibration_sum_with_two_digit_lines() -> None:
    puzzle_input = """
    11
    11
    """
    assert day_1.get_calibration_sum(puzzle_input) == 22


def test_get_calibration_sum_with_alpha_numeric_lines() -> None:
    puzzle_input = """
    abcdef
    1asidjs23jdfj0
    1122
    """
    assert day_1.get_calibration_sum(puzzle_input) == 22
