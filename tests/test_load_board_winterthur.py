from skripts.Class_Game import load_board_winterthur
from skripts.Class_Fill import Field, Street, House, Business, Water, Car

def test_load_board_winterthur():
    game = load_board_winterthur()
    assert len(game.board) == 30
    assert len(game.board[0]) == 30
    assert isinstance(game.board[0][0], (Field, Street, House, Business, Water, Car))
