from pss_code.pss_utils import check_winner
from pss_code.pss_utils import PAPER, SCISSORS, STONE, VALID_MOVES
from pss_code.pss_players import pick_move_random


# test the win check method
def test_win_check():
    assert check_winner(PAPER, SCISSORS) == -1
    assert check_winner(PAPER, STONE) == 1
    assert check_winner(SCISSORS, SCISSORS) == 0
    assert check_winner(STONE, STONE) == 0
    assert check_winner(SCISSORS, STONE) == -1


# test the random player to check it always returns
# a move in VALID_MOVES and to check that it uses
# all VALID_MOVES
def test_pick_move_random():
    totals = {v: 0 for v in VALID_MOVES}
    for i in range(1000):
        move = pick_move_random()
        assert move in VALID_MOVES
        totals[move] += 1
    for v in VALID_MOVES:
        assert totals[v] > 0
