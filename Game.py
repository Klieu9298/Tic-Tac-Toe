from graphics import *
import time

win = GraphWin('Tic Tac Toe',600, 500)
score=0
win.items=[]

#def players():

#    onePlayerB = Rectangle(Point(550,200), Point(350,300))
#    onePlayerB.setOutline('black')
#    onePlayerB.setFill('grey')
#    onePlayerB.setWidth(1)
#    onePlayerB.draw(win)
#    onePlayerT = Text(Point(450,250), 'One-Player')
#    onePlayerT.setTextColor('red')
#    onePlayerT.setStyle('bold')
#    onePlayerT.setSize(20)
#    onePlayerT.draw(win)

#    twoPlayerB = Rectangle(Point(250,200), Point(50,300))
#    twoPlayerB.setOutline('black')
#    twoPlayerB.setFill('grey')
#    twoPlayerB.setWidth(1)
#    twoPlayerB.draw(win)
#    twoPlayerT = Text(Point(150,250), 'Two-Player')
#    twoPlayerT.setTextColor('red')
#    twoPlayerT.setStyle('bold')
#    twoPlayerT.setSize(20)
#    twoPlayerT.draw(win)


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

#Make it so players can not choose the same square
def noBack():
    for i in range(9):
        tile = Text(Point(120+(i%3)*100, 120+(i//3)*100), i+1)
        win.items.append(tile)

#Assigns a number to each square
def numberBoard():
    for i in range(9):
        win.items[i].setTextColor('red')
        win.items[i].setStyle('bold')
        win.items[i].setSize(15)
        win.items[i].draw(win)

#Restart function
def restart():
    score = 0
    for i in range(9):
        win.items[i].setText(str(i+1))
    clear(win)
    gameOne()
    board()

#Exit function
def nowExit():
    win.close()
    raise SystemExit()

#Game results in a draw
def tieGame():
    results = Text(Point(300, 50), "Tie Game")
    results.setSize(20)
    results.setTextColor('black')
    results.setStyle('italic')
    results.draw(win)
    time.sleep(3)
    results.setText("")
    gameTwo()

#X is the winner
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

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    board()

def invalidChoice():
    results = Text(Point(250, 50), "Invalid Choice!")
    results.setSize(20)
    results.setTextColor('red')
    results.setStyle('italic')
    results.draw(win)
    time.sleep(3)
    results.setText("")

def winnerCheck():
    if (win.items[0].getText()==win.items[1].getText() and win.items[1].getText()==win.items[2].getText()):
        if win.items[0].getText()== 'X': Xwinner()
        elif win.items[0].getText()== 'O' : Owinner()
        return False
    elif (win.items[3].getText()==win.items[4].getText() and win.items[4].getText()==win.items[5].getText()):
        if win.items[3].getText()== 'X' : Xwinner()
        elif win.items[3].getText()== 'O' : Owinner()
        return False
    elif (win.items[6].getText()==win.items[7].getText() and win.items[7].getText()==win.items[8].getText()):
        if win.items[6].getText()== 'X' : Xwinner()
        elif win.items[6].getText()== 'O' : Owinner()
        return False
    elif (win.items[0].getText()==win.items[3].getText() and win.items[3].getText()==win.items[6].getText()):
        if win.items[0].getText()== 'X' : Xwinner()
        elif win.items[0].getText()== 'O' : Owinner()
        return False
    elif (win.items[1].getText()==win.items[4].getText() and win.items[4].getText()==win.items[7].getText()):
        if win.items[1].getText()== 'X' : Xwinner()
        elif win.items[1].getText()== 'O' : Owinner()
        return False
    elif (win.items[2].getText()==win.items[5].getText() and win.items[5].getText()==win.items[8].getText()):
        if win.items[2].getText()== 'X' : Xwinner()
        elif win.items[2].getText()== 'O' : Owinner()
        return False
    elif (win.items[0].getText()==win.items[4].getText() and win.items[4].getText()==win.items[8].getText()):
        if win.items[0].getText()== 'X' : Xwinner()
        elif win.items[0].getText()== 'O' : Owinner()
        return False
    elif (win.items[2].getText()==win.items[4].getText() and win.items[4].getText()==win.items[6].getText()):
        if win.items[2].getText()== 'X' : Xwinner()
        elif win.items[2].getText()== 'O' : Owinner()
        return False
    else :
        for i in range(9):
            if win.items[i].getText() not in ['X','O'] :
                return True
        tieGame()
        return False

def gameOne():
    while (winnerCheck()):
        playerButton=win.getMouse()
        if ( (playerButton.getX()>100 and playerButton.getX()<400) and (playerButton.getY()>100 and playerButton.getY()<400)):
            X=int((playerButton.getX()-100)//100)
            Y=int((playerButton.getY()-100)//100)
            global score
            if not (win.items[Y*3+X].getText()=='X') and not (win.items[Y*3+X].getText()=='O') :
                if score%2==0 : win.items[Y*3+X].setText('X')
                else : win.items[Y*3+X].setText('O')
                score+=1
                clear(win)

            else :
                invalidChoice()
        elif ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>160 and playerButton.getY()<190)) :
            restart ()
        elif ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>310 and playerButton.getY()<340)) :
            nowExit ()

def gameTwo():
    playerButton=win.getMouse()
    if ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>160 and playerButton.getY()<190)) :
        restart ()
    elif ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>310 and playerButton.getY()<340)) :
        nowExit ()
    else :
        clear(win)
        playerButton=win.getMouse()
        if ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>160 and playerButton.getY()<190)) :
            restart ()
        elif ((playerButton.getX()>440 and playerButton.getX()<560) and (playerButton.getY()>310 and playerButton.getY()<340)) :
            nowExit ()
        else :
            gameTwo()

noBack()
board()
gameOne()
