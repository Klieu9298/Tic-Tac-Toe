from graphics import *
import time

print("Please Choose an Option\n")
print("Press any Empty Space to exit\n")

def main():
    win = GraphWin('Tic Tac Toe',500, 500)
    
    win.items=[]

    exText = Text(Point(250,20), 'Please Choose an Option')
    exText.setTextColor('black')
    exText.setSize(15)
    exText.draw(win)

    exText = Text(Point(250,40), 'To exit, click any white space')
    exText.setTextColor('black')
    exText.setSize(15)
    exText.draw(win)
    
    #Two-Player
    exBut = Rectangle(Point(180,90), Point(330,180))
    exBut.setOutline('black')
    exBut.setFill('grey')
    exBut.setWidth(1)
    exBut.draw(win)
    exText = Text(Point(255,135), 'Two-Player')
    exText.setTextColor('red')
    exText.setStyle('bold')
    exText.setSize(20)
    exText.draw(win)

    #Single Player
    exBut = Rectangle(Point(180,230), Point(330,320))
    exBut.setOutline('black')
    exBut.setFill('grey')
    exBut.setWidth(1)
    exBut.draw(win)
    exText = Text(Point(255,271), 'Single-Player')
    exText.setTextColor('red')
    exText.setStyle('bold')
    exText.setSize(20)
    exText.draw(win)

    #Custom
    exBut = Rectangle(Point(180,370), Point(330,460))
    exBut.setOutline('black')
    exBut.setFill('grey')
    exBut.setWidth(1)
    exBut.draw(win)
    exText = Text(Point(255,410), 'Customization')
    exText.setTextColor('red')
    exText.setStyle('bold')
    exText.setSize(20)
    exText.draw(win)

    


main()
