from helpers.read_file import read_file
import re

possible_digits: dict[str, int] = {
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


def get_first_digit_in_line(line: str, reversed: bool = False) -> str | None:
    found_digits = []
    for name, number in possible_digits.items():
        if reversed:
            name = name[::-1]
        if name in line:
            found_digits.append((name, number, line.index(name)))

    if found_digits:
        found_digits.sort(key=lambda x: x[2])
        return found_digits[0][0]
    return None


def get_calibration_sum(puzzle_input: str) -> int:
    lines: list[str] = puzzle_input.split("\n")
    sum = 0

    for line in lines:
        if not line.strip():
            continue

        print(line)

        first_digit_name: str | None = get_first_digit_in_line(line)
        print("First digit name:", first_digit_name)
        if first_digit_name:
            line = line.replace(
                first_digit_name, str(possible_digits[first_digit_name]), 1
            )

        reversed_line: str = line[::-1]

        print("Reversed line:", reversed_line)
        last_digit_name: str | None = get_first_digit_in_line(reversed_line, True)
        print("Last digit name:", last_digit_name)
        if last_digit_name:
            reversed_line = reversed_line.replace(
                last_digit_name, str(possible_digits[last_digit_name[::-1]]), 1
            )

        line = reversed_line[::-1]

        print("Un-reversed Line:", line)

        digits: str = re.sub(r"[^0-9]", "", line)

        if len(digits) < 1:
            continue

        num: str = digits[0] + digits[-1]
        print("Num:", num)
        sum += int(num)

    return sum


if __name__ == "__main__":
    puzzle_input: str = read_file("./inputs/day_1.txt")
    print(get_calibration_sum(puzzle_input))
