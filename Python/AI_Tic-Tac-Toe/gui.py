import tkinter as tk
from tkinter import messagebox
from player import RandomPlayer  # Import the RandomPlayer class
from board import Board

class TicTacToeGUI:
    def __init__(self, master, board):
        self.master = master
        self.board = board
        self.round_number = 0  # Keep track of the number of games played
        self.current_player = 1  # 1 for Player 1, -1 for Player 2
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

        # Initialize the players (Player 1 is human, Player 2 is random)
        self.player1 = "Player 1"  # Player 1 (human)
        self.player2 = RandomPlayer("Player 2", "O", self.board)  # Player 2 (random)
        self.current_player_instance = self.player1  # Player 1 starts the game

    def create_widgets(self):
        """Create the Tkinter widgets."""
        self.create_board()  # Create the game board (3x3 grid of buttons)

        # Label to display the number of games played
        self.game_counter_label = tk.Label(
            self.master,
            text=f"Games Played: {self.round_number}",
            font=("Arial", 16)
        )
        self.game_counter_label.grid(row=3, column=0, columnspan=3)  # Position below the board

    def create_board(self):
        """Create the Tic-Tac-Toe board with buttons."""
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.master,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.execute_turn(r, c),  # Assign button click event
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def execute_turn(self, row, col):
        """Execute the player's turn when a valid, empty cell is clicked."""
        setup = self.board.get_board_setup()  # Get the current board setup (numpy array)
        if setup[row, col] == 0:  # Check if the cell is empty
            # Update the board with the current player's move
            self.board.update_board((row, col), self.current_player)

            # Update the button with the corresponding symbol
            symbol = "X" if self.current_player == 1 else "O"
            self.buttons[row][col].config(text=symbol, state="disabled")  # Disable the button

            # Check for a winner after each move
            if self.board.check_winner():
                winner = "Player 1" if self.current_player == 1 else "Player 2"
                self.show_winner(winner)
                self.end_game()

            # Check for a tie if the board is full but no winner
            if self.board.check_tie():
                self.show_tie()
                self.end_game()

            # Switch to the other player after a valid move
            self.current_player *= -1
            self.current_player_instance = self.player2 if self.current_player == -1 else self.player1

            # If it's Player 2's turn (the random player), make a move automatically
            if self.current_player == -1:
                self.random_player_turn()

        else:
            # If the button is not empty, show an error message
            messagebox.showinfo("Invalid Move", "Cell already occupied!")

    def random_player_turn(self):
        """Let the RandomPlayer take its turn."""
        next_move = self.player2.choose_next_move()  # Get a random move from Player 2
        row, col = next_move
        self.execute_turn(row, col)  # Make the random move by calling execute_turn

    def show_winner(self, winner):
        """Display the winner and disable all buttons."""
        messagebox.showinfo("Game Over", f"{winner} wins!")
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")  # Disable all buttons when the game ends

    def show_tie(self):
        """Display the tie message and disable all buttons."""
        messagebox.showinfo("Game Over", "It's a tie!")

    def end_game(self):
        """End the game, disable all buttons and clear the board for the next round."""
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")  # Disable all buttons when the game ends

        # After the game ends, reset the board for a new round
        self.reset_game()

    def reset_game(self):
        """Reset the game state for a new round."""
        self.board.clear_board()  # Clear the board
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.config(text="", state="normal")  # Reset button text and enable

        # Increment the round number and update the label
        self.round_number += 1  # Increment the round number after the loop
        self.game_counter_label.config(text=f"Games Played: {self.round_number}")

        # Alternate the starting player based on round number
        self.current_player = 1 if self.round_number % 2 == 0 else -1  # Player 1 starts on even rounds, Player 2 on odd rounds
        self.current_player_instance = self.player1 if self.current_player == 1 else self.player2
