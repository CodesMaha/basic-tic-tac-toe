import pygame; pygame.init()
from sys import exit
from rendering.icons import SCREEN_SIZE
from rendering.display_grid import draw_grid
from core.data_handler import increment_score
from rendering.display_score import draw_win_msg, draw_scores
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

def decide_winner(grid_) -> str | None:
    """ decide value of winner after turns """
    if winner: # already not None
        return winner
    
    if is_draw(grid_):
        return "draw"
    
    for i in ("x", "o"):
        if is_win(grid_, i):
            increment_score(i)
            return i
    return None # if no break in loop

running = True
while running:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (event.type == pygame.MOUSEBUTTONUP) and (not winner):
            collided = collisions.check_grid(pygame.mouse.get_pos())
            grid = g.modify_grid(grid, "x", collided)
            # TODO: fix bug where comp takes turn if empty slot chosen
            if collided: 
                grid = g.modify_grid(grid, "o", computer_choose(grid))
                collided = None
            winner = decide_winner(grid)

    draw_grid(screen, grid)
    draw_scores(screen)
    if winner:
        draw_win_msg(screen, winner)

    pygame.display.flip()

pygame.quit(); exit()