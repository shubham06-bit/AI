import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Rows, Columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    if check_winner(board, 'O'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for r, c in get_empty_cells(board):
        board[r][c] = 'X'
        score = minimax(board, 0, False)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    if move:
        board[move[0]][move[1]] = 'X'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print("You are 'O'. AI is 'X'. AI plays first.")
    ai_move(board)

    while True:
        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins! 😈")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Player move
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
        except ValueError:
            print("Please enter numbers.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, 'O'):
            print_board(board)
            print("You win! 🎉")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move(board)

# Run the game
play_game()