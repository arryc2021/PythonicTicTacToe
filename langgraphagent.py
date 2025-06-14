from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from typing import TypedDict, Literal, List, Optional
import random

# 1. Game state definition
class GameState(TypedDict):
    board: List[str]
    turn: Literal["X", "O"]
    winner: Optional[Literal["X", "O", "Draw"]]
    moves: int

# 2. Initial state
def initial_state() -> GameState:
    return {
        "board": [" " for _ in range(9)],
        "turn": "X",
        "winner": None,
        "moves": 0
    }

# 3. Print board with numbers for empty spots
def print_board(board: List[str]):
    display = [board[i] if board[i] != " " else str(i + 1) for i in range(9)]
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        print(f" {display[i]} | {display[i+1]} | {display[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

# 4. Human move
def human_move(state: GameState) -> GameState:
    board = state["board"]
    print_board(board)
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")
    state["board"] = board
    state["moves"] += 1
    return state

# 5. AI move with rule-based priority
def ai_move(state: GameState) -> GameState:
    board = state["board"]

    def check_line(a, b, c, player):
        line = [board[a], board[b], board[c]]
        return line.count(player) == 2 and line.count(" ") == 1

    def find_winning_move(player):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combos:
            if check_line(a, b, c, player):
                for i in [a, b, c]:
                    if board[i] == " ":
                        return i
        return None

    move = find_winning_move("O")
    if move is not None:
        board[move] = "O"
        print(f"AI (O) plays to win at position {move + 1}")
    else:
        move = find_winning_move("X")
        if move is not None:
            board[move] = "O"
            print(f"AI (O) blocks at position {move + 1}")
        elif board[4] == " ":
            board[4] = "O"
            print("AI (O) takes center (5)")
        else:
            corners = [i for i in [0, 2, 6, 8] if board[i] == " "]
            if corners:
                move = random.choice(corners)
                board[move] = "O"
                print(f"AI (O) takes corner at position {move + 1}")
            else:
                sides = [i for i in [1, 3, 5, 7] if board[i] == " "]
                if sides:
                    move = random.choice(sides)
                    board[move] = "O"
                    print(f"AI (O) takes side at position {move + 1}")

    state["board"] = board
    state["moves"] += 1
    print_board(board)
    return state

# 6. Check winner or draw with debug print
def check_winner(state: GameState) -> GameState:
    board = state["board"]
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            state["winner"] = board[a]
            print(f"Winner detected: {state['winner']}")
            return state
    if state["moves"] == 9:
        state["winner"] = "Draw"
        print("Game ended in a draw.")
    return state

# 7. Switch turns
def switch_turn(state: GameState) -> GameState:
    state["turn"] = "O" if state["turn"] == "X" else "X"
    return state

# 8. End game display
def game_over(state: GameState) -> GameState:
    print_board(state["board"])
    if state["winner"] == "Draw":
        print("Game ended in a draw.")
    else:
        print(f"Player {state['winner']} wins!")
    return state

# 9. Decide whose turn it is
def move_router(state: GameState) -> str:
    return "human_move" if state["turn"] == "X" else "ai_move"

# 10. Build graph and add nodes
graph = StateGraph(state_schema=GameState)

graph.add_node("move", RunnableLambda(lambda x: x))  # Router node
graph.add_node("human_move", RunnableLambda(human_move))
graph.add_node("ai_move", RunnableLambda(ai_move))
graph.add_node("check_winner", RunnableLambda(check_winner))
graph.add_node("switch_turn", RunnableLambda(switch_turn))
graph.add_node("game_over", RunnableLambda(game_over))

# 11. Edges and conditional routing
graph.add_conditional_edges("move", move_router, {
    "human_move": "human_move",
    "ai_move": "ai_move"
})

graph.add_edge("human_move", "check_winner")
graph.add_edge("ai_move", "check_winner")

graph.add_conditional_edges(
    "check_winner",
    lambda state: END if state["winner"] else "switch_turn"
)

graph.add_edge("switch_turn", "move")

graph.set_entry_point("move")
graph.set_finish_point("game_over")

# 12. Run the game with increased recursion limit
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("You are X. AI is O.")
    app = graph.compile()
    state = initial_state()
    app.invoke(state)
