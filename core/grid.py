""" logic preparing a grid with a label and its position in grid """

G_SIZE = 3

# falsy value for empty slot then x or o for turns
def reset_grid() -> list[list[list[str]]]:
    return [['', '', ''] for _ in range(G_SIZE)]

def is_full(grid: list[list[str]]) -> bool:
    return all([[bool[b] for b in a] for a in grid])

def modify_grid(
        grid: list[list[list[str]]],
        content: str, index: tuple[int, int]
    ) -> list[list[list[str, tuple[int, int]]]]:
    """ 
    replace grid index only if the spot has not been taken.
    truthy content intended. falsy index returns no change
    TODO: bool for if changed
    """
    if not index: 
        return grid
    grid[index[0]][index[1]] = grid[index[0]][index[1]] or content
    return grid