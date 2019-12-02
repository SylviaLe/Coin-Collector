from graphics import *
from coin import *

class Player:
    def __init__(self, window, num):
        self.coinNum = num
        self.coin = Coin(self.coinNum, window)

        self.playFile = 'fox.png'
        self.iniPos = Point(400, 292)
        self.player = Image(self.iniPos, self.playFile)
        self.player.draw(window)
        
    def playerMove(self, window):
        key = window.getKey()
        if key == 'Up':
            self.player.move(0, 15)
        elif key == 'Down':
            self.player.move(0, -15)
        elif key == 'Left':
            self.player.move(-15, 0)
        elif key == 'Right':
            self.player.move(15, 0)

    def collectCoin(self, window):
        self.playerMove(window)
        count = 0
        
    #def stop(): #stop the player when it hits the boundaries
        
def main():
    win = GraphWin('Player Test', 800, 600)
    win.setCoords(0, 0, 800, 600)
    player = Player(win, 50)

    while True:
        player.collectCoin(win)
    
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
