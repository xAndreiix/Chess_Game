import tkinter as tk
from tkinter import messagebox
import chess

PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
    '.': ' '
}

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Chess GUI")
        self.board = chess.Board()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.selected_square = None
        self.cursor_row = 7  # Start from bottom left like real chess
        self.cursor_col = 0
        self.create_board()
        self.master.bind('<Key>', self.move_with_keys)
        self.update_highlight()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                color = '#EEE' if (row + col) % 2 == 0 else '#444'
                btn = tk.Button(self.master, font=('Helvetica', 32), width=2, height=1,
                                bg=color, fg='black',
                                command=lambda r=row, c=col: self.select_square(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
        self.update_board()

    def update_board(self):
        board_str = str(self.board).split('\n')
        for row in range(8):
            line = board_str[row].split(' ')
            for col in range(8):
                piece = line[col]
                self.buttons[row][col].config(text=PIECES.get(piece, ' '))
        self.update_highlight()

    def select_square(self, row, col):
        index = chess.square(col, 7 - row)
        if self.selected_square is None:
            if self.board.piece_at(index) and self.board.turn == self.board.piece_at(index).color:
                self.selected_square = index
        else:
            move = chess.Move(self.selected_square, index)
            if move in self.board.legal_moves:
                self.board.push(move)
                if self.board.is_game_over():
                    self.update_board()
                    messagebox.showinfo("Game Over", f"Game over: {self.board.result()}")
                    self.master.quit()
                self.selected_square = None
                self.update_board()
            else:
                self.selected_square = None
                self.update_board()

    def move_with_keys(self, event):
        if event.keysym == 'Up' and self.cursor_row > 0:
            self.cursor_row -= 1
        elif event.keysym == 'Down' and self.cursor_row < 7:
            self.cursor_row += 1
        elif event.keysym == 'Left' and self.cursor_col > 0:
            self.cursor_col -= 1
        elif event.keysym == 'Right' and self.cursor_col < 7:
            self.cursor_col += 1
        elif event.keysym == 'Return':
            self.select_square(self.cursor_row, self.cursor_col)
        self.update_highlight()

    def update_highlight(self):
        for r in range(8):
            for c in range(8):
                color = '#EEE' if (r + c) % 2 == 0 else '#444'
                if r == self.cursor_row and c == self.cursor_col:
                    self.buttons[r][c].config(bg='yellow')
                else:
                    self.buttons[r][c].config(bg=color)

if __name__ == '__main__':
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
