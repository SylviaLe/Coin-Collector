PROBLEM SPECIFICATION AND DESIGN DOCUMENT

- Program description:
This project creates a game called 'Coin Collector'. 
In this game, user can use the up, down, left, or right key to move a character on the screen, to get the coins that is generated randomly on the window. 
There will be a countdown clock, the user must get as many coins as possible before time runs out. 
Other features: sounds, levels of difficulty(Easy/Medium/Hard) and random obstacles (i.e. explosives, cats, potholes) that decreases user's chance of winning.

*** Note: In the document below, 'player' and 'character' are sometimes used interchangably.

- Classes and methods:
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
            
  + CoinCollector: INSTANCE VARIABLES:  
                   METHODS: 
                    
  + Timer: INSTANCE VARIABLES:
           METHODS:
  
  
- Pseudo code for main function:

1. Create a main menu with buttons where user can navigate (i.e. 'Start','Rules','Exit'...)
2. Game begins as soon as user clicks 'Start' button
3. Create a new window 
4. Create a Player class
5. Create a Timer class
6. Print stuffs like 'Ready', 'Go'
7. Print out results
  - User loses if time-out or she/he steps on explosives/cats/holes
  - User wins: if she/he collects all coins before time-out
8. Available options after game ends: Restart or Exit  



