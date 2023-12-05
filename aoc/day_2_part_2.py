from helpers.read_file import read_file
from aoc.day_2 import Game, BagConfiguration, parse_input

from dataclasses import dataclass
import math


@dataclass
class ExpandedGame(Game):
    def get_max_red_value(self) -> float:
        max_red: float = -math.inf

        for bag_configuration in self.sets:
            if bag_configuration.red > max_red:
                max_red = bag_configuration.red

        return max_red

    def get_max_blue_value(self) -> float:
        max_blue: float = -math.inf

        for bag_configuration in self.sets:
            if bag_configuration.blue > max_blue:
                max_blue = bag_configuration.blue

        return max_blue

    def get_max_green_value(self) -> float:
        max_green: float = -math.inf

        for bag_configuration in self.sets:
            if bag_configuration.green > max_green:
                max_green = bag_configuration.green

        return max_green


def get_power_sum(games: list[Game]) -> float:
    expanded_games: list[ExpandedGame] = [
        ExpandedGame(id=game.id, sets=game.sets) for game in games
    ]
    powers_sum: float = 0.0

    for game in expanded_games:
        max_red: float = game.get_max_red_value()
        max_blue: float = game.get_max_blue_value()
        max_green: float = game.get_max_green_value()

        powers_sum += max_red * max_blue * max_green

    return powers_sum


if __name__ == "__main__":
    puzzle_input: str = read_file("./inputs/day_2.txt")
    games: list[Game] = parse_input(puzzle_input)
    bag_configuration = BagConfiguration(
        red=12,
        green=13,
        blue=14,
    )
    power_sum: float = get_power_sum(games)
    print(int(power_sum))
