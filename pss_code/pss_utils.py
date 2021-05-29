# Utility methods for PSS
import random

PAPER = 0
SCISSORS = 1
STONE = 2
VALID_MOVES = set([PAPER, SCISSORS, STONE])

#method to check winner of the round

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


#method to generate a random choice of moves

def pick_move():
    cpu_move = random.randint(0, 2)
    return cpu_move

if __name__ == "__main__":
    assert check_winner(PAPER, SCISSORS) == -1
    assert check_winner(PAPER, STONE) == 1
    assert check_winner(SCISSORS, SCISSORS) == 0
    totals = {PAPER:0, SCISSORS:0, STONE:0}
    for i in range(1000):
        result = pick_move()
        totals[result] += 1
        print(totals)
        assert pick_move() in VALID_MOVES
    