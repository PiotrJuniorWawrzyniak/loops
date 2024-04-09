import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

computer = 'X'
player = 'O'
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
        if winner == 'X':
            print('Przegrales!')
        else:
            print('Wygrales!')
        game_running = False

    elif check_vertically(board):
        print_board(board)
        if winner == 'X':
            print('Przegrales!')
        else:
            print('Wygrales!')
        game_running = False

    elif check_diagonally(board):
        print_board(board)
        if winner == 'X':
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
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def get_move(board):
    if board[0] == 'x' and board[1] == 'x' and not board[2]:
        return 2
    elif board[0] == 'x' and board[2] == 'x' and not board[1]:
        return 1
    elif board[1] == 'x' and board[2] == 'x' and not board[0]:
        return 0
    elif board[3] == 'x' and board[4] == 'x' and not board[5]:
        return 5
    elif board[3] == 'x' and board[5] == 'x' and not board[4]:
        return 4
    elif board[4] == 'x' and board[5] == 'x' and not board[3]:
        return 3
    elif board[6] == 'x' and board[7] == 'x' and not board[8]:
        return 8
    elif board[6] == 'x' and board[8] == 'x' and not board[7]:
        return 7
    elif board[7] == 'x' and board[8] == 'x' and not board[6]:
        return 6
    elif board[0] == 'x' and board[3] == 'x' and not board[6]:
        return 6
    elif board[0] == 'x' and board[6] == 'x' and not board[3]:
        return 3
    elif board[3] == 'x' and board[6] == 'x' and not board[0]:
        return 0
    elif board[1] == 'x' and board[4] == 'x' and not board[7]:
        return 7
    elif board[1] == 'x' and board[7] == 'x' and not board[4]:
        return 4
    elif board[4] == 'x' and board[7] == 'x' and not board[1]:
        return 1
    elif board[2] == 'x' and board[5] == 'x' and not board[8]:
        return 8
    elif board[2] == 'x' and board[8] == 'x' and not board[5]:
        return 5
    elif board[5] == 'x' and board[8] == 'x' and not board[2]:
        return 2
    elif board[0] == 'x' and board[5] == 'x' and not board[8]:
        return 8
    elif board[0] == 'x' and board[8] == 'x' and not board[4]:
        return 4
    elif board[4] == 'x' and board[8] == 'x' and not board[0]:
        return 0
    elif board[2] == 'x' and board[4] == 'x' and not board[6]:
        return 6
    elif board[2] == 'x' and board[6] == 'x' and not board[4]:
        return 4
    elif board[6] == 'x' and board[4] == 'x' and not board[2]:
        return 2
    return random.choice([i for i in range(9) if board[i] == "-"])


def computer_move(board):
    global computer
    computer_position = get_move(board)
    board[computer_position] = computer
    print_board(board)


def make_move(board):
    if current_player == 'X':
        player_input(board)
    else:
        computer_move(board)
    switch_player()


while game_running:
    make_move(board)
    check_winning(board)
    check_draw(board)
