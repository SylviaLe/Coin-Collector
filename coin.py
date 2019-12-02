from random import randrange
from graphics import *

class Coin():
    def __init__(self, num, window):
        self.num = num
        self.coinList = []
        self.coinFile = 'coin.png'
        self.createCoin(window)

    def createCoin(self, window):
        for i in range(self.num):
            x = randrange(10, 990)
            y = randrange(10, 790)
            self.coinList.append(Point(x, y))

            Image(Point(x, y), self.coinFile).draw(window)
    
                
def main():
    win = GraphWin('Coin Test', 1000, 800)
    coin = Coin(50, win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
