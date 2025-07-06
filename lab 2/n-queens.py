def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens_util(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack
    return False

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print(f"No solution exists for N = {n}")
        return

    print(f"One solution for N = {n}:\n")
    for row in board:
        print(" ".join('Q' if cell else '.' for cell in row))
    print("\n" + "-" * (2 * n - 1) + "\n")

# Solve for N = 4 to 8
for n in range(4, 9):
    solve_nqueens(n)
