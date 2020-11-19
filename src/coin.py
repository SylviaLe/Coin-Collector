from random import randrange
from graphics import *

class Coin():
    """This class generates coins randomly on the screen. It also creates obstacles such as
    tnt, bombs, and fish."""
    def __init__(self, num, window):
        self.num = num
        self.selectedPts = []
        self.Img = ["img/coin(1).png","img/tnt.png","img/bomb.png","img/fish.png"]
        
        #create coins
        self.selectedPtsCoin = []
        self.selectedCoins = []
        self.coinDict = {}
        self.create(1,window,self.selectedPtsCoin,self.selectedCoins,self.coinDict,0)
        
        #create tnt
        self.selectedPtsTNT = []
        self.selectedTNT = []
        self.tntDict = {}
        self.create(6,window,self.selectedPtsTNT,self.selectedTNT,self.tntDict,1)
        
        #create bombs
        self.selectedPtsBomb = []
        self.selectedBombs = []
        self.bombDict = {}
        self.create(5,window,self.selectedPtsBomb,self.selectedBombs,self.bombDict,2)
        
        #create fish
        self.selectedPtsFish = []
        self.selectedFish = []
        self.fishDict = {}
        self.create(5,window,self.selectedPtsFish,self.selectedFish,self.fishDict,3)

        #convert dictionaries to lists for later use
        self.coinList = list(self.coinDict.values())
        self.tntList = list(self.tntDict.values())
        self.bombList = list(self.bombDict.values())
        self.fishList = list(self.fishDict.values())
        
    #This is how we create variables randomly
    def create(self,ratio,window,list1,list2,dictionary,index):
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
            dictionary[i] = (x,y)
        
def main():
    win = GraphWin('Coin Test', 600, 600)
    win.setCoords(0, 0, 600, 600)
    coin = Coin(10, win)  
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
