""" logic preparing a grid with a label and its position in grid """

from rendering.icons import pos_grid
from core.mechanics.check_win import G_SIZE

# falsy value for empty slot then x or o for turns
def reset_grid() -> list[list[list[str, tuple[int, int]]]]:
    new_grid = [[] for x in range(G_SIZE)]
    for i in range(G_SIZE):
        for j in range(G_SIZE):
            new_grid[i].append(["", pos_grid[i][j]])
    return new_grid

def modify_grid(
        grid: list[list[list[str, tuple[int, int]]]],
        content: str, index: tuple[int, int]
    ) -> list[list[list[str, tuple[int, int]]]]:
    """ 
    replace grid index only if the spot has not been taken.
    truthy content intended. falsy index returns no change"""
    if not index: 
        return grid
    grid[index[0]][index[1]][0] = grid[index[0]][index[1]][0] or content
    return grid