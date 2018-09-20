from graphics import *
import time

win = GraphWin('Tic Tac Toe',600, 500)
score=0
win.items=[]

def board():
    #restart Button
    reBut = Rectangle(Point(440,160), Point(560,190))
    reBut.setOutline('black')
    reBut.setFill('grey')
    reBut.setWidth(1)
    reBut.draw(win)
    reText = Text(Point(500,175), 'Restart')
    reText.setTextColor('red')
    reText.setStyle('bold')
    reText.setSize(10)
    reText.draw(win)

    #Exit Button
    exBut = Rectangle(Point(440,310), Point(560,340))
    exBut.setOutline('black')
    exBut.setFill('grey')
    exBut.setWidth(1)
    exBut.draw(win)
    exText = Text(Point(500,325), 'Exit')
    exText.setTextColor('red')
    exText.setStyle('bold')
    exText.setSize(10)
    exText.draw(win)

    #Largest Rectangle of board
    RectangleOne = Rectangle(Point(100,100), Point(400,400))
    RectangleOne.setOutline('black')
    RectangleOne.setFill('grey')
    RectangleOne.setWidth(3)
    RectangleOne.draw(win)

    #Top horizontal line
    horizontalOne = Line(Point(100, 200), Point(400, 200)) # set endpoints
    horizontalOne.setOutline('black')
    horizontalOne.setWidth(3)
    horizontalOne.draw(win)

    #Bottom horizontal line
    horizontalTwo = Line(Point(100, 300), Point(400, 300)) # set endpoints
    horizontalTwo.setOutline('black')
    horizontalTwo.setWidth(3)
    horizontalTwo.draw(win)

    #Middle left verticle line
    verticleOne = Line(Point(200, 100), Point(200, 400)) # set endpoints
    verticleOne.setOutline('black')
    verticleOne.setWidth(3)
    verticleOne.draw(win)

    #Middle right verticle line
    verticleTwo = Line(Point(300, 100), Point(300, 400)) # set endpoints
    verticleTwo.setOutline('black')
    verticleTwo.setWidth(3)
    verticleTwo.draw(win)

    numberBoard()

def first():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter
def tieGame():
    results = Text(Point(300, 50), "Tie Game")
    results.setSize(20)
    results.setTextColor('black')
    results.setStyle('italic')
    results.draw(win)
    time.sleep(3)
    results.setText("")
    gameTwo()
def Xwinner():
    results = Text(Point(300, 50), "X is the winner!!")
    results.setSize(20)
    results.setTextColor('black')
    results.setStyle('bold')
    results.draw(win)
    time.sleep(3)
    results.setText("")
    gameTwo()

#O is the winner
def Owinner():
    results = Text(Point(300, 50),  "O is the winner!!")
    results.setSize(20)
    results.setTextColor('black')
    results.setStyle('bold')
    results.draw(win)
    time.sleep(3)
    gameTwo()
def getBoardCopy(board):

    dBoard = []

    for i in board:
        dBoard.append(i)

    return dBoard

def isSpaceFree(board, move):
    
    return board[move] == ' '

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


