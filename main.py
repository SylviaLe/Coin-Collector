from coin import *
from graphics import *
from player import *
from button import *
from leaderboard import *
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
    gamename.setFace("quicksand")
    gamename.setStyle('bold')
    gamename.draw(intwin)

    bigFox = Image(Point(90,190),"bigFox.png").draw(intwin)
    bigCoin = Image(Point(280,200),"bigCoin.png").draw(intwin)
    bigCoin = Image(Point(365,179),"bigCoin.png").draw(intwin)
    bigCoin = Image(Point(310,156),"bigCoin.png").draw(intwin)
    
    #Buttons for users to choose what to do
    start = Button(intwin, Point(200,230),75,25,"Start")
    rule = Button(intwin, Point(200,200), 75, 25, "Rules")
    Quit = Button(intwin, Point(200,140),75,25, "Quit")
    lead = Button(intwin, Point(200, 170), 75, 25, 'Leaderboard')

    #Levels of difficulty prompt screen
    box = Rectangle(Point(100,260),Point(300,100))
    box.setFill(color_rgb(49, 77, 14))
    level = Text(Point(200,245),"Choose your level of difficulty")
    level.setFill(color_rgb(255, 240, 214))
    level.setStyle("italic")
    
    global board
    board = Leaderboard()

    coinNum = 0
    pt = intwin.getMouse()
    while not Quit.isClicked(pt):
        if start.isClicked(pt): 
            # Prompt user to choose level of difficulty before starting game
            box.draw(intwin)
            level.draw(intwin)
            easy = Button(intwin, Point(200,220),75,25,"Easy")
            med = Button(intwin, Point(200,180),75,25,"Medium")
            hard = Button(intwin, Point(200,140),75,25,"Hard")
            pt = intwin.getMouse()
            while not (easy.isClicked(pt) or med.isClicked(pt) or hard.isClicked(pt)):
                pt = intwin.getMouse()
            if easy.isClicked(pt):
                coinNum = 10
            elif med.isClicked(pt):
                coinNum = 20
            elif hard.isClicked(pt):
                coinNum = 50
            #Start the game
            intwin.close()
            main(coinNum)
            break
        elif rule.isClicked(pt):  #pop up the rules for user
            rules()
        elif lead.isClicked(pt):
            leaderboard()
        pt= intwin.getMouse()
    intwin.close()

def leaderboard():
    leadWin = GraphWin('Leaderboard', 400, 400)
    leadWin.setCoords(0, 0, 400, 400)
    theme = Image(Point(200, 200), 'lead.png')
    theme.draw(leadWin)

    proName = Text(Point(200, 368), 'Leaderboard')
    proName.setStyle('bold')
    proName.setFace('garamond')
    proName.setSize(25)
    proName.setFill('lemon chiffon')
    proName.draw(leadWin)

    playCol = Text(Point(135, 330), 'Player')
    scoreCol = Text(Point(265, 330), 'Score')
    playCol.setStyle('bold')
    playCol.setFace('helvetica')
    playCol.setSize(18)
    playCol.setFill('white smoke')
    scoreCol.setStyle('bold')
    scoreCol.setFace('helvetica')
    scoreCol.setSize(18)
    scoreCol.setFill('white smoke')
    playCol.draw(leadWin)
    scoreCol.draw(leadWin)

    board.show(8, 135, 265, leadWin)

def rules():
    #Rules of our game in a separate window. Appears when user clicks rules.
    rulewin = GraphWin("CoinCollector Rules", 400,400)
    rulewin.setCoords(0,0,200,200)
    #Design
    design = Image(Point(100,100), "rules.png")
    design.draw(rulewin)

    title = Text(Point(100,175), "Rules")
    title.setSize(32)
    title.setTextColor(color_rgb(240, 255, 255))
    title.setFace('quicksand')
    title.setStyle('bold')
    title.draw(rulewin)

    line1 = Text(Point(100,140),"- Try to collect all the coins with the shortest time.\nYour score will be determined by it.")
    line1.setSize(14)
    line1.setFace("calibri")
    line1.setFill('ghost white')
    line1.draw(rulewin)
    
    line2 = Text(Point(100,110),"- Use 'up', 'down', 'left', or 'right' key\nto move the character.")
    line2.setSize(14)
    line2.setFace("calibri")
    line2.setFill('ghost white')
    line2.draw(rulewin)
    
    line3 = Text(Point(100,70),"- Don't hit the obstacles, they will slow you down.\nFish bones: make you dizzy and take long to get over\nBombs: will take longer to diffuse")
    line3.setSize(14)
    line3.setFace("calibri")
    line3.setFill('ghost white')
    line3.draw(rulewin)

    line4 = Text(Point(100,40),"Warning! You will lose all score by collecting TNT explosives!")
    line4.setSize(14)
    line4.setFace("calibri")
    line4.setFill('gold')
    line4.draw(rulewin)

    line5 = Text(Point(100,20),"- See the leaderboard, try to beat other players.")
    line5.setSize(14)
    line5.setFace("calibri")
    line5.setFill('ghost white')
    line5.draw(rulewin)

    
def main(coinNum):
    win = GraphWin('Coin Collector', 600, 600)
    win.setCoords(0, 0, 600, 600)
    theme = Image(Point(300,300),"grass.png").draw(win)  #the background

    prompt = Text(Point(300, 340), 'Enter your name: ')  #prompt users to type name
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
        playerName = 'Guest'   #set the default to Player if the user didnt type anything
    
    prompt.undraw()
    userInput.undraw()
    play.undraw()

    # result to print out when game ends
    result = Text(Point(300,300),"")
    result.setSize(60)
    result.setFill("white")
    result.setFace("courier")
    result.setStyle("bold italic")
    result.draw(win)
    # play the music file indefinitely
    # the -1 signals pygame to play forever
    pygame.init()
    pygame.mixer.music.load("Jazzapation.wav")
    pygame.mixer.music.play(-1)

    #create a Player object 
    coinNumber = coinNum  #number of object on the screen
    player = Player(win, coinNumber)

    #a loop to keep track of collected coins
    start = time.time()
    #print(player.coin.coinList)
    while player.count < coinNumber and (not player.gameOver):
        player.playerCollect(win)
    if player.count >= coinNumber:
        result.setText("Mission Completed!")
        time.sleep(0.8)
        result.undraw()
        end = time.time()
        score = round((end - start)*100)
    else:
        result.setText("Game Over")
        time.sleep(0.8)
        result.undraw()
        end = time.time()
        score = 0

    coinNumber = player.count        
        
    player.player.undraw()
    resultBox = Rectangle(Point(150, 150), Point(450, 450))
    resultBox.setFill(color_rgb(115, 29, 78))
    resultBox.setWidth(0.1)
    resultBox.draw(win)

    board.update(playerName, score)

    #tell the user the result
    name = Text(Point(300, 336), 'Player: ' + str(playerName))
    name.setSize(17)
    name.setFill('white smoke')
    name.setFace('quicksand')
    collected = Text(Point(300, 300), 'Coin collected: ' + str(coinNumber))
    collected.setSize(17)
    collected.setFill('white smoke')
    collected.setFace('quicksand')
    score = Text(Point(300, 265), 'Score: ' + str(score))
    score.setSize(17)
    score.setFill('white smoke')
    score.setFace('quicksand')
    name.draw(win)
    collected.draw(win)
    score.draw(win)

    #choice: replay, see board, exit game
    restart = Button(win, Point(200, 175), 60, 30, 'Restart')
    viewBoard = Button(win, Point(300, 175), 95, 30, 'Leaderboard')
    Exit = Button(win, Point(400, 175), 60, 30, 'Exit')

    pt = win.getMouse()
    while not Exit.isClicked(pt):
        if viewBoard.isClicked(pt):
            leaderboard() #pop the leaderboard again if the user clicks
        elif restart.isClicked(pt):
            win.close()
            pygame.mixer.music.stop() #game end. Buh bye!
            main()
            break
        pt = win.getMouse()
    
    win.close()
    pygame.mixer.music.stop()
intro()
