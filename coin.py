from random import randrange
from graphics import *

class Coin():
    def __init__(self, num, window):
        self.num = num
        self.coinList = []
        self.selectedPts = []
        self.coinFile = 'coin(1).png'
        self.createCoin(window)

    def createCoin(self, window):
##        for i in range(self.num):
##            x = randrange(10, 990)
##            y = randrange(10, 790)
##            self.coinList.append(Point(x, y))
##
##            Image(Point(x, y), self.coinFile).draw(window)
##    
        for x in range (10,791, 15):
            for y in range(7, 593, 15):
                self.coinList.append(Point(x, y))

        selectedImg = []
        for i in range(self.num):
            selectedImg.append(Image(self.coinList[randrange(2120)], self.coinFile).draw(window))

        for item in selectedImg:
            self.selectedPts.append(item.getAnchor())
          
def main():
    win = GraphWin('Coin Test', 800, 600)
    win.setCoords(0, 0, 800, 600)
    coin = Coin(50, win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
