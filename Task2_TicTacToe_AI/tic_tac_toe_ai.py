import math

def print_board(board):
    for row in board:
        print("|", " | ".join(row), "|")
    print()

def check_winner(board):
    winning_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    if ["X", "X", "X"] in winning_states:
        return "X"
    if ["O", "O", "O"] in winning_states:
        return "O"
    return None

def empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                cells.append((i, j))
    return cells

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    if len(empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe (You = X, AI = O)\n")

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("🎉 You WIN!")
            break

        if len(empty_cells(board)) == 0:
            print_board(board)
            print("It's a DRAW!")
            break

        (ai_row, ai_col) = best_move(board)
        board[ai_row][ai_col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("💻 AI WINS!")
            break

        if len(empty_cells(board)) == 0:
            print_board(board)
            print("It's a DRAW!")
            break

play_game()
