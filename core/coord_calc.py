""" basic functions for math of some coordinate calculations """

import pygame

def center_surface(surf1: pygame.Surface, surf2: pygame.Surface) -> tuple[int,int]:
    """ return resulting coords of if surf2 is centered at surf1 """
    return (surf1.get_width() - surf2.get_width()) //2, (surf1.get_height() - surf2.get_height()) //2

def get_midpoint(surf: pygame.Surface) -> tuple[int, int]:
    """ return the centre of the given surface """
    return surf.get_width() //2, surf.get_height() //2

def add_tuples(t1: tuple[int,int], t2: tuple[int,int]) -> tuple[int, int]:
    ''' tuple comprehension for combining two coordinate pairs '''
    return tuple(sum((x, y)) for x, y in zip(t1, t2))