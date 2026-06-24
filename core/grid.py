""" logic preparing a grid with a label and its position in grid """

G_SIZE = 3

# falsy value for empty slot then x or o for turns
def reset_grid() -> list[list[list[str]]]:
    return [['', '', ''] for _ in range(G_SIZE)]

def is_full(grid: list[list[str]]) -> bool:
    return all([[bool[b] for b in a] for a in grid])

def is_slot_available(
        grid: list[list[str]], 
        index: tuple[int, int]
    ) -> bool:
    """ 
    check if grid slot is empty or not.
    if empty then return True else False
    """
    return not bool(grid[index[0]][index[1]])

def modify_grid(
        grid: list[list[list[str]]],
        content: str, index: tuple[int, int]
    ) -> list[list[list[str]]]:
    """ 
    replace grid index only if the spot has not been taken.
    truthy content intended. falsy index returns no change
    TODO: bool for if changed
    """
    grid[index[0]][index[1]] = grid[index[0]][index[1]] or content
    return grid