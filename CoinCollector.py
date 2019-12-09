from player import *
from coin import *
from graphics import *
import time

class CoinCollector:
    def __init__(self, window):
        self.player = Player(window, 50)
        self.score = 0
        self.isOver = False
        
    def play(self, window):
        start = time.time()
        while self.player.count != 10:
            self.player.collectCoin(window)
        end = time.time()
        self.score = end - start
        
    def evalScore(self):
        return (self.player.count, round(self.score *10))
        
    def gameOver(self):
        if self.isOver == True:
            return True


        
    
