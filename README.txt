PROBLEM SPECIFICATION AND DESIGN DOCUMENT

- This project creates a game called 'Coin Collector'
In this game, user can use the up, down, left, or right key to move a character on the screen, to get the coins that is generated randomly on the window. There will be a countdown clock, the user must get as many coins as possible before the clocks tick. Sounds and levels of difficulty (i.e. Easy/Medium/Hard) will also be added to the game.   

- Classes and methods:
  + Timer:INSTANCE VARIABLES:
          METHODS:
          
  + Coin: INSTANCE VARIABLES: 
              num: number of coins generated on the window
              selectedPts: a list of center points of all generated coins
              selectedCoins: a list of Image objects of all generated coins
              coinImg: an image file (.png or .gif) of a coin
          METHODS:
              createCoin(self, window)
                parameter(s): window
                return value(s): none
                function: randomly generate a specified number of coins on window and 
                          add their coordinations to selectedPts and  selectedCoins lists
  
  + Player: INSTANCE VARIABLES:
                
            METHODS: 
            
  + CoinCollector:  INSTANCE VARIABLES:
                    METHODS: 
  

- Pseudo code for main function:

#


