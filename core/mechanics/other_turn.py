""" use randomness to decide the turn of the computer """

from random import choice
from .check_win import G_SIZE

def computer_choose(grid: list[list[str, tuple]]) -> tuple[int, int] | None:
    """ return random grid position. or skip turn if draw """
    slots: list[tuple[int,int]] = [] # to append to
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            if not grid[i][j][0]: # if empty
                slots.append((i,j))
    
    if slots: # else None
        return choice(slots)