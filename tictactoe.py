import random

def drawBoard(board):
   

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputPlayerLetter():
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

   
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def first():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def again():
   
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def winner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):

    dBoard = []

    for i in board:
        dBoard.append(i)

    return dBoard

def isSpaceFree(board, move):
    
    return board[move] == ' '

def getPlayerMove(board):
    
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What move will you make? \nPlease enter a number 1-9 to make your move: ')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
  
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, cLetter):
    
    if cLetter == 'X':
        pLetter = 'O'
    else:
        pLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, cLetter, i)
            if winner(copy, cLetter):
                return i

    
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, pLetter, i)
            if winner(copy, pLetter):
                return i

    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    
    if isSpaceFree(board, 5):
        return 5

    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
   
    theBoard = [' '] * 10
    pLetter, cLetter = inputPlayerLetter()
    turn = first()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, pLetter, move)

            if winner(theBoard, pLetter):
                drawBoard(theBoard)
                print('YAY! YOU WON!')
                playing = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
           
            move = getComputerMove(theBoard, cLetter)
            makeMove(theBoard, cLetter, move)

            if winner(theBoard, cLetter):
                drawBoard(theBoard)
                print('The computer wins! You lose.')
                playing = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not again():
        break
