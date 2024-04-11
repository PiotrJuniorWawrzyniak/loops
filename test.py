board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

computer = 'x'
player = 'o'
winner = None
game_running = True
current_player = None


def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('=========')


def player_input(board):
    inp = int(input('Wybierz pole 1-9: '))
    if board[inp - 1] == "-":
        board[inp - 1] = player
    else:
        print('Blad!')


def check_horizontally(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_vertically(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[3]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[2]
        return True


def check_winning(board):
    global game_running
    if check_horizontally(board):
        print_board(board)
        if winner == 'x':
            print('Przegrales!')
        else:
            print('Wygrales!')
        game_running = False

    elif check_vertically(board):
        print_board(board)
        if winner == 'x':
            print('Przegrales!')
        else:
            print('Wygrales!')
        game_running = False

    elif check_diagonally(board):
        print_board(board)
        if winner == 'x':
            print('Przegrales!')
        else:
            print('Wygrales!')
        game_running = False


def check_draw(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('Remis!')
        game_running = False


def switch_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'


def get_move(board):
    if board[4] == '-':
        return 4
    if board[0] == 'o':
        return 2
    if board[2] == 'o':
        return 8
    if board[6] == 'o':
        return 3
    if board[8] == 'o':
        return 7
    if board[1] == 'o':
        return 5
    if board[3] == 'o':
        return 2
    if board[5] == 'o':
        return 0
    if board[7] == 'o':
        return 7


def computer_move(board):
    global computer
    computer_position = get_move(board)
    board[computer_position] = computer
    print_board(board)


def make_move(board):
    if current_player == 'x':
        player_input(board)
    else:
        computer_move(board)
    switch_player()


while game_running:
    make_move(board)
    check_winning(board)
    check_draw(board)
