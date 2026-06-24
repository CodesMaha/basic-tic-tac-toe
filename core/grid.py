""" logic preparing a grid with a label and its position in grid """

G_SIZE = 3

# falsy value for empty slot then x or o for turns
class Grid:
    def __init__(self):
        self.grid = []; self.reset_grid()

    def reset_grid(self) -> list[list[list[str]]]:
        self.grid = [['', '', ''] for _ in range(G_SIZE)]

    def is_slot_available(self, index: tuple[int, int]) -> bool:
        """ 
        check if grid slot is empty or not.
        if empty then return True else False
        """
        return not bool(self.grid[index[0]][index[1]])

    def modify_grid(self, content: str, index: tuple[int, int] | None) -> None:
        """ 
        replace grid index only if the spot has not been taken.
        truthy content intended. falsy index returns no change
        """ 
        if not index:
            return # for if index from core.mechanics.other_turn is None
        self.grid[index[0]][index[1]] = self.grid[index[0]][index[1]] or content