# pss_players.py
import random
from .pss_utils import VALID_MOVES

#method to generate a random choice of moves
def pick_move_random(history=None):
    cpu_move = random.randint(min(VALID_MOVES), max(VALID_MOVES))
    return cpu_move

if __name__ == '__main__':
    totals = {v: 0 for v in VALID_MOVES}
    for i in range(1000):
        result = pss_players.pick_move()
        totals[result] += 1
        assert result in VALID_MOVES
    print(totals)