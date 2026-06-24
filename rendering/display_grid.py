""" draws on the screen """

import pygame
from . import icons as ic
from . import colours as col
import core.coord_calc as cc
from core.grid import G_SIZE

def draw_grid(screen: pygame.surface.Surface, grid: list[list[list[str, tuple[int, int]]]]):
    screen.fill(col.BG)
    screen.blit(ic.surf_grid, cc.center_surface(screen, ic.surf_grid))

    # drawing icons on grid
    for row in range(G_SIZE):
        for i, j in zip(grid[row], ic.pos_grid[row]):
            if not i: 
                continue # empty slot
            elif i == "x": screen.blit(ic.x, j)
            else: screen.blit(ic.o, j) # for o