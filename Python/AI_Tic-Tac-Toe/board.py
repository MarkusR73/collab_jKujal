import numpy as np

class Board:
    def __init__(self):
        # Initialize a 3x3 board with zeros
        self.board = np.array([[0 for _ in range(3)] for _ in range(3)])

    def clear_board(self):
        self.board = np.array([[0 for _ in range(3)] for _ in range(3)])

    def update_board(self, location, symbol):
        self.board[location[0]][location[1]]=symbol

    def get_board_setup(self):
        return self.board.copy()

    def check_winner(self):
        board = self.board
        # Check rows and columns
        for i in range(3):
            if abs(sum(board[i, :])) == 3:  # Check row
                return True
            if abs(sum(board[:, i])) == 3:  # Check column
                return True
        # Check diagonals
        if abs(sum(board.diagonal())) == 3:  # Main diagonal
            return True
        if abs(sum(np.fliplr(board).diagonal())) == 3:  # Anti-diagonal
            return True
        return False

    def check_tie(self):
        """Check if the game is a tie (board is full, no winner)."""
        return not any(0 in row for row in self.board) and not self.check_winner()
