import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = [''] * 9  # To keep track of the moves in the board
        self.current_player = 'X'  # X starts first

        # Create a 3x3 grid of buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text='', font=('normal', 20), width=10, height=3,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create a Reset Button
        self.reset_button = tk.Button(root, text="Reset", font=('normal', 15), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, index):
        """Update the board and check for win or draw."""
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                self.display_winner()
            elif '' not in self.board:
                self.display_draw()
            else:
                self.switch_player()

    def switch_player(self):
        """Switch between player X and O."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        """Check if the current player has won."""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]
        
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != '':
                return True
        return False

    def display_winner(self):
        """Display a message when a player wins."""
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_game()

    def display_draw(self):
        """Display a message when the game ends in a draw."""
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        """Reset the game to the initial state."""
        self.board = [''] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='')

# Set up the main application window
root = tk.Tk()
game = TicTacToe(root)

# Run the application
root.mainloop()
