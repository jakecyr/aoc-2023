from helpers.read_file import read_file
import re

possible_digits: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_sum(puzzle_input: str) -> int:
    lines: list[str] = puzzle_input.split("\n")
    sum = 0

    for line in lines:
        if not line.strip():
            continue

        for digit, num in possible_digits.items():
            if digit in line:
                replace_with: str = digit + num + digit
                line = line.replace(digit, str(replace_with))

        digits: str = re.sub(r"[^0-9]", "", line)

        if len(digits) < 1:
            continue

        calibration_number: str = digits[0] + digits[-1]
        sum += int(calibration_number)

    return sum


if __name__ == "__main__":
    puzzle_input: str = read_file("./inputs/day_1.txt")
    print(get_calibration_sum(puzzle_input))
