import math

# Display the board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


# Check whether a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Check whether the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)


# Minimax algorithm
def minimax(board, is_maximizing):
    # Computer wins
    if check_winner(board, "O"):
        return 1

    # Human wins
    if check_winner(board, "X"):
        return -1

    # Draw
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"

                    score = minimax(board, False)

                    board[i][j] = " "

                    best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"

                    score = minimax(board, True)

                    board[i][j] = " "

                    best_score = min(best_score, score)

        return best_score


# Find the best move for the computer
def computer_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"

                score = minimax(board, False)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


# Main game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("TIC-TAC-TOE")
    print("You are X")
    print("Computer is O")

    while True:
        print_board(board)

        # Human move
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Try again.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied. Try again.")
                continue

        except ValueError:
            print("Please enter numbers only.")
            continue

        board[row][col] = "X"

        # Check human win
        if check_winner(board, "X"):
            print_board(board)
            print("You WIN!")
            break

        # Check draw
        if is_full(board):
            print_board(board)
            print("DRAW!")
            break

        # Computer move
        print("Computer is thinking...")

        row, col = computer_move(board)
        board[row][col] = "O"

        # Check computer win
        if check_winner(board, "O"):
            print_board(board)
            print("Computer WINS!")
            break

        # Check draw
        if is_full(board):
            print_board(board)
            print("DRAW!")
            break


# Start the game
play_game()