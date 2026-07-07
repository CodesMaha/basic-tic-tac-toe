""" win-related rendering functions """

import pygame
from core.coord_calc import center_surface
from . import colours as col
from .icons import MARGIN_IC

big_font = pygame.font.SysFont("monospace", 64)
small_font = pygame.font.SysFont("monospace", 32)

def draw_win_msg(screen: pygame.Surface, winner: str) -> None:
    """ blit msg onto screen. arg winner could be 'draw' """
    if winner == "draw":
        msg = "no winner"
    else:
        msg = f"{winner} wins"

    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 179)) # black
    screen.blit(overlay)

    font_img = big_font.render(msg, True, col.WHITE)
    screen.blit(font_img, center_surface(screen, font_img))

def draw_scores(screen: pygame.Surface, score_data: dict) -> None:
    """ blit scores for x and o """
    text_img = small_font.render(f"x: {score_data["x_score"]}", True, col.BLACK)
    screen.blit(text_img, (MARGIN_IC, 0))
    
    text_img = small_font.render(f"o: {score_data["o_score"]}", True, col.BLACK)
    screen.blit(text_img, (screen.get_width() - (text_img.get_width() + MARGIN_IC), 0))