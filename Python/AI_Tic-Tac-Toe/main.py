from board import Board
from gui import TicTacToeGUI
import tkinter as tk

def main():
    # Initialize the game board
    game_board = Board()

    # Set up the Tkinter root window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Initialize the GUI with the game board
    gui = TicTacToeGUI(root, game_board)

    # Start the Tkinter main loop (this will now handle all events like clicks)
    root.mainloop()

if __name__ == "__main__":
    main()
