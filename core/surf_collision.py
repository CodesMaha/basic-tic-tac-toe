""" detecting collision of clickable surfaces """

import pygame
from rendering.icons import SQUARE_WIDTH, pos_grid
from core.grid import G_SIZE

single_square = pygame.Surface((SQUARE_WIDTH, SQUARE_WIDTH))

def check_grid(mouse_pos) -> tuple[int, int] | None:
    """ 
    check for collision then return index of which grid pressed.
    if not found then return None
    """

    def actual_check(index0, index1) -> bool:
        if single_square.get_rect(topleft=pos_grid[index0][index1]).collidepoint(mouse_pos):
            return True
        else: return False

    # loop to run checks
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            if not actual_check(i, j): continue
            return i, j