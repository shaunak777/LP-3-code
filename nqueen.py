# 8-Queens Problem using Backtracking
N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_queens(board, row):
    if row == N:
        print("Final 8-Queens Matrix:")
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack
    return False

# --- Main program ---
board = [[0 for _ in range(N)] for _ in range(N)]

# Take first queen position input
r = int(input("Enter the row (0-7) for first Queen: "))
c = int(input("Enter the column (0-7) for first Queen: "))

board[r][c] = 1  # Place first queen

# Solve starting from next row
if not solve_queens(board, r + 1):
    print("Solution not possible with this starting position.")
