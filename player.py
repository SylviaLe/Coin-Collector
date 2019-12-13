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
        self.coin_sound = pygame.mixer.Sound("coinSound.wav")
        self.bomb_sound = pygame.mixer.Sound("bombSound.wav")
        self.fish_sound = pygame.mixer.Sound("fishSound.wav")
        
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

    def effect(self,window,coords,objectList,imageList,sound,image,delayTime,isCoin):
        i = objectList.index(coords)
        del objectList[i]
        imageList[i].undraw()
        del imageList[i]
        pygame.mixer.Sound.play(sound)
        if isCoin:
            text = Text(Point(coords[0],coords[1]+40),"+1")
            text.setFill("coral")
            text.setStyle("bold")
            text.setSize(16)
            text.draw(window)
            time.sleep(delayTime)
            text.undraw()
            self.count += 1
        else:
            exp = Image(Point(coords[0],coords[1]+40),image)
            exp.draw(window)
            time.sleep(delayTime)
            exp.undraw()
            
    def playerCollect(self, window):
        self.playerMove(window)
        player_x = self.player.getAnchor().getX()
        player_y = self.player.getAnchor().getY()
        #enlarge the area the fox covers
        coords1 = (player_x,player_y)
        coords2 = (player_x,player_y + 15)
        coords3 = (player_x,player_y - 15)
        coords = (coords1 or coords2 or coords3)

        #(coords1 in self.coin.coinList) or (coords2 in self.coin.coinList) or (coords3 in self.coin.coinList)
        if coords1 in self.coin.coinList:
            self.effect(window,coords1,self.coin.coinList,self.coin.selectedCoins,self.coin_sound,"coin(1).png",0.2,True)
        elif coords1 in self.coin.tntList:
            self.effect(window,coords1,self.coin.tntList,self.coin.selectedTNT,self.bomb_sound,"explosion.png",0.5,False)
        elif coords1 in self.coin.bombList:
            self.effect(window,coords1,self.coin.bombList,self.coin.selectedBombs,self.bomb_sound,"explosion.png",0.5,False)
        elif coords1 in self.coin.fishList:
            self.effect(window,coords1,self.coin.fishList,self.coin.selectedFish,self.fish_sound,"stars.png",0.4,False)

if __name__ == '__main__':
    main()


