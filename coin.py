from random import randrange
from graphics import *

class Coin():
    def __init__(self, num, window):
        self.num = num
        #generate coins
        self.selectedPts = []
        self.selectedCoins = []
        self.coinImg = 'coin(1).png'
        self.createCoin(window)

        #generate obstacles
        self.selectedPts2 = []
        self.selectedObstacles = []
        self.obstacleImg = ["fish.png","tnt.png","mushroom.png"]
        self.createObstacle(window)

    def createCoin(self, window):
        for i in range(self.num):
            x = randrange(30,571,15)
            y = randrange(30,571,15)
            pt = Point(x,y)
            while pt in self.selectedPts:
                x = randrange(15,571,15)
                y = randrange(15,571,15)
                pt = Point(x,y)
            self.selectedPts.append(pt)
            self.selectedCoins.append(Image(pt, self.coinImg).draw(window))

    def createObstacle(self,window):
        for i in range(self.num//4):
            x = randrange(30,571,15)
            y = randrange(30,571,15)
            pt = Point(x,y)
            while (pt in self.selectedPts) or (pt in self.selectedPts2):
                x = randrange(15,571,15)
                y = randrange(15,571,15)
                pt = Point(x,y)
            self.selectedPts2.append(pt)
            self.selectedObstacles.append(Image(pt, self.obstacleImg[randrange(3)]).draw(window))
          
def main():
    win = GraphWin('Coin Test', 600, 600)
    win.setCoords(0, 0, 600, 600)
    coin = Coin(20, win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
