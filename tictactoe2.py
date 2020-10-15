def printBoard():
    print(board[1] +  ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def isWinner(letter):
    return((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[8] == letter and board[5] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[7] == letter and board[5] == letter and board[7] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter))

def moveplayer1():
    while True:
        move = int(input('Please select a position to place an O (1-9):'))
        if isSpaceFree(move):
            print("Success!")
            insertBoard(move,'O')
            printBoard()
            break
        else:
            print('The position is occupied, pick a new one!')
def moveplayer2():
    while True:
        move = int(input('Please select a position to place an O (1-9):'))
        if isSpaceFree(move):
            print("Success!")
            insertBoard(move,'X')
            printBoard()
            break
        else:
            print('The position is occupied, pick a new one!')    

def isSpaceFree(move):
    return board[move]==' '

def insertBoard(move, letter):
    board[move]=letter

board=[' ' for x in range(10)]
print("Welcome to Tic Tac Toe")
printBoard()
while True:
    moveplayer1() 
    if isWinner('O'):
        print('O win !')
        break
    if board.count(' ') <= 1:
        print('Game is a tie! No more spaces left to move.')
        break 
    moveplayer2()   
    if isWinner('X'):
        print('X win !')
        break
    