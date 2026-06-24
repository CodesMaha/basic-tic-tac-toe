""" has Grid class with methods for grid modification and win checks """

from enum import Enum
from core.data_handler import increment_score

G_SIZE = 3

class Winner(Enum):
    """ 
    different win conditions 
    so str | None
    """
    X = "x"; O = "o"
    DRAW = "draw"
    CONTINUE = None

# falsy value for empty slot then x or o for turns
class Grid:
    def __init__(self):
        self.grid = []; self.reset_grid()

    def reset_grid(self) -> list[list[str]]:
        self.grid = [['', '', ''] for _ in range(G_SIZE)]

    def is_slot_available(self, index: tuple[int, int]) -> bool:
        """ 
        check if grid slot is empty or not.
        if empty then return True else False
        """
        return not bool(self.grid[index[0]][index[1]])

    def modify_grid(self, content: Winner, index: tuple[int, int] | None) -> None:
        """ 
        replace grid index only if the spot has not been taken.
        truthy content intended. falsy index returns no change
        """ 
        if not index:
            return # for if index from core.mechanics.other_turn is None
        self.grid[index[0]][index[1]] = self.grid[index[0]][index[1]] or content.value


    def _check_left_diagonal(self, turn: str) -> bool:
        return all(self.grid[i][i] == turn for i in range(G_SIZE))

    def _check_right_diagonal(self, turn: str) -> bool:
        return all(self.grid[i][G_SIZE - (i+1)] == turn for i in range(G_SIZE))

    def _check_horizontal(self, turn: str) -> bool:
        for row in range(G_SIZE):
            if all(self.grid[row][col] == turn for col in range(G_SIZE)):
                return True
        return False

    def _check_vertical(self, turn: str) -> bool:
        for col in range(G_SIZE):
            if all(self.grid[row][col] == turn for row in range(G_SIZE)):
                return True
        return False
    
    def _is_draw(self) -> bool:
        """ check if any slots are available or empty str """
        for row in self.grid:
            if any(not col for col in row):
                return False
        return True

    def is_win(self) -> Winner:
        """ 
        check conditions for if x or o has won.
        also call increment_score.
        return from Enum class type str | None
        """

        if self._is_draw():
            return Winner.DRAW

        def check_turn(turn: str) -> bool:
            """ check if this turn led to a win or not """
            for i in (
                self._check_left_diagonal, self._check_right_diagonal, 
                self._check_horizontal, self._check_vertical
            ):
                if i(turn):
                    return True
            return False
        
        for i in (Winner.X, Winner.O):
            if check_turn(i.value):
                increment_score(i.value)
                return i
        
        return Winner.CONTINUE