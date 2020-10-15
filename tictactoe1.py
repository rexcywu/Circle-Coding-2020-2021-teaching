
print("Welcome to Tic Tac Toe")
#board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board=[' ' for x in range(10)]
print(board[1] + ' | ' + board[2] + ' | ' + board[3])
print('-----------')
print(board[4] + ' | ' + board[5] + ' | ' + board[6])
print('-----------')
print(board[7] + ' | ' + board[8] + ' | ' + board[9])

while True:
    while (True):
        move = input('Please select a position to place an O (1-9):')
        if (board[move]==' '):
            print("Success!")
            board[move]='O'
            print(board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('-----------')
            print(board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('-----------')
            print(board[7] + ' | ' + board[8] + ' | ' + board[9])
            break
        else:
            print('The position is occupied, pick a new one!')    
    if((board[7]=='O' and board[8]=='O' and board[9]=='O') or
        (board[4]=='O' and board[5]=='O' and board[6]=='O') or 
        (board[1]=='O' and board[2]=='O' and board[3]=='O') or
        (board[1]=='O' and board[4]=='O' and board[7]=='O') or
        (board[2]=='O' and board[8]=='O' and board[5]=='O') or
        (board[3]=='O' and board[6]=='O' and board[9]=='O') or
        (board[7]=='O' and board[5]=='O' and board[7]=='O') or
        (board[1]=='O' and board[5]=='O' and board[9]=='O')):
        print('O win !')
        break
    if (board.count(' ') <= 1):
        print('Game is a tie! No more spaces left to move.')
        break 
    run = True
    while (run):
        move = input('Please select a position to place an X (1-9): ')
        if (board[move]==' '):
            run = False
            print("Success!")
            board[move]='X'
            print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('-----------')
            print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('-----------')
            print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        else:
            print('The position is occupied, pick a new one!')    
    if((board[7]=='X' and board[8]=='X' and board[9]=='X') or
        (board[4]=='X' and board[5]=='X' and board[6]=='X') or 
        (board[1]=='X' and board[2]=='X' and board[3]=='X') or
        (board[1]=='X' and board[4]=='X' and board[7]=='X') or
        (board[2]=='X' and board[8]=='X' and board[5]=='X') or
        (board[3]=='X' and board[6]=='X' and board[9]=='X') or
        (board[7]=='X' and board[5]=='X' and board[7]=='X') or
        (board[1]=='X' and board[5]=='X' and board[9]=='X')):
        print('X win !')
        break
    