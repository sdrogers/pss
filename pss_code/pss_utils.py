# Utility methods for PSS

PAPER = 0
SCISSORS = 1
STONE = 2

#method to check winner of the round

def check_winner(p1Choice, p2Choice):
    if p1Choice == p2Choice + 1:
        winner = 1
    elif p1Choice == p2Choice - 2:
        winner = 1
    elif p2Choice == p1Choice + 1:
        winner = -1
    elif p2Choice == p1Choice - 2:
        winner = -1
    elif psChoice == p1Choice:
        winner = 0