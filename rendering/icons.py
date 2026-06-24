""" 
different surfaces manually defined to be blit, 
which are the lines of the grid and the icons for a nought and cross
"""

import pygame
from . import colours as col
import core.coord_calc as cc
from core.grid import G_SIZE

SCREEN_SIZE = (640, 580) # not pygame.RESIZEABLE
LINE_WEIGHT = 10

# grid
surf_grid = pygame.Surface(tuple(SCREEN_SIZE[1] //1.5 for x in range(2)))
surf_grid.fill(col.BG)

SQUARE_WIDTH = surf_grid.get_height() // G_SIZE
MARGIN_IC = SQUARE_WIDTH // 6
# list of lists to hold individual square positions
pos_grid: list[list[tuple[int,int]]] = [[(0,0) for _ in range(G_SIZE)] for _ in range(G_SIZE)]


def get_grid_pos(_pos_grid: list[list[tuple[int,int]]]) -> list[list[tuple[int,int]]]:
    """ reinitialize the positions of the topleft of squares on grid relative to grid """
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            _pos_grid[i][j] = j * SQUARE_WIDTH, i * SQUARE_WIDTH
    return _pos_grid

def adjust_grid_pos(_pos_grid: list[list[tuple[int,int]]]) -> list[list[tuple[int,int]]]:
    """ set grid positions as relative to the screen """
    offset = (SCREEN_SIZE[0] - surf_grid.get_width()) //2, (SCREEN_SIZE[1] - surf_grid.get_height()) //2
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            _pos_grid[i][j] = cc.add_tuples(pos_grid[i][j], offset)
    return _pos_grid


# the actual surfaces getting defined
def draw_grid_lines(
        _surf_grid: pygame.Surface, 
    ) -> pygame.Surface:
    """ four lines for tic-tac-toe """

    for i in (1, 2): # two lines drawn twice
        square_offset = i * SQUARE_WIDTH

        # vertical lines then horizontal lines
        pygame.draw.line(
            _surf_grid, col.GRID, 
            (square_offset, 0), (square_offset, _surf_grid.get_height()),
            LINE_WEIGHT
        )
        pygame.draw.line(
            _surf_grid, col.GRID, 
            (0, square_offset), (_surf_grid.get_width(), square_offset),
            LINE_WEIGHT
        )

    return _surf_grid

def draw_x() -> pygame.Surface:
    _x = pygame.Surface((SQUARE_WIDTH, SQUARE_WIDTH), pygame.SRCALPHA)

    x_line_weight = MARGIN_IC * 1.5

    pygame.draw.line( # start from topleft
        _x, col.X, (x_line_weight, x_line_weight), 
        (SQUARE_WIDTH - x_line_weight, SQUARE_WIDTH - x_line_weight),
        LINE_WEIGHT
    )
    pygame.draw.line( # start from top right
        _x, col.X, 
        (SQUARE_WIDTH - x_line_weight, x_line_weight), (x_line_weight, SQUARE_WIDTH - x_line_weight),
        LINE_WEIGHT
    )
    
    return _x

def draw_o() -> pygame.Surface:
    _o = pygame.Surface((SQUARE_WIDTH, SQUARE_WIDTH), pygame.SRCALPHA)

    pygame.draw.circle(
        _o, col.O, 
        (SQUARE_WIDTH //2, SQUARE_WIDTH //2), 
        (SQUARE_WIDTH //2) - MARGIN_IC, LINE_WEIGHT
    )

    return _o


# initilizing with functions
surf_grid = draw_grid_lines(surf_grid)
pos_grid = adjust_grid_pos(get_grid_pos(pos_grid))
x = draw_x()
o = draw_o()