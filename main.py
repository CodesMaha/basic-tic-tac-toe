import pygame; pygame.init()
from sys import exit
from rendering.icons import SCREEN_SIZE
from rendering.display_grid import draw_grid
from rendering.display_score import draw_win_msg
import core.surf_collision as collisions
import core.grid as g
from core.mechanics.other_turn import computer_choose
from core.mechanics.check_win import is_win, is_draw

# initializations
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("tic-tac-toe")

winner: str | None = None
grid = g.reset_grid()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (event.type == pygame.MOUSEBUTTONUP) and (not winner):
            collided = collisions.check_grid(pygame.mouse.get_pos())
            grid = g.modify_grid(grid, "x", collided)
            if collided: 
                grid = g.modify_grid(grid, "o", computer_choose(grid))
                collided = None

    draw_grid(screen, grid)
    if not winner:
        if is_draw(grid):
            winner = "draw"
        elif is_win(grid, "x"):
            winner = "x"
        elif is_win(grid, "o"):
            winner = "o"
    else:
        draw_win_msg(screen, winner)

    pygame.display.flip()

pygame.quit(); exit()