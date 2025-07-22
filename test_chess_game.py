import unittest
import tkinter as tk
import chess
from chess_game import ChessGUI

class TestChessGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.gui = ChessGUI(self.root)

    def test_initial_board_state(self):
        self.assertTrue(self.gui.board.is_valid())
        self.assertFalse(self.gui.board.is_game_over())
        self.assertEqual(self.gui.board.fullmove_number, 1)

    def test_valid_move(self):
        from_square = chess.E2
        to_square = chess.E4
        move = chess.Move(from_square, to_square)
        self.assertIn(move, self.gui.board.legal_moves)
        self.gui.board.push(move)
        self.assertEqual(str(self.gui.board.piece_at(to_square)), "P")

    def test_illegal_move(self):
        illegal_move = chess.Move(chess.E2, chess.E5)
        self.assertNotIn(illegal_move, self.gui.board.legal_moves)

    def test_game_over_checkmate(self):
        moves = ["f2f3", "e7e5", "g2g4", "d8h4"]
        for move in moves:
            self.gui.board.push_uci(move)
        self.assertTrue(self.gui.board.is_game_over())
        self.assertEqual(self.gui.board.result(), "0-1")

    def test_update_board_does_not_crash(self):
        try:
            self.gui.update_board()
        except Exception as e:
            self.fail(f"update_board() raised an exception: {e}")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
