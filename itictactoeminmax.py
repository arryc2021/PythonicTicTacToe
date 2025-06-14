import random

# The game board
board = [' ' for _ in range(9)]

# Function to insert a letter in the board
def insertLetter(letter, pos):
    board[pos] = letter
    return

# Function to check if a space is free
def spaceIsFree(pos):
    return board[pos] == ' '

# Function to print the board
def printBoard(board):
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]}')

# Function to check if the board is full
def isBoardFull(board):
    return board.count(' ') == 0

# Function to check for a win
def isWinner(board, le):
    return ((board[6] == le and board[7] == le and board[8] == le) or 
    (board[3] == le and board[4] == le and board[5] == le) or 
    (board[0] == le and board[1] == le and board[2] == le) or 
    (board[6] == le and board[3] == le and board[0] == le) or 
    (board[7] == le and board[4] == le and board[1] == le) or 
    (board[8] == le and board[5] == le and board[2] == le) or 
    (board[6] == le and board[4] == le and board[2] == le) or 
    (board[8] == le and board[4] == le and board[0] == le))

# The minimax function
def minimax(board, depth, isMaximizing):
    if isWinner(board, 'X'):
        return -10 + depth
    elif isWinner(board, 'O'):
        return 10 - depth
    elif isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(len(board)):
            if spaceIsFree(i):
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(len(board)):
            if spaceIsFree(i):
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# The AI function
def aiMove(board):
    bestScore = -1000
    bestMove = 0
    for i in range(len(board)):
        if spaceIsFree(i):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    insertLetter('O', bestMove)
    return

# Main game loop
def main():
    print("You play as X and AI plays as O")
    printBoard(board)

    while not(isBoardFull(board)):
        move = input("Please select a position to place an 'X' (1-9): ")
        if spaceIsFree(int(move) - 1):
            insertLetter('X', int(move) - 1)
            printBoard(board)

            if isWinner(board, 'X'):
                print("You win! Congratulations!")
                break

            aiMove(board)
            printBoard(board)

            if isWinner(board, 'O'):
                print("AI wins! Better luck next time!")
                break
        else:
            print("Sorry, this space is occupied!")

    if isBoardFull(board):
        print("Tie Game!")

main()