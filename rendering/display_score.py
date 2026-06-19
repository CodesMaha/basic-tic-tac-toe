""" win-related rendering functions """

import pygame
from core.coord_calc import center_surface
from . import colours as col

big_font = pygame.font.SysFont("monospace", 64)
small_font = pygame.font.SysFont("monospace", 32)

def draw_win_msg(screen: pygame.Surface, winner: str) -> None:
    """ blit msg onto screen. arg winner could be 'draw' """
    msg = "no winner" if winner == "draw" else f"{winner} wins"

    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 179)) # black
    screen.blit(overlay)

    font_img = big_font.render(msg, True, col.TEXT)
    screen.blit(font_img, center_surface(screen, font_img))