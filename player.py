from graphics import *
from coin import *

class Player:
    def __init__(self, window, num):
        self.coinNum = num
        self.coin = Coin(self.coinNum, window)

        self.playerImg = 'fox.png'
        self.iniPos = Point(300,300)
        self.player = Image(self.iniPos, self.playerImg)
        self.player.draw(window)
        self.count = 0
        
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
        playerCoords = self.player.getAnchor()

        if (playerCoords.getX() in self.coin.selectedX) and (playerCoords.getY() in self.coin.selectedY)
        and (self.coin.selectedX.index(playerCoords.getX()) == self.coin.selectedY.index(playerCoords.getY())):
            i = self.coin.selectedX.index(playerCoords.getX())
            self.coin.selectedCoins[i].undraw()
            self.count += 1
       
def main():
    win = GraphWin('Player Test', 600, 600)
    win.setCoords(0, 0, 600, 600)
    player = Player(win, 50)

    while player.count < 50:
        player.collectCoin(win)
    
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

