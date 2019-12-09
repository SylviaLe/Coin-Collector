from graphics import *
from coin import *
import pygame
import time

class Player:
    def __init__(self, window, num):
        self.coinNum = num
        self.coin = Coin(self.coinNum, window)

        self.playerImg = 'fox.png'
        self.iniPos = Point(300,300)
        self.player = Image(self.iniPos, self.playerImg)
        self.player.draw(window)
        self.count = 0
        self.coin_sound = pygame.mixer.Sound("collectCoin.wav")
        
    def playerMove(self, window):
        key = window.getKey()
        player_x = self.player.getAnchor().getX()
        player_y = self.player.getAnchor().getY()

        if key == 'Up'and player_y + 15 <= 570:
            self.player.move(0, 15)
        elif key == 'Down' and player_y - 15 >= 30:
            self.player.move(0, -15)
        elif key == 'Left' and player_x - 15 >= 30:
            self.player.move(-15, 0)
        elif key == 'Right' and player_x + 15 <= 570:  
            self.player.move(15, 0)
            
    def collectCoin(self, window):
        self.playerMove(window)
        player_x = self.player.getAnchor().getX()
        player_y = self.player.getAnchor().getY()
        player_y1 = player_y + 15 #enlarge the area the fox covers
        player_y2 = player_y - 15

        for p in self.coin.selectedPts:
            pt_x = p.getX()
            pt_y = p.getY()
            if pt_x == player_x and (pt_y == player_y or pt_y == player_y1 or pt_y == player_y2):
                i = self.coin.selectedPts.index(p)
                del self.coin.selectedPts[i]
                
                self.coin.selectedCoins[i].undraw()
                del self.coin.selectedCoins[i]
                
                #play coin sound
                pygame.mixer.Sound.play(self.coin_sound)
                #+1
                text = Text(Point(pt_x,pt_y+40),"+1")
                text.setFill("coral")
                text.setStyle("bold")
                text.setSize(16)
                text.draw(window)
                time.sleep(0.2)
                text.undraw()
                self.count += 1
       

if __name__ == '__main__':
    main()


