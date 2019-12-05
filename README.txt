PROBLEM SPECIFICATION AND DESIGN DOCUMENT

- This project creates a game called 'Coin Collector'
In this game, user can use the up, down, left, or right key to move a character on the screen, to get the coins that is generated randomly on the window. There will be a countdown clock, the user must get as many coins as possible before the time runs out. Other features: sounds and levels of difficulty (i.e. Easy/Medium/Hard). 

Note: In the document below, 'player' and 'character' are sometimes used interchangably.

- Classes and methods:
  + Timer: INSTANCE VARIABLES:
           METHODS:
          
  + Coin: INSTANCE VARIABLES: 
              num: number of coins generated on the window
              selectedPts: a list of center points of all generated coins
              selectedCoins: a list of Image objects of all generated coins
              coinImg: an image file (.png or .gif) of a coin
          METHODS:
              createCoin
                  parameters: window
                  return values: none
                  function: randomly generates a specified number of coins on window and 
                            appends their coords to selectedPts and  selectedCoins lists
  
  + Player: INSTANCE VARIABLES:
                coinNum: number of coins to generate 
                coin: a Coin object, generating coins on window
                playerImg: an image file (.png or .gif) of player
                iniPos: coords where player first stands, a Point object
                player: an Image object representing player
                count: a variable to keep track of coins which are already collected
            METHODS: 
                playerMove
                    parameters: window
                    return values: none
                    function: checks for key inputs (up,down,left,or right) and move character accordingly
                collectCoin
                    parameters: window
                    return values: none
                    function: simulates coin collection, signaling successful intake of coins.
            
  + CoinCollector:  INSTANCE VARIABLES:
                        
                    METHODS: 
  

- Pseudo code for main function:

#


