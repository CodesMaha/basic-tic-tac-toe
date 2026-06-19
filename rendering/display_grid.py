""" draws on the screen """

import pygame
from . import icons as ic
from . import colours as col
import core.coord_calc as cc

def draw_grid(screen: pygame.surface.Surface, grid: list[list[list[str, tuple[int, int]]]]):
    screen.fill(col.BG)
    screen.blit(ic.surf_grid, cc.center_surface(screen, ic.surf_grid))

    # drawing grid
    for i in range(3):
        for j in grid[i]:
            if j[0] == "x": screen.blit(ic.x, j[1])
            elif j[0] == "o": screen.blit(ic.o, j[1])