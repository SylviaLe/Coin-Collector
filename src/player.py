from graphics import *
from coin import *
import pygame
import time

class Player:
    """This class draws the player, which is an image of a fox, and determines whether the player
    gets the coin or runs into obstacles"""
    
    #Initializing player

    def __init__(self, window, num):
        self.coinNum = num
        self.coin = Coin(self.coinNum, window)

        self.playerImg = 'img/fox.png'
        self.iniPos = Point(300,300)
        self.player = Image(self.iniPos, self.playerImg)
        self.player.draw(window)
        self.count = 0
        self.coin_sound = pygame.mixer.Sound("sound/coinSound.wav")
        self.tnt_sound = pygame.mixer.Sound("sound/tntSound.wav")
        self.bomb_sound = pygame.mixer.Sound("sound/bombSound.wav")
        self.fish_sound = pygame.mixer.Sound("sound/fishSound.wav")
        self.gameOver = False
       
    #How we are moving the fox
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

    #Create visual and sound effects when getting coins or running into obstacles       
    def effect(self,window,coords,objectList,imageList,sound,image,delayTime,isCoin):
        x = self.player.getAnchor().getX()
        y = self.player.getAnchor().getY()+40
        i = objectList.index(coords)
        del objectList[i]
        imageList[i].undraw()
        del imageList[i]
        pygame.mixer.Sound.play(sound)
        
        if isCoin:
            text = Text(Point(x,y),"+1")
            text.setFill("coral")
            text.setStyle("bold")
            text.setSize(16)
            text.draw(window)
            time.sleep(delayTime)
            text.undraw()
            self.count += 1
        else:
            exp = Image(Point(x,y),image)
            exp.draw(window)
            time.sleep(delayTime)
            exp.undraw()
            
    #How big of a space the fox will cover     
    def playerCollect(self, window):
        self.playerMove(window)
        player_x = self.player.getAnchor().getX()
        player_y = self.player.getAnchor().getY()
        #enlarge the area the fox covers
        coords1 = (player_x,player_y)
        coords2 = (player_x,player_y + 15)
        coords3 = (player_x,player_y - 15)
        coords = (coords1 or coords2 or coords3)
        c = 0

        for l in [self.coin.coinList,self.coin.tntList,self.coin.bombList,self.coin.fishList]:
            if (coords1 in l) or (coords2 in l) or (coords3 in l):
                if coords1 in l:
                    c = coords1
                elif coords2 in l:
                    c = coords2
                elif coords3 in l:
                    c = coords3
                    
                if l == self.coin.coinList:
                    self.effect(window,c,self.coin.coinList,self.coin.selectedCoins,self.coin_sound,"img/coin(1).png",0.2,True)
                elif l == self.coin.tntList:
                    self.effect(window,c,self.coin.tntList,self.coin.selectedTNT,self.tnt_sound,"img/tnt_explosion.png",0.5,False)
                    self.gameOver = True
                elif l == self.coin.bombList:
                    self.effect(window,c,self.coin.bombList,self.coin.selectedBombs,self.bomb_sound,"img/explosion.png",0.5,False)
                else:
                    self.effect(window,c,self.coin.fishList,self.coin.selectedFish,self.fish_sound,"img/stars.png",0.4,False)
                    
if __name__ == '__main__':
    main()
