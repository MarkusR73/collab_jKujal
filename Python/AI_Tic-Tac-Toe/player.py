import numpy as np
import random
from board import Board

class Player:
    def __init__(self, name, symbol, board):
        self.name = name
        self.symbol = symbol
        self.board = board
        # Initialize dictionary to store board setups and their moves
        self.moves_for_setup = {}  # Dictionary to store board setups and their moves

    def setup_already_observed(self, setup):
        # Check all rotations of the current board
        for _ in range(4):  # 0, 90, 180, 270 degrees
            serialized_setup = setup.tobytes()
            if serialized_setup in self.moves_for_setup:
                return serialized_setup  # Return the serialized key if found
            # Rotate the board 90 degrees counterclockwise
            temp_board = np.rot90(setup)
        # If no match is found, return None
        return None

    def initialize_new_setup(self, setup, key):
        """Add the current board to the recognized setups for the given turn."""
        for row in range(setup.shape[0]):  # Iterate over the rows (indices)
            for column in range(setup.shape[1]):  # Iterate over the columns (indices)
                if setup[row, column] == 0:  # Check if the cell is empty
                    # Record the move (row, column) for the current setup
                    if key not in self.moves_for_setup:
                        self.moves_for_setup[key] = []
                    self.moves_for_setup[key].append((row, column))  # Append as a tuple

    def choose_next_move(self):
        """Check if the current board setup has already been observed, and add if not initialize all possible moves for the setup."""
        current_board_setup = self.board.get_board_setup()
        serialized_key = self.setup_already_observed(current_board_setup)
        if serialized_key is None:  # Not observed
            serialized_key = current_board_setup.tobytes()
            self.initialize_new_setup(current_board_setup, serialized_key)

        next_move = random.choice(self.moves_for_setup[serialized_key])
        return next_move

class RandomPlayer(Player):
    def __init__(self, name, symbol, board):
        super().__init__(name, symbol, board)

class LearningPlayer(Player):
    def __init__(self, name, symbol, board):
        super().__init__(name, symbol, board)
