from random import randrange
from graphics import *

class Coin():
    def __init__(self, num, window):
        self.num = num
        self.selectedPts = []
        self.selectedX = []
        self.selectedY = []
        self.selectedCoins = []
        self.coinImg = 'coin(1).png'
        self.createCoin(window)

    def createCoin(self, window):
        for i in range(self.num):
            x = randrange(15,586,15)
            y = randrange(15,586,15)
            pt = Point(x,y)
            while pt in self.selectedPts:
                x = randrange(15,786,15)
                y = randrange(15,786,15)
                pt = Point(x,y)
            self.selectedX.append(x)
            self.selectedY.append(y)
            self.selectedPts.append(pt)
            self.selectedCoins.append(Image(pt, self.coinImg).draw(window))
          
def main():
    win = GraphWin('Coin Test', 600, 600)
    win.setCoords(0, 0, 600, 600)
    coin = Coin(50, win)

    for i in range(20):
        coin.selectedCoins[i].undraw()
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

