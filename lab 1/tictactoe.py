import random

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        row = board[3*i:3*i+3]
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for winner
def check_winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combinations)

# Get empty positions
def empty_positions():
    return [i for i in range(9) if board[i] == ' ']

# AI move logic
def ai_move():
    # Step 1: Win if possible
    for i in empty_positions():
        board_copy = board[:]
        board_copy[i] = 'X'
        if check_winner(board_copy, 'X'):
            return i

    # Step 2: Block opponent
    for i in empty_positions():
        board_copy = board[:]
        board_copy[i] = 'O'
        if check_winner(board_copy, 'O'):
            return i

    # Step 3: Take center
    if board[4] == ' ':
        return 4

    # Step 4: Take any corner
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i

    # Step 5: Take any side
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            return i

    return None

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are O, AI is X.")
    print_board()

    for turn in range(9):
        if turn % 2 == 0:
            print("AI's turn (X):")
            move = ai_move()
            if move is not None:
                board[move] = 'X'
        else:
            print("Your turn (O). Choose position (1-9):")
            move = None
            while move not in empty_positions():
                try:
                    move = int(input()) - 1
                    if move not in empty_positions():
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number from 1 to 9.")
            board[move] = 'O'

        print_board()

        if check_winner(board, 'X'):
            print("AI wins!")
            return
        elif check_winner(board, 'O'):
            print("You win!")
            return

    print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()
