from aoc import day_1_part_2


def test_get_calibration_sum_with_all_digit_lines() -> None:
    puzzle_input = """
    1122
    1111
    1234
    91212129
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 136


def test_get_calibration_sum_with_spelled_out_digits() -> None:
    puzzle_input = """
    oneljfef789two
    1ddfhjsu3ahdfu23
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 25


def test_get_calibration_sum_with_spelled_overlapping_digits() -> None:
    puzzle_input = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 281


def test_empty_lines() -> None:
    puzzle_input = """
    
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 0


def test_lines_with_only_words() -> None:
    puzzle_input = """
    hello world
    python coding
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 0


def test_lines_with_single_digits() -> None:
    puzzle_input = """
    1abc
    xyz2
    3xyz4
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 67


def test_non_overlapping_spelled_out_digits() -> None:
    puzzle_input = """
    onexyzthree
    twoabcseven
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 40


def test_lines_with_special_characters_and_digits() -> None:
    puzzle_input = """
    1!@#$%^&*()2
    three#$$%four
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 46


def test_lines_with_digits_in_the_middle() -> None:
    puzzle_input = """
    axb5c6dz
    eyf7gh8i
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 134


def test_lines_with_more_than_one_digit_occurring() -> None:
    puzzle_input = """
    4five8ffive
    """
    assert day_1_part_2.get_calibration_sum(puzzle_input) == 45
