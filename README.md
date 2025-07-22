# Python Chess GUI 🎯

A complete GUI-based chess game implemented in Python using `tkinter` and the powerful `python-chess` engine for move validation and game state management.

## 🧩 Project Structure

- ├── chess_game.py # Main GUI chess game using tkinter
- ├── test_chess_game.py # Full test coverage using unittest
- ├── .gitignore # Git configuration to ignore unnecessary files
- └── README.md # This file

## 🕹 Features

- Fully functional 8x8 chess board rendered with Unicode pieces ♔♕♖.
- Keyboard navigation with arrow keys + `Enter` for move selection.
- Mouse-click interaction for intuitive gameplay.
- Automatic validation of legal moves.
- Detects game over (checkmate, stalemate) and displays the result via popup.
- Clean and modern interface using tkinter.
- Built-in test suite to verify game functionality and rules.

## 🧪 Testing

Testing is implemented using the `unittest` module. To run tests:

```bash```
python test_chess_game.py

Test coverage includes:
- Initial board state validation
- Valid and invalid move execution
- Checkmate detection (e.g., Fool's Mate)
- GUI method robustness (update_board)
- Full setup and teardown of the GUI environment

## 📦 Dependencies
- python-chess
- tkinter (standard with Python on most systems)
- Install python-chess via pip if not already:
- pip install python-chess

## 🚀 Running the Application
python chess_game.py

## 🛡 Git Integration
This project includes a full .gitignore to avoid cluttering the repository with unnecessary files like __pycache__, .venv/, editor configs, OS metadata, and test caches.

Enjoy playing chess in Python with a beautiful minimal GUI. ♟