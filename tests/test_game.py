import pytest
from skripts.Class_Game import Game
from skripts.Class_Fill import Field, Street, House, Business, Water, Car


# Equivalence class 1: fill_field mapping
def test_fill_field_creates_field():
    game = Game()
    game.lines = ["G"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], Field)


def test_fill_field_creates_street():
    game = Game()
    game.lines = ["S"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], Street)


def test_fill_field_creates_house():
    game = Game()
    game.lines = ["R"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], House)


# Equivalence class 2: population growth
def test_population_growth_increases_population():
    game = Game()
    house = House()
    house.bewohner = 1

    game.board = [[house]]

    game.population_growth()

    assert game.board[0][0].bewohner > 1



# Equivalence class 3: edge case - house dies
def test_population_house_turns_into_field():
    game = Game()
    house = House()
    house.bewohner = 0

    game.board = [[house]]

    game.population_growth()

    assert isinstance(game.board[0][0], Field)


# Equivalence class 4: edge case - empty board
def test_population_growth_empty_board():
    game = Game()
    game.board = []

    game.population_growth()  # should not crash



# Equivalence class 5: traffic simulation (deterministic!)
def test_simulate_traffic_places_car_on_street():
    game = Game()

    # minimal board instead of 30x30
    game.board = [[Street(), Street()],
                  [Street(), Street()]]

    game.drivetime = 1

    game.simulate_traffic()

    found_car = any(isinstance(cell, Car) for row in game.board for cell in row)

    assert found_car


# Equivalence class 6: display output
def test_display_board_prints_character(capsys):
    game = Game()
    game.board = [[Field()]]

    game.display_board()

    captured = capsys.readouterr()

    assert "." in captured.out


# Equivalence class 7: deterministic random city
def test_random_city_deterministic(monkeypatch):
    game = Game()

    # force random to always return 0 → always Field
    monkeypatch.setattr("random.randrange", lambda x: 0)

    game.load_random_city()

    for row in game.board:
        for cell in row:
            assert isinstance(cell, Field)


# Equivalence class 8: invalid input handling
def test_population_with_invalid_cell_raises():
    game = Game()
    game.board = [[None]]

    with pytest.raises(AttributeError):
        game.population_growth()


# Equivalence class 9: load board from file
def test_load_board_winterthur():
    game = load_board_winterthur()
    assert len(game.board) == 30
    assert len(game.board[0]) == 30
    assert isinstance(game.board[0][0], (Field, Street, House, Business, Water, Car))