""" win-related rendering functions """

import pygame
from core.coord_calc import center_surface
from . import colours as col
from .icons import MARGIN_IC
from core.data_handler import read_data

big_font = pygame.font.SysFont("monospace", 64)
small_font = pygame.font.SysFont("monospace", 32)
scores = read_data() # initialize

def draw_win_msg(screen: pygame.Surface, winner: str) -> None:
    """ blit msg onto screen. arg winner could be 'draw' """
    global scores
    if winner == "draw":
        msg = "no winner"
    else:
        msg = f"{winner} wins"

    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 179)) # black
    screen.blit(overlay)

    font_img = big_font.render(msg, True, col.WHITE)
    screen.blit(font_img, center_surface(screen, font_img))

def draw_scores(screen: pygame.Surface) -> None:
    """ blit scores for x and o """
    text_img = small_font.render(f"x: {scores["x_score"]}", True, col.BLACK)
    screen.blit(text_img, (MARGIN_IC, 0))
    
    text_img = small_font.render(f"o: {scores["o_score"]}", True, col.BLACK)
    screen.blit(text_img, (screen.get_width() - (text_img.get_width() + MARGIN_IC), 0))