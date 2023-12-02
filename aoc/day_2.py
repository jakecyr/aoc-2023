from enum import Enum, auto
from helpers.read_file import read_file
from dataclasses import dataclass


class Colors(Enum):
    BLUE = auto()
    RED = auto()
    GREEN = auto()


@dataclass
class BagConfiguration:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    id: int
    sets: list[BagConfiguration]


def get_possible_games(
    bag_configuration: BagConfiguration, games: list[Game]
) -> list[Game]:
    possible_games: list[Game] = []

    for game in games:
        failed = False
        for game_set in game.sets:
            if game_set.red > bag_configuration.red:
                failed = True
                break
            elif game_set.blue > bag_configuration.blue:
                failed = True
                break
            elif game_set.green > bag_configuration.green:
                failed = True
                break

        if not failed:
            possible_games.append(game)

    return possible_games


def get_sum_of_game_ids(games: list[Game]) -> int:
    sum = 0
    for game in games:
        sum += game.id
    return sum


def parse_sets_strs(sets_strs: list[str]) -> list[BagConfiguration]:
    sets: list[BagConfiguration] = []

    for sets_str in sets_strs:
        if not sets_str.strip():
            continue

        configuration = BagConfiguration()
        set_colors: list[str] = sets_str.strip().split(",")

        for color in set_colors:
            count, color = color.strip().split(" ")
            if color == "red":
                configuration.red = int(count)
            elif color == "blue":
                configuration.blue = int(count)
            elif color == "green":
                configuration.green = int(count)

        sets.append(configuration)

    return sets


def parse_input(puzzle_input: str) -> list[Game]:
    lines: list[str] = puzzle_input.split("\n")
    games: list[Game] = []

    for line in lines:
        if not line.strip():
            continue
        game_info, sets_str = line.split(":")
        game_id = int(game_info.replace("Game ", ""))
        sets_strs: list[str] = sets_str.split(";")
        sets: list[BagConfiguration] = parse_sets_strs(sets_strs)
        game = Game(id=game_id, sets=sets)
        games.append(game)

    return games


if __name__ == "__main__":
    puzzle_input: str = read_file("./inputs/day_2.txt")
    games: list[Game] = parse_input(puzzle_input)
    bag_configuration = BagConfiguration(
        red=12,
        green=13,
        blue=14,
    )
    possible_games: list[Game] = get_possible_games(bag_configuration, games)
    sum_of_ids: int = get_sum_of_game_ids(possible_games)
    print(f"Answer: {sum_of_ids}")
