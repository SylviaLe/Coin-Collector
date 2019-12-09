from coin import *
from graphics import *
from CoinCollector import *
from player import *
from button import *

def intro():
    intwin = GraphWin("Welcome to CoinCollector", 1000,600)
    intwin.setCoords(0,0,400,400)
    #Designs
    background = Image(Point(200,200),"coin-collection.png")
    background.draw(intwin)

    gamename = Text(Point(200,300), "Coin Collector")
    gamename.setSize(36)
    gamename.setTextColor("red")
    gamename.setFace("century")
    gamename.draw(intwin)
    
    start = Button(intwin, Point(200,230),50,25,"Start")
    Quit = Button(intwin, Point(200,170),50,25, "Quit")
    rule = Button(intwin, Point(200,200), 50, 25, "Rules")

    pt = intwin.getMouse()
    while not Quit.isClicked(pt):
        if start.isClicked(pt):
            intwin.close()
            main()
            break
        elif rule.isClicked(pt):
            rules()
        pt= intwin.getMouse()
    intwin.close()

def rules():
    rulewin = GraphWin("CoinCollector Rules", 400,400)
    rulewin.setCoords(0,0,200,200)
    #Design
    design = Image(Point(100,100), "rules background.png")
    design.draw(rulewin)

    line1 = Text(Point(100,150),"- Use 'up', 'down', 'left', or 'right' key\nto move the character around to collect coins.")
    line1.setSize(14)
    line1.setFace("calibri")
    line1.draw(rulewin)
    
    line2 = Text(Point(100,130),"- Coins are randomly generated.")
    line2.setSize(14)
    line2.setFace("calibri")
    line2.draw(rulewin)
    
    line3 = Text(Point(100,110),"- Goal of this game is to collect\n all the coins ASAP.")
    line3.setSize(14)
    line3.setFace("calibri")
    line3.draw(rulewin)
    
    title = Text(Point(100,175), "Rules")
    title.setSize(30)
    title.setTextColor('black')
    title.setFace('century')
    title.setStyle('bold')
    title.draw(rulewin)


def main():
    win = GraphWin("CoinCollector", 600,600)
    win.setBackground("green")
    #Randomly draw bush
    game = CoinCollector(win)
    game.play(win)
    
intro()
