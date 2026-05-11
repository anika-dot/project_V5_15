import builtins
import pytest
from skripts.Class_Game import Game
from skripts.Class_Fill import Field, Street, House, Business, Water, Car
from skripts.Class_PlayGame import PlayGame
from skripts.Class_PlayGame import figures



# Equivalence class 1: fill_field mapping
def test_fill_field_creates_field():
    '''
    Test that fill_field creates the correct object type based on the input character.
    '''
    game = Game()
    game.lines = ["G"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], Field)


def test_fill_field_creates_street():
    '''
    Test that fill_field creates a Street object when the input character is "S".
    '''
    game = Game()
    game.lines = ["S"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], Street)


def test_fill_field_creates_house():
    '''
    Test that fill_field creates a House object when the input character is "R".
    '''
    game = Game()
    game.lines = ["R"]
    game.board = [[]]

    game.fill_field(0, 0)

    assert isinstance(game.board[0][0], House)


# Equivalence class 2: population growth
def test_population_growth_increases_population():
    '''
    Test that population_growth increases the number of inhabitants
    in a house with at least 1 inhabitant.
    '''
    game = Game()
    house = House()
    house.bewohner = 1

    game.board = [[house]]

    game.population_growth()

    assert game.board[0][0].bewohner > 1



# Equivalence class 3: edge case - house dies
def test_population_house_turns_into_field():
    '''
    Test that a house with 0 inhabitants turns into a Field.
    '''
    game = Game()
    house = House()
    house.bewohner = 0

    game.board = [[house]]

    game.population_growth()

    assert isinstance(game.board[0][0], Field)


# Equivalence class 4: edge case - empty board
def test_population_growth_empty_board():
    '''
    Test that population_growth does not crash on an empty board.
    '''
    game = Game()
    game.board = []

    game.population_growth()  # should not crash



# Equivalence class 5: traffic simulation (deterministic!)
def test_simulate_traffic_places_car_on_street():
    '''
    Test that simulate_traffic places a Car on a Street cell after one drivetime.
    '''
    game = Game()
    game.board = [[Street() for _ in range(30)] for _ in range(30)]
    game.drivetime = 1
    game.simulate_traffic()
    found_car = any(isinstance(cell, Car) for row in game.board for cell in row)

    assert found_car


# Equivalence class 6: display output
def test_display_board_prints_character(capsys):
    '''
    Test that display_board prints the expected character for a Field cell.
    '''
    game = Game()
    game.board = [[Field()]]

    game.display_board()

    captured = capsys.readouterr()

    assert "." in captured.out


# Equivalence class 7: deterministic random city
def test_random_city_deterministic(monkeypatch):
    '''
    Test that load_random_city creates a board of Fields when random is forced to return 0.
    '''
    game = Game()

    # force random to always return 0 → always Field
    monkeypatch.setattr("random.randrange", lambda x: 0)

    game.load_random_city()

    for row in game.board:
        for cell in row:
            assert isinstance(cell, Field)


# Equivalence class 8: invalid input handling
def test_population_with_invalid_cell_raises():
    '''
    Test that population_growth raises an error,
    if the board contains an invalid cell type (e.g. None).
    '''
    game = Game()
    game.board = [[None]]

    with pytest.raises(AttributeError):
        game.population_growth()


# Equivalence class 9: load board from file
def test_load_winterthur_map():
    '''
    Test that load_winterthur_map loads a 30x30 board with valid cell types.
    '''
    game = Game()
    game.load_winterthur_map()
    assert len(game.board) == 30
    assert len(game.board[0]) == 30
    assert isinstance(game.board[0][0], (Field, Street, House, Business, Water, Car))


# Tests for Play.py ---------------------------------------


# Equivalence class 1: user selects Winterthur map (input = 1)
def test_user_choice_winterthur(monkeypatch):
    '''
    Test that selecting "1" calls play_winterthur_map and not play_random_map.
    '''
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
    '''
    Test that selecting "2" calls play_random_map and not play_winterthur_map.
    '''
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

    assert calls["winterthur"] is False
    assert calls["random"] is True


# Equivalence class 3: invalid input (not 1 or 2)
def test_user_choice_invalid(monkeypatch):
    '''
    Test that invalid input does not call either play_winterthur_map or play_random_map.
    '''
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



# Tests for Class_PlayGame.py---------------------------------------


# Equivalence class 1: pressing "q"
def test_on_press_q_stops_game():
    '''
    Test that pressing "q" stops the game.
    '''
    game = PlayGame()

    class MockKey:
        '''
        Mock key with a char attribute that is "q", to test that on_press sets running to False.'''
        char = "q"

    game.on_press(MockKey())

    assert game.running is False


# Equivalence class 2: pressing another key
def test_on_press_other_key_keeps_game_running():
    '''
    Test that pressing another key does not stop the game.
    '''
    game = PlayGame()

    class MockKey:
        '''
        Mock key with a char attribute that is not "q", 
        to test that on_press does not stop the game.
        '''
        char = "a"

    game.on_press(MockKey())

    assert game.running is True


# Equivalence class 3: special key without char attribute
def test_on_press_special_key_does_not_crash():
    '''
    Test that pressing a special key without a char attribute does not crash the game.
    '''
    game = PlayGame()

    class MockSpecialKey:
        '''
        Mock special key that does not have a char attribute,
        to test that on_press handles it gracefully.'''
        pass

    game.on_press(MockSpecialKey())

    assert game.running is True


# Equivalence class 4: play_winterthur_map initialization
def test_play_winterthur_map_initializes_values(monkeypatch):
    '''
    Test that play_winterthur_map initializes counter and drivetime correctly.
    '''
    game = PlayGame()

    monkeypatch.setattr(game, "load_winterthur_map", lambda: None)
    monkeypatch.setattr(game, "population_growth", lambda: None)
    monkeypatch.setattr(game, "simulate_traffic", lambda: None)
    monkeypatch.setattr(game, "check_population_safety", lambda: None)

    def mock_display_board():
        game.running = False

    monkeypatch.setattr(game, "display_board", mock_display_board)

    class MockListener:
        '''
        Mock keyboard listener that does nothing, but is needed for testing.'''
        def __init__(self, on_press):
            pass

        def start(self):
            '''
            Mock start method that does nothing, but is needed for testing.
            '''
            pass

        def stop(self):
            '''
            Mock stop method that does nothing, but is needed for testing.
            '''
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


# Equivalence class 5: play_random_map initialization
def test_play_random_map_initializes_values(monkeypatch):
    '''
    Test that play_random_map initializes counter and drivetime correctly.
    '''
    game = PlayGame()

    monkeypatch.setattr(game, "load_random_city", lambda: None)
    monkeypatch.setattr(game, "population_growth", lambda: None)
    monkeypatch.setattr(game, "simulate_traffic", lambda: None)
    monkeypatch.setattr(game, "check_population_safety", lambda: None)

    def mock_display_board():
        game.running = False

    monkeypatch.setattr(game, "display_board", mock_display_board)

    class MockListener:
        '''
        Mock keyboard listener that does nothing, but is needed for testing.
        '''
        def __init__(self, on_press):
            pass

        def start(self):
            '''
            Mock start method that does nothing, but is needed for testing.
            '''
            pass

        def stop(self):
            ''''
            Mock stop method that does nothing, but is needed for testing.
            '''
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


# Equivalence class 6: figures list content
def test_figures_contains_correct_classes():
    '''
    Test that figures contains the expected object types in the correct order.
    '''
    expected_types = [
        Field,
        Water,
        House,
        Business,
        Street,
        Car
    ]

    for figure, expected_type in zip(figures, expected_types):
        assert isinstance(figure, expected_type)
