""" menace implementation for turn indexes """

from random import choice
from core.grid import G_SIZE

class MENACETurn:
    """ functions related to how MENACE will play """
    def __init__(self, matchboxes_data: dict):
        self.matchboxes: dict = matchboxes_data
        self.INDEXES: list[tuple[int, int]] = [(a, b) for a in range(G_SIZE) for b in range(G_SIZE)]
        self.moves: set = set()
    
    def reset_moves(self) -> None:
        self.moves.clear()

    def get_new_beads(self, grid: str) -> list:
        """ modify matchboxes with new beads """
        # get all available slots in str version
        new_beads: list[tuple] = [idx for idx, val in zip(self.INDEXES, grid) if val == ' ']
        self.matchboxes.update({grid: new_beads}) # modify matchboxes
        return new_beads

    def choose(self, grid: str) -> tuple[int, int] | None:
        """ return grid indexes or None if draw """
        if grid not in self.matchboxes: # keys
            self.get_new_beads(grid)
        beads: list[tuple] = self.matchboxes[grid]

        if beads:
            # more likely to choose idx if more instances
            bead: tuple[int, int] = choice(beads)
            self.moves.add((grid, bead))
        else: # no empty slots
            return None
        return bead