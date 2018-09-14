from graphics import *
import time

win = GraphWin('Tic Tac Toe',600, 500) 
count=0
win.items=[]

def players():
    
    onePlayerB = Rectangle(Point(550,200), Point(350,300))
    onePlayerB.setOutline('black')
    onePlayerB.setFill('grey')
    onePlayerB.setWidth(1)
    onePlayerB.draw(win)

    onePlayerT = Text(Point(450,250), 'One-Player')
    onePlayerT.setTextColor('red')
    onePlayerT.setStyle('bold')
    onePlayerT.setSize(20)
    onePlayerT.draw(win)

    twoPlayerB = Rectangle(Point(250,200), Point(50,300))
    twoPlayerB.setOutline('black')
    twoPlayerB.setFill('grey')
    twoPlayerB.setWidth(1)
    twoPlayerB.draw(win)

    twoPlayerT = Text(Point(150,250), 'Two-Player')
    twoPlayerT.setTextColor('red')
    twoPlayerT.setStyle('bold')
    twoPlayerT.setSize(20)
    twoPlayerT.draw(win)


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

#Assigns a number to each square
def numberBoard():
    for i in range(9):
        win.items[i].setTextColor('red')
        win.items[i].setStyle('bold')
        win.items[i].setSize(15)
        win.items[i].draw(win)
def noBoard():
    for i in range(9):
        tile = Text(Point(120+(i%3)*100, 120+(i//3)*100), i+1)
        win.items.append(tile)

#Restart function        
def restart():
    count=0
    for i in range(9):
        win.items[i].setText(str(i+1))
        
#Exit function
def exit():
    win.close()
    raise SystemExit()
noBoard()
board()
