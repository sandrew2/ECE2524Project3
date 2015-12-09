import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


def getPlayerLetter():
    letter = raw_input("What letter do you want to be? x or o")
    while letter != 'x' and letter != 'o':
        letter = raw_input('That was not a valid letter! Pick again')
    if letter == 'x':
        return ['x', 'o']
    else:
        return ['o', 'x']

def getPlayerMove(board, letter):
    move = raw_input("Where do you want to move? (1-9)")
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isValidMove(board, int(move)):
        move = raw_input('That was not a valid move! Pick again')
    board[int(move)] = letter

def isValidMove(board, move):
    return (board[int(move)] == ' ')

def getComputerMove(board, completter, playerletter):
    validMoves = []
    for i in range(1, 10):
        if isValidMove(board, i):
            validMoves.append(i)
    for i in validMoves:
        board[i] = completter
        if checkWin(board, completter):
            moved = True
            return
        else:
            board[i] = ' '
    for i in validMoves:
        board[i] = playerletter
        if checkWin(board, playerletter):
            board[i] = completter
            moved = True
            return
        else:
            board[i] = ' '
    move = int(validMoves[random.randrange(len(validMoves))])
    board[int(move)] = completter

def peekBoard(board):
    tempBoard = []
    for i in board:
        tempBoard.append(i)
    return tempBoard

def checkWin(board, letter):
    return ((board[1] == letter and (
    (board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[7] == letter)))
    or (board[9] == letter and (
    (board[8] == letter and board[7] == letter) or
    (board[6] == letter and board[3] == letter)))
    or (board[5] == letter and (
    (board[1] == letter and board[9] == letter) or
    (board[7] == letter and board[3] == letter)or
    (board[4] == letter and board[6] == letter)or
    (board[2] == letter and board[8] == letter))))

def checkTie(board):
    for i in range(1,10):
        if isValidMove(board, i):
            return False
    return True


def playAgain():
     # This function returns True if the player wants to play again, otherwise it returns False.
    again = raw_input('Do you want to play again? (yes or no)')
    return again.startswith('y')


def playGame():
    while True:
        theBoard = [' '] * 10
        playerletter, computerletter = getPlayerLetter()
        if playerletter == 'x':
            turn = 'player'
        else:
            turn = 'computer'
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                getPlayerMove(theBoard, playerletter)
                if checkWin(theBoard, playerletter):
                    drawBoard(theBoard)
                    print('You Win!')
                    gameIsPlaying = False
                else:
                    if checkTie(theBoard):
                        drawBoard(theBoard)
                        print('Tie')
                        gameIsPlaying = False
                        break
                    else:
                        turn = 'computer'
            if turn == 'computer':
                getComputerMove(theBoard, computerletter, playerletter)
                if checkWin(theBoard, computerletter):
                    drawBoard(theBoard)
                    print('Sorry, you Lose')
                    gameIsPlaying = False
                else:
                    if checkTie(theBoard):
                        drawBoard(theBoard)
                        print('It was a Tie')
                        gameIsPlaying = False
                        break
                    else:
                        turn = 'player'
        if not playAgain():
            break
