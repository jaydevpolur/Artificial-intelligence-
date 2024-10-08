import random

board = [[" " for i in range(3)] for j in range(3)]

def display_board():
    for i in range(3):
        print(board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        print("---------")

def check_win(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def human_move():
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("Cell already taken, try again.")

def bot_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

while True:
    display_board()
    human_move()
    if check_win("X"):
        display_board()
        print("Congratulations! You win!")
        break
    if check_draw():
        display_board()
        print("It's a draw!")
        break

    bot_move()
    if check_win("O"):
        display_board()
        print("Bot wins! Better luck next time.")
        break
    if check_draw():
        display_board()
        print("It's a draw!")
        break
11
