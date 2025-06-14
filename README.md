# Tic Tac Toe Game with Minimax Algorithm

## 🎯 Objective

This project implements a simple **Tic Tac Toe** game in Python, where a human player competes against an AI opponent. The AI uses the **Minimax algorithm**, enabling it to play optimally and never lose.

---

## 🕹️ Game Description

Tic Tac Toe is a 2-player game played on a 3×3 grid. Players take turns marking a square with `X` or `O`.  
- The first player to get **three in a row** (horizontally, vertically, or diagonally) wins.  
- If all squares are filled and neither player has won, the game ends in a **tie**.

---

## 🧠 Minimax Algorithm

The **Minimax algorithm** is a recursive decision-making algorithm used in two-player games. It simulates all possible game states to determine the best move by assuming that both players play optimally.

### Algorithm Steps

1. **Evaluate the current board**  
   Check if there is a winner or if the board is full (tie).

2. **Generate possible moves**  
   List all empty cells available for a move.

3. **Simulate each move**  
   For each available move, place the symbol and recursively evaluate the result.

4. **Recursively call Minimax**  
   Alternate between minimizing and maximizing player scores for each depth level.

5. **Choose the optimal move**  
   - The AI (Maximizer) chooses the move with the highest score.
   - The human (Minimizer) is assumed to pick moves that minimize the AI’s score.

This ensures the AI makes the most optimal decisions possible.

---

## 🧱 Code Structure

- `insertLetter(letter, pos)`: Places an `X` or `O` at the given position.
- `spaceIsFree(pos)`: Checks if a position on the board is empty.
- `printBoard(board)`: Displays the current board.
- `isBoardFull(board)`: Returns `True` if all cells are filled.
- `isWinner(bo, le)`: Checks if the player with letter `le` has won.
- `minimax(board, depth, isMaximizing)`: The recursive Minimax algorithm.
- `aiMove()`: Finds and makes the best move using Minimax.
- `main()`: Controls the flow of the game (human vs. AI).

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed on your machine

### 💾 Installation

1. Clone the repository or download the `tictactoe.py` file.
2. Open a terminal and navigate to the project directory.

### ▶️ Running the Game

```bash
python tictactoe.py
🕵️ Example Gameplay
You play as X and AI plays as O

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Please select a position to place an 'X' (1-9): 5

1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
Continue playing until there is a winner or the board is full.
📝 Notes
This is a basic implementation of the Minimax algorithm.

It assumes the AI always plays optimally and instantly.

No depth-limiting or alpha-beta pruning is used (these could improve performance for more complex games).

Great for learning AI fundamentals and game algorithms.

📚 Future Improvements
Add GUI using tkinter or pygame

Support player vs. player mode

Implement Alpha-Beta pruning for optimization

Add difficulty levels by limiting Minimax depth

👨‍💻 Author
Made with ❤️ for learning and fun.

yaml
Copy
Edit

---

Let me know if you'd like to add badges, GitHub Actions, or convert it into a multi-file project with tests or GUI.







