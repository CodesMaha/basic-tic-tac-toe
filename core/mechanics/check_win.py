""" checks for winner based on grid """

G_SIZE: int = 3 # grid size is 3 for tic-tac-toe

def check_left_diagonal(grid: list[list[str]], turn: str) -> bool:
    return all(grid[i][i] == turn for i in range(G_SIZE))

def check_right_diagonal(grid:list[list[str]], turn: str) -> bool:
    return all(grid[i][G_SIZE - (i+1)] == turn for i in range(G_SIZE))

def check_horizontal(grid: list[list[str]], turn: str) -> bool:
    for row in range(G_SIZE):
        if all(grid[row][col] == turn for col in range(G_SIZE)):
            return True
    return False

def check_vertical(grid: list[list[str]], turn: str) -> bool:
    for col in range(G_SIZE):
        if all(grid[row][col] == turn for row in range(G_SIZE)):
            return True
    return False

def is_win(grid: list[list[str]], turn: str) -> bool:
    """ check conditions for if x or o has won """
    for i in (
        check_left_diagonal, check_right_diagonal, check_horizontal, check_vertical
    ):
        if i(grid, turn):
            return True
    return False # if loop executed without return

def is_draw(grid: list[list[str]]) -> bool:
    """ check if any slots are available or empty str """
    for row in range(G_SIZE):
        if any(not grid[row][col] for col in range(G_SIZE)):
            return False # if any slot is available
    return True