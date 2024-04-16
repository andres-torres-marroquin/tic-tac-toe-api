import random


def check_winner(board):
    """
    Check if either "X" or "O" has won in a Tic Tac Toe game.

    Args:
        board (list of lists): The Tic Tac Toe board represented as a 3x3 grid.

    Returns:
        str or None: The winning symbol ("X" or "O") if there is a winner, otherwise None.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ".":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ".":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
        return board[0][2]

    # No winner
    return ''


def get_random_x_y():
    return random.randint(0, 2), random.randint(0, 2)
