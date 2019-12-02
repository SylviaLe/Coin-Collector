from graphics import *
from coin import *

class Player:
    def __init__(self, window, num):
        self.playFile = 'fox.png'
        self.iniPos = Point(500, 400)
        self.player = Image(self.iniPos, self.playFile)
        self.player.draw(window)

        self.coinNum = num
        self.coin = Coin(self.coinNum, window)
        
    def playerMove(self, window):
        key = window.getKey()
        if key == 'Up':
            self.player.move(0, 20)
        elif key == 'Down':
            self.player.move(0, -20)
        elif key == 'Left':
            self.player.move(-20, 0)
        elif key == 'Right':
            self.player.move(20, 0)

    def collectCoin(self, window):
        
    #def stop(): #stop the player when it hits the boundaries
        
def main():
    win = GraphWin('Player Test', 1000, 800)
    player = Player(win, 50)

    while True:
        player.playerMove(win)
    
    win.getMouse()
    win.close()

main()  
