# Utility methods for PSS

PAPER = 0
SCISSORS = 1
STONE = 2
VALID_MOVES = [PAPER, SCISSORS, STONE]

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
    
if __name__ == "__main__":
    check_winner(PAPER, SCISSORS)
    assert winner == -1
    check_winner(STONE, PAPER)
    assert winner == 1
    check_winner(SCISSORS, SCISSORS)
    assert winner == 0