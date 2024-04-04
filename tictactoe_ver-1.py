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


def player_input(board):
    inp = int(input('Wybierz pole 1-9: '))
    if board[inp-1] == "-":
        board[inp-1] = player
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


def computer_move(board):
    global computer
    computer_position = random.choice([i for i in range(9) if board[i] == "-"])
    board[computer_position] = computer
    print_board(board)
    switch_player()


while game_running:
    computer_move(board)
    switch_player()
    player_input(board)
    check_winning(board)
    check_draw(board)

# 1. Pominalem wyswietlenie planszy na poczatku, poniewaz dwie plansze jedna
#    pod druga byly nieczytelne. Od razu zaczyna komputer.

# 2. Komputer niestety moze przegrac, czyli nie gra optymalnie.

# 3. W przypadku remisu, gdy wszystkie pola sa juz zajete, uzytkownik i tak
#    musi wybrac dowolne pole, zeby program wyswietlil 'Remis' i zakonczyl
#    dzialanie.

# 4. Problem jest tez w przypadku porazki uzytkownika, program najpierw
#    wyswietla informacje 'Przegrales', a nastepnie te sama plansze z
#    informacja 'Remis'.
