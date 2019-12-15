PROBLEM SPECIFICATION AND DESIGN DOCUMENT

- Program description:
This project creates a game called 'Coin Collector'. 
How to play: use 'up', 'down', 'left', or 'right' key to move the character around to collect coins, which are randomly generated.
There will be a countdown clock, so user must get as many coins as possible before time runs out. 
Other features: sounds, levels of difficulty(Easy/Medium/Hard) and random obstacles (i.e. explosives, fish bones, bombs)
Packages: pygame, leaderboard, graphics, button

*** Note: In the document below, 'player' and 'character' are sometimes used interchangably.

- Classes and methods:
   + Class Coin: INSTANCE VARIABLES: 
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
  
  + Class Player: INSTANCE VARIABLES:
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
                playerCollect
                    parameters: window
                    return values: none
                    function: How big of a space the fox will cover
                effect
                  parameters: window, coords, objectList, imageList, sound, image, delayTime, isCoin
                  return values: None
                  function: play sound and pops up "+1" above the fox to indicate that the user has collected a coin.
  + Class Leaderboard: INSTANCE VARIABLES: 
                       file: name of the text file we are keeping the scores in.
                       data: reading the text file
                       board: a list consisting of nested lists that contain name-score pairs inside
                       name: Stores the name of the people currently exist in the board.
                       
                 METHODS: 
                     update
                        parameters: name, score
                        return values: none
                        function: updates the leaderboard.
                     show
                        parameters: num, iniNamePos, iniScorePos, window
                        return values: none
                        function: shows the text on the graphics window
                 
- Kinds of testing you have done and modifications you would make for a future version:
  
- Pseudocode for main function:
         1. Create a main menu with buttons where user can navigate (i.e. 'Start','Rules','Exit'...)
         2. Start game if clicks 'Start', quit game if she clicks 'Exit'.
         3. Prompt user to choose level of difficulty 
         4. Create a new window, asking user to type her name 
         5. Show GUI and play game soundtrack: draw coins, obstacles, character
         6. Print out results
           - User loses all score if she/he steps on TNT explosives
           - User earns score if she/he collects all coins 
         7. Calculate score(win: score determined by the ellapsed time/lose: score 0)    
         8. Save score to leaderboard
         9. Available options after game ends: Restart, Exit, or Leaderboard  



