import os
import time
import csv
from mock import mock
from slugify import slugify
from pss_app.pss_utils import check_winner, dump_history_to_csv
from pss_app.pss_utils import PAPER, SCISSORS, STONE, VALID_MOVES
from pss_app.pss_players import pick_move_random


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
    for _ in range(1000):
        move = pick_move_random()
        assert move in VALID_MOVES
        totals[move] += 1
    for v in VALID_MOVES:
        assert totals[v] > 0


# test that the file writing makes a correct file
# mock the time.time call in pss_utils to 
# return 12345 regardless of the actual time
@mock.patch('pss_app.pss_utils.time.time', mock.MagicMock(return_value=12345))
def test_write_csv():

    history = [
        [1, 0],
        [0, 2],
        [2, 2]
    ]
    name = 'simon rogers test'
    slug_name = slugify(name)
    expected_file_name = f'{slug_name}_12345.csv'
    file_path = os.path.join('game_dumps', expected_file_name)

    # Call the method
    dump_history_to_csv(history, name)
    
    # Check that the file exists (should probably delete before)
    assert os.path.isfile(file_path)
    
    # Open the file and check its contents
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        heads = next(reader)
        # check the heading
        assert heads == ['AI', slug_name]
        for i, line in enumerate(reader):
            # check the other lines
            int_line = [int(l) for l in line]
            assert int_line == history[i]

