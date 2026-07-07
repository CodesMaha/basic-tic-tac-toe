""" menace implementation for turn indexes """

from random import choice
from core.grid import G_SIZE

def computer_choose(grid: list[list[str]]) -> tuple[int, int] | None:
    """ return random grid indexes. or skip turn if draw """
    slots: list[tuple[int,int]] = [] # to append to
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            if not grid[i][j]: # if empty
                slots.append((i,j))
    
    if slots: # else None
        return choice(slots)

class MENACETurn:
    """ functions related to how MENACE will play """
    def __init__(self):
        self.matchboxes: dict = {}
        self.INDEXES: list[tuple[int, int]] = [(a, b) for a in range(G_SIZE) for b in range(G_SIZE)]
        self.moves: set = set()
    
    def reset_moves(self) -> None:
        self.moves.clear()

    def new_beads(self, grid: str) -> list:
        """ modify matchboxes with new beads """
        # get all available slots in str version
        new_beads: list[tuple] = [idx for idx, val in zip(self.INDEXES, grid) if val == ' ']
        self.matchboxes.update({grid: new_beads}) # modify matchboxes
        return new_beads

    def choose(self, grid: str) -> tuple[int, int] | None:
        """ return grid indexes or None if draw """
        if grid not in self.matchboxes: # keys
            self.new_beads(grid)
        beads: list[tuple] = self.matchboxes[grid]

        if beads:
            # more likely to choose idx if more instances
            bead: tuple[int, int] = choice(beads)
            self.moves.add((grid, bead))
        else: # no empty slots
            return None
        return bead