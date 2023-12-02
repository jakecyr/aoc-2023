from aoc import day_2


def test_parse_sets_strs_returns_expected_count() -> None:
    sets_str = "4 red, 3 green; 2 blue, 4 red, 5 green; 3 red, 3 green"
    sets: list[day_2.BagConfiguration] = day_2.parse_sets_strs(sets_str.split(";"))
    assert len(sets) == 3


def test_parse_set_strs_returns_expected_configurations() -> None:
    sets_str = "4 red, 3 green; 2 blue, 4 red, 5 green; 3 red, 3 green"
    sets: list[day_2.BagConfiguration] = day_2.parse_sets_strs(sets_str.split(";"))
    assert sets[0].red == 4
    assert sets[0].green == 3
    assert sets[0].blue == 0
    assert sets[1].red == 4
    assert sets[1].green == 5
    assert sets[1].blue == 2
    assert sets[2].red == 3
    assert sets[2].green == 3
    assert sets[2].blue == 0


def test_parse_input_returns_expected_number_of_games() -> None:
    input_str = "Game 70: 1 blue, 3 green, 2 red; 1 green, 2 blue; 5 green, 1 red; 2 blue, 4 green; 1 red, 5 green"
    games: list[day_2.Game] = day_2.parse_input(input_str)
    assert len(games) == 1


def test_parse_input_with_multiple_games_returns_expected_number_of_games() -> None:
    input_str = """Game 70: 1 blue, 3 green, 2 red; 1 green, 2 blue; 5 green, 1 red; 2 blue, 4 green; 1 red, 5 gree
Game 71: 1 blue, 3 green, 2 red; 1 green, 2 blue; 5 green, 1 red; 2 blue, 4 green; 1 red, 5 green"""
    games: list[day_2.Game] = day_2.parse_input(input_str)
    assert len(games) == 2


def test_parse_inout_returns_games_with_expected_configuration() -> None:
    input_str = "Game 70: 1 blue, 3 green, 2 red; 1 green, 2 blue; 5 green, 1 red; 2 blue, 4 green; 1 red, 5 green"
    games: list[day_2.Game] = day_2.parse_input(input_str)
    assert games[0].sets[0].blue == 1
    assert games[0].sets[0].green == 3
    assert games[0].sets[0].red == 2
    assert games[0].sets[1].blue == 2
    assert games[0].sets[1].green == 1
    assert games[0].sets[1].red == 0
    assert games[0].sets[2].blue == 0
    assert games[0].sets[2].green == 5
    assert games[0].sets[2].red == 1
    assert games[0].sets[3].blue == 2
    assert games[0].sets[3].green == 4
    assert games[0].sets[3].red == 0
    assert games[0].sets[4].blue == 0
    assert games[0].sets[4].green == 5
    assert games[0].sets[4].red == 1


def test_get_possible_games_returns_expected_list_of_games() -> None:
    bag_configuration = day_2.BagConfiguration(red=4, green=3, blue=2)
    games: list[day_2.Game] = [
        day_2.Game(id=1, sets=[day_2.BagConfiguration(red=4, green=3, blue=2)]),
        day_2.Game(id=2, sets=[day_2.BagConfiguration(red=2, green=5, blue=1)]),
        day_2.Game(id=3, sets=[day_2.BagConfiguration(red=4, green=3, blue=0)]),
    ]
    possible_games: list[day_2.Game] = day_2.get_possible_games(
        bag_configuration,
        games,
    )
    assert len(possible_games) == 2


def test_gets_correct_answer_from_string() -> None:
    input_string = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """

    games: list[day_2.Game] = day_2.parse_input(input_string)

    assert len(games) == 5

    bag_configuration = day_2.BagConfiguration(
        red=12,
        green=13,
        blue=14,
    )
    possible_games: list[day_2.Game] = day_2.get_possible_games(
        bag_configuration,
        games,
    )

    assert len(possible_games) == 3
    assert possible_games[0].id == 1
    assert possible_games[1].id == 2
    assert possible_games[2].id == 5

    id_sum: int = day_2.get_sum_of_game_ids(possible_games)

    assert id_sum == 8
