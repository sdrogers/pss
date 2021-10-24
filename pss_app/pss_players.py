# pss_players.py
import random
from .pss_utils import VALID_MOVES


# method to generate a random choice of moves
def pick_move_random(history: list[list[int]]=None) -> int:
    cpu_move = random.randint(min(VALID_MOVES), max(VALID_MOVES))
    return cpu_move
