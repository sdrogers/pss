# Utility methods for PSS
from slugify import slugify
import time
import os
import csv

PAPER = 0
SCISSORS = 1
STONE = 2
VALID_MOVES = set([PAPER, SCISSORS, STONE])

MOVE_DICT = {PAPER: 'Paper', SCISSORS: 'Scissors', STONE: 'Stone'}


# method to check winner of the round
def check_winner(p1_choice, p2_choice):
    assert p1_choice in VALID_MOVES
    assert p2_choice in VALID_MOVES
    if p1_choice == p2_choice + 1:
        winner = 1
    elif p1_choice == p2_choice - 2:
        winner = 1
    elif p2_choice == p1_choice + 1:
        winner = -1
    elif p2_choice == p1_choice - 2:
        winner = -1
    elif p2_choice == p1_choice:
        winner = 0
    return winner


def dump_history_to_csv(history, name, file_name=None):
    # dump the history to a .csv file
    # if filename is None, make a filename from
    # the slug of the name and the int timestamp
    name = slugify(name)
    head_line = ['AI', name]
    if file_name is None:
        file_name = f'{name}_{int(time.time())}.csv'


    # check if folder exists
    if not os.path.isdir('game_dumps'):
        os.makedirs('game_dumps')

    # write the csv
    with open(os.path.join('game_dumps', file_name), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(head_line)
        for move in history:
            writer.writerow(move)
    

