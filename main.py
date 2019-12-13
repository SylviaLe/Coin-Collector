from coin import *
from graphics import *
from player import *
from button import *
import time

def intro():
    #Introduction of our game
    
    intwin = GraphWin("Welcome to CoinCollector", 600,600)
    intwin.setCoords(0,0,400,400)
    #Designs
    background = Image(Point(200,200),"intro.png")
    background.draw(intwin)

    gamename = Text(Point(200,300), "Coin Collector")
    gamename.setSize(40)
    gamename.setTextColor(color_rgb(255, 240, 214))
    gamename.setFace("calibri")
    gamename.setStyle('bold')
    gamename.draw(intwin)
    
    #Buttons for users to choose what to do
    start = Button(intwin, Point(200,230),75,25,"Start")
    rule = Button(intwin, Point(200,200), 75, 25, "Rules")
    Quit = Button(intwin, Point(200,170),75,25, "Quit")
    lead = Button(intwin, Point(200, 140), 75, 25, 'Leaderboard')

    pt = intwin.getMouse()
    while not Quit.isClicked(pt):
        if start.isClicked(pt): #Start the game
            intwin.close()
            main()
            break
        elif rule.isClicked(pt): #pops up the rules for user
            rules()
        pt= intwin.getMouse()
    intwin.close() #end of intro

def rules():
    #Rules of our game in a separate window. Appears when user clicks rules.
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
    #Our game!
    win = GraphWin('CoinCollerctor', 600, 600)
    win.setCoords(0, 0, 600, 600)
    theme = Image(Point(300,300),"grass.png").draw(win) #Our background

    prompt = Text(Point(300, 340), 'Enter your name: ') #Asking for the player's name
    prompt.setFace('calibri')
    prompt.setStyle('bold')
    prompt.setSize(28)
    prompt.setFill(color_rgb(255, 240, 214))
    prompt.draw(win)

    userInput = Entry(Point(300, 300), 15)
    userInput.draw(win)

    play = Button(win, Point(300, 265), 50, 25, 'Play!')
    p = win.getMouse()
    while not play.isClicked(p):
        p = win.getMouse()

    playerName = userInput.getText()
    if playerName == '':
        playerName = 'Player'
    
    prompt.undraw()
    userInput.undraw()
    play.undraw()


    # play the music file indefinitely
    # the -1 signals pygame to play forever
    pygame.init()
    pygame.mixer.music.load("Jazzapation.wav") #Background music
    pygame.mixer.music.play(-1)

    #create a Player object 
    coinNumber = 10 #numbers of coins appearing on the screen
    player = Player(win, coinNumber)

    #a loop to keep track of collected coins
    start = time.time()
    while player.count < coinNumber:
        player.playerCollect(win)
    end = time.time()
    score = round((end - start)*100)
        
    player.player.undraw()
    resultBox = Rectangle(Point(200, 200), Point(450, 450))
    resultBox.setFill(color_rgb(115, 29, 78))
    resultBox.setWidth(0.1)
    resultBox.draw(win)

    #Telling the user the result of his/her game
    name = Text(Point(325, 360), 'Player: ' + str(playerName))
    name.setSize(17)
    name.setFill('white smoke')
    name.setFace('quicksand')
    collected = Text(Point(325, 335), 'Coin collected: ' + str(coinNumber))
    collected.setSize(17)
    collected.setFill('white smoke')
    collected.setFace('quicksand')
    score = Text(Point(325, 310), 'Score: ' + str(score))
    score.setSize(17)
    score.setFill('white smoke')
    score.setFace('quicksand')
    name.draw(win)
    collected.draw(win)
    score.draw(win)

    
    Exit = Button(win, Point(250, 235), 60, 30, 'Exit')
    restart = Button(win, Point(400, 235), 60, 30, 'Restart')

    pt = win.getMouse()
    while not Exit.isClicked(pt):
        if restart.isClicked(pt):
            win.close()
            pygame.mixer.music.stop()
            main()
            break
        pt = win.getMouse()
    
    win.close()
    pygame.mixer.music.stop()
intro()
