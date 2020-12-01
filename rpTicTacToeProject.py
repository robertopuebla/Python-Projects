var = [' ' for _ in range(9)]
turn_counter = 1
stop = False
win_pos = [var[0:3], var[3:6], var[6:9],
           var[0:7:3], var[1:8:3], var[2:9:3],
           var[0:9:4], var[2:7:2]]
board = [
    [var[6], var[3], var[0]],
    [var[7], var[4], var[1]],
    [var[8], var[5], var[2]],
]


def board_display():
    print("---------")
    print("|", board[0][2], board[1][2], board[2][2], "|")
    print("|", board[0][1], board[1][1], board[2][1], "|")
    print("|", board[0][0], board[1][0], board[2][0], "|")
    print("---------")


def next_move():
    while True:  # fake assumption - we need it to enter the loop:
        move = input("Enter your move: ")
        coordinates = move.split()
        col = int(coordinates[0]) - 1
        row = int(coordinates[1]) - 1
        global turn_counter
        global board
        if coordinates[0].isalpha() or coordinates[1].isalpha():
            print('You should enter numbers!')
        elif col < 0 or col > 2 or row < 0 or row > 2:
            print('Coordinates should be from 1 to 3!')
        elif board[col][row] != ' ':
            print('This cell is occupied! Choose another one!')
        elif 0 <= col <= 2 and 0 <= row <= 2:
            if turn_counter % 2 != 0:
                board[col][row] = 'X'
                turn_counter += 1
                break
            else:
                board[col][row] = 'O'
                turn_counter += 1
                break


def update_var():
    global win_pos
    var[6] = board[0][2]
    var[3] = board[1][2]
    var[0] = board[2][2]
    var[7] = board[0][1]
    var[4] = board[1][1]
    var[1] = board[2][1]
    var[8] = board[0][0]
    var[5] = board[1][0]
    var[2] = board[2][0]
    win_pos = [var[0:3], var[3:6], var[6:9],
               var[0:7:3], var[1:8:3], var[2:9:3],
               var[0:9:4], var[2:7:2]]


def game_state():
    global stop
    global var
    global win_pos
    if var.count("X") - var.count("O") >= 2 or var.count("X") - var.count("O") <= -2:
        print("Impossible")
        stop = True
    elif win_pos.count(['X', 'X', 'X']) + win_pos.count(['O', 'O', 'O']) >= 2:
        print("Impossible")
        stop = True
    elif ['X', 'X', 'X'] in win_pos:
        print("X wins")
        stop = True
    elif ['O', 'O', 'O'] in win_pos:
        print("O wins")
        stop = True
    elif var.count(" ") > 0:
        print("Game not finished")
        stop = False
    elif var.count(" ") == 0:
        print("Draw")
        stop = True


def keep_going():
    next_move()
    board_display()
    update_var()
    game_state()


board_display()
keep_going()

while True:
    if stop:
        break
    else:
        keep_going()
