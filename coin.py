from random import randrange
from graphics import *

class Coin():
    def __init__(self, num, window):
        self.num = num
        self.selectedPts = []
        self.Img = ["coin(1).png","tnt.png","bomb.png","fish.png"]
        
        #create coins
        self.selectedPtsCoin = []
        self.selectedCoins = []
        self.create(1,window,self.selectedPtsCoin,self.selectedCoins,0)
        
        #create tnt
        self.selectedPtsTNT = []
        self.selectedTNT = []      
        self.create(6,window,self.selectedPtsTNT,self.selectedTNT,1)
        
        #create bombs
        self.selectedPtsBomb = []
        self.selectedBombs = []
        self.create(5,window,self.selectedPtsBomb,self.selectedBombs,2)
        
        #create fishes
        self.selectedPtsFish = []
        self.selectedFish = []
        self.create(5,window,self.selectedPtsFish,self.selectedFish,3)

    def create(self,ratio,window,list1,list2,index):
        length = self.num//ratio
        for i in range(length):
            x = randrange(30,571,15)
            y = randrange(30,571,15)
            pt = Point(x,y)
            while (pt in list1) or (pt in self.selectedPts):
                x = randrange(15,571,15)
                y = randrange(15,571,15)
                pt = Point(x,y)
            self.selectedPts.append(pt)
            list1.append(pt)
            list2.append(Image(pt,self.Img[index]).draw(window))
          
def main():
    win = GraphWin('Coin Test', 600, 600)
    win.setCoords(0, 0, 600, 600)
    coin = Coin(20, win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
