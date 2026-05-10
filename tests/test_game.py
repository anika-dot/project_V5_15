import pytest
from skripts.Class_Game import Game
from skripts.Class_Fill import Field, Street, House, Business, Water, Car
import builtins
from skripts.Class_PlayGame import PlayGame


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

    game.board = [[Street() for _ in range(30)] for _ in range(30)]

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
def test_load_winterthur_map():
    game = Game()
    game.load_winterthur_map()
    assert len(game.board) == 30
    assert len(game.board[0]) == 30
    assert isinstance(game.board[0][0], (Field, Street, House, Business, Water, Car))


#---------------------------------------------------------------------------------------------
# Tests for Play.py


# Equivalence class 1: user selects Winterthur map (input = 1)
def test_user_choice_winterthur(monkeypatch):
    calls = {"winterthur": False, "random": False}

    def mock_input(prompt):
        return "1"

    def mock_play_winterthur(self):
        calls["winterthur"] = True

    def mock_play_random(self):
        calls["random"] = True

    monkeypatch.setattr(builtins, "input", mock_input)
    monkeypatch.setattr(PlayGame, "play_winterthur_map", mock_play_winterthur)
    monkeypatch.setattr(PlayGame, "play_random_map", mock_play_random)

    import skripts.Play

    assert calls["winterthur"] is True
    assert calls["random"] is False


# Equivalence class 2: user selects random map (input = 2)
def test_user_choice_random(monkeypatch):
    calls = {"winterthur": False, "random": False}

    def mock_input(prompt):
        return "2"

    def mock_play_winterthur(self):
        calls["winterthur"] = True

    def mock_play_random(self):
        calls["random"] = True

    monkeypatch.setattr(builtins, "input", mock_input)
    monkeypatch.setattr(PlayGame, "play_winterthur_map", mock_play_winterthur)
    monkeypatch.setattr(PlayGame, "play_random_map", mock_play_random)

    import skripts.Play

    assert calls["winterthur"] is False
    assert calls["random"] is True


# Equivalence class 3: invalid input (not 1 or 2)
def test_user_choice_invalid(monkeypatch):
    calls = {"winterthur": False, "random": False}

    def mock_input(prompt):
        return "3"

    def mock_play_winterthur(self):
        calls["winterthur"] = True

    def mock_play_random(self):
        calls["random"] = True

    monkeypatch.setattr(builtins, "input", mock_input)
    monkeypatch.setattr(PlayGame, "play_winterthur_map", mock_play_winterthur)
    monkeypatch.setattr(PlayGame, "play_random_map", mock_play_random)

    import skripts.Play

    assert calls["winterthur"] is False
    assert calls["random"] is False




#---------------------------------------------------------------------------------------------
# # Tests for Class_File.py

# import pytest
# from skripts.Class_File import File 

# # Equivalence class 1: file contains commas → commas should be removed
# def test_remove_commas_basic(tmp_path):
#     test_file = tmp_path / "test.txt"
#     test_file.write_text("Hello,World,Test")

#     File.remove_commas(test_file)

#     content = test_file.read_text()
#     assert content == "HelloWorldTest"


# # Equivalence class 2: file contains no commas → content unchanged
# def test_remove_commas_no_commas(tmp_path):
#     test_file = tmp_path / "test.txt"
#     test_file.write_text("Hello World Test")

#     File.remove_commas(test_file)

#     content = test_file.read_text()
#     assert content == "Hello World Test"


# # Equivalence class 3: empty file → stays empty
# def test_remove_commas_empty_file(tmp_path):
#     test_file = tmp_path / "test.txt"
#     test_file.write_text("")

#     File.remove_commas(test_file)

#     content = test_file.read_text()
#     assert content == ""


# # Equivalence class 4: file with only commas → becomes empty
# def test_remove_commas_only_commas(tmp_path):
#     test_file = tmp_path / "test.txt"
#     test_file.write_text(",,,")

#     File.remove_commas(test_file)

#     content = test_file.read_text()
#     assert content == ""


# # Equivalence class 5: file does not exist → should raise error
# def test_remove_commas_file_not_found():
#     with pytest.raises(FileNotFoundError):
#         File.remove_commas("non_existent_file.txt")


# ---------------------------------------------------------------------------------------------
# Tests for Class_PlayGame.py




# Equivalence class 1: pressing "q" stops the game
def test_on_press_q_stops_game():
    game = PlayGame()

    class MockKey:
        char = "q"

    game.on_press(MockKey())

    assert game.running is False


# Equivalence class 2: pressing another key does not stop the game
def test_on_press_other_key_keeps_running():
    game = PlayGame()

    class MockKey:
        char = "a"

    game.on_press(MockKey())

    assert game.running is True


# Equivalence class 3: special key without char attribute
def test_on_press_special_key():
    game = PlayGame()

    class MockSpecialKey:
        pass

    # should not crash
    game.on_press(MockSpecialKey())

    assert game.running is True


# Equivalence class 4: play_winterthur_map initializes values correctly
def test_play_winterthur_initialization(monkeypatch):
    game = PlayGame()

    # mock methods to avoid infinite loop
    monkeypatch.setattr(game, "load_winterthur_map", lambda: None)
    monkeypatch.setattr(game, "display_board", lambda: None)
    monkeypatch.setattr(game, "population_growth", lambda: None)
    monkeypatch.setattr(game, "simulate_traffic", lambda: None)
    monkeypatch.setattr(game, "check_population_safety", lambda: None)

    # stop loop immediately
    def stop_running():
        game.running = False

    monkeypatch.setattr(game, "display_board", stop_running)

    # mock keyboard listener
    class MockListener:
        def __init__(self, on_press):
            pass

        def start(self):
            pass

        def stop(self):
            pass

    monkeypatch.setattr(
        "skripts.Class_PlayGame.keyboard.Listener",
        MockListener
    )

    monkeypatch.setattr("time.sleep", lambda x: None)
    monkeypatch.setattr("os.system", lambda x: None)

    game.play_winterthur_map()

    assert game.counter == 1
    assert game.drivetime == 1


# Equivalence class 5: play_random_map initializes values correctly
def test_play_random_initialization(monkeypatch):
    game = PlayGame()

    # mock methods
    monkeypatch.setattr(game, "load_random_city", lambda: None)
    monkeypatch.setattr(game, "population_growth", lambda: None)
    monkeypatch.setattr(game, "simulate_traffic", lambda: None)
    monkeypatch.setattr(game, "check_population_safety", lambda: None)

    # stop loop immediately
    def stop_running():
        game.running = False

    monkeypatch.setattr(game, "display_board", stop_running)

    # mock keyboard listener
    class MockListener:
        def __init__(self, on_press):
            pass

        def start(self):
            pass

        def stop(self):
            pass

    monkeypatch.setattr(
        "skripts.Class_PlayGame.keyboard.Listener",
        MockListener
    )

    monkeypatch.setattr("time.sleep", lambda x: None)
    monkeypatch.setattr("os.system", lambda x: None)

    game.play_random_map()

    assert game.counter == 1
    assert game.drivetime == 1


# Equivalence class 6: figures list contains all expected classes
def test_figures_contains_correct_types():
    from skripts.Class_PlayGame import figures
    from skripts.Class_Fill import (
        Field, Water, House, Business, Street, Car
    )

    expected_types = [Field, Water, House, Business, Street, Car]

    for figure, expected in zip(figures, expected_types):
        assert isinstance(figure, expected)