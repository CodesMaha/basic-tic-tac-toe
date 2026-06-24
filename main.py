import pygame; pygame.init()
from sys import exit

from rendering.icons import SCREEN_SIZE
from rendering.display_grid import draw_grid
from rendering.display_score import draw_win_msg, draw_scores

import core.surf_collision as collisions
from core.grid import Grid, Winner
from core.other_turn import computer_choose

# initializations
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("tic-tac-toe")

g = Grid() # board is g.grid
winner: Winner = Winner.CONTINUE
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (event.type == pygame.MOUSEBUTTONUP) and (not winner.value):
            collided = collisions.check_grid(pygame.mouse.get_pos())
            if (collided) and (g.is_slot_available(collided)): 
                g.modify_grid(Winner.X, collided)
                g.modify_grid(Winner.O, computer_choose(g.grid))
                collided = None
                winner = g.is_win()

    draw_grid(screen, g.grid)
    draw_scores(screen)
    if winner.value:
        draw_win_msg(screen, winner.value)

    pygame.display.flip()

pygame.quit(); exit()