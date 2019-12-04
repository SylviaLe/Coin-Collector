from player import *
from coin import *
from gameTimer import *
from graphics import *


class CoinCollector:
    def __init__(self, window):
        self.clock = Timer(window, Point(20, 580))
        self.player = Player(window, 50)
        
    def play(self, window):
        self.clock.countdown(10, window)

        while not self.clock.timeUp():
            self.player.collectCoin(window)
        
    def evalScore(self):
        return self.player.count
        
    #def gameOver():

def main():
    win = GraphWin('Test', 600, 600)
    win.setCoords(0, 0, 600, 600)

    game = CoinCollector(win)
    game.play(win)
    print(game.evalScore())

    win.getMouse()
    win.close()

main()
        
    
