from helpers.read_file import read_file
import re


def get_calibration_sum(puzzle_input: str) -> int:
    lines: list[str] = puzzle_input.split("\n")
    sum = 0

    for line in lines:
        if not line.strip():
            continue
        digits: str = re.sub(r"[^0-9]", "", line)

        if len(digits) < 1:
            continue

        num: str = digits[0] + digits[-1]
        sum += int(num)

    return sum


if __name__ == "__main__":
    puzzle_input: str = read_file("./inputs/day_1.txt")
    print(get_calibration_sum(puzzle_input))
