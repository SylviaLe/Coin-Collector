from player import *
from coin import *
from graphics import *
import time

class CoinCollector:
    def __init__(self, window, num):
        self.player = Player(window, num)
        self.score = 0
        self.isOver = False
        
    def play(self, window):
        start = time.time()
        while self.player.count != num:
            self.player.collectCoin(window)
        end = time.time()
        self.score = end - start
        
    def evalScore(self):
        return (self.player.count, round(self.score *10))
        
    def gameOver(self):
        if self.isOver == True:
            return True


        
    
