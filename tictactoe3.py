def printBoard(board):
    print(board[1] +  ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def isWinner(board, letter):
    return((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[8] == letter and board[5] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[7] == letter and board[5] == letter and board[7] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter))

def moveplayer1(board, playerChoice):
    while True:
        move = int(input('Please select a position to place an O (1-9):'))
        if isSpaceFree(board, move):
            print("Success!")
            insertBoard(board, move, playerChoice)
            printBoard(board)
            break
        else:
            print('The position is occupied, pick a new one!')
def moverandom(board, compChoice):
    import random
    while True:
        move = random.randrange(1,10)
        if isSpaceFree(board, move):
            insertBoard(board, move, compChoice)
            printBoard(board)
            break
        else:
            print('The position is occupied, pick a new one!')    

def isSpaceFree(board, move):
    return board[move]==' '

def insertBoard(board, move, letter):
    board[move]=letter

def main():
    board=[' ' for x in range(10)]
    # Addition feature 2: To make player choose 'O' , 'X' 
    print("Welcome to Tic Tac Toe")
    playerChoice = input('Do you want to choose O or X ?\n')
    compChoice = 'X' 
    while True:
        if playerChoice == 'O':
            compChoice = 'X'
            break
        elif playerChoice == 'X':
            compChoice = 'O'
            break
        else:
            playerChoice = input("Invalid input, please choose again!\n")
    printBoard(board)
    while True:
        moveplayer1(board, playerChoice) 
        if isWinner(board, playerChoice):
            print(playerChoice + ' win !\n')
            break
        if board.count(' ') <= 1:
            print('Game is a tie! No more spaces left to move.\n')
            break 
        moverandom(board, compChoice)   
        if isWinner(board,compChoice):
            print(compChoice + ' win !\n')
            break

main()
# Addition feature 1: To make player decide whether want to replay it or not 
while True:
    answer = input('Do you want to play again? (Y/N)\n')
    if answer.lower() == 'y' or answer.lower == 'yes':
        print('-----------------------------------')
        main()
    else:
        break    