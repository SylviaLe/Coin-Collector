#Jin, Sylvia, and Sophie
#16 Dec. 2019
#leaderboard.py
#creates a leaderboard so then we can compare the scores after each game

from graphics import *

class Leaderboard:
    """This class creates leaderboard, which will rank the players' score and compare them"""
    def __init__(self):
        self.file = 'leaderboard.txt'
        with open(self.file, 'r') as file: #open the file
            data = file.readlines()
            self.board = eval(data[-1])  #cuz I cannot think of a short way to delete the previous session's data, here get the very last line of the file
            self.names = [self.board[i][1] for i in range(len(self.board))]
            #print(self.names)
            
    #This puts the player's name and score into the leaderboard
    def update(self, name, score):
        if name in self.names:  #if user already exist
            for sub_list in self.board:    
                if name in sub_list:
                    pointer = self.board.index(sub_list)   #search for the index of the sublist that has the name in it
            self.board[pointer][0] = score    
            newBoard = sorted(self.board)               #sort the board
            with open(self.file, 'w') as file:
                file.write(str(newBoard))   #write to the file
        else:   
            self.names.append(name)           #append the name to the name list  
            result = [score, name]
            self.board.append(result)
            newBoard = sorted(self.board)
            with open(self.file, 'w') as file:
                file.write(str(newBoard))

    #This method makes the leaderboard to appear on the graphics window
    def show(self, num, iniNamePos, iniScorePos, window):
        with open(self.file, 'r') as file: #open the file
            data = file.readlines()
            show = eval(data[-1])  #get the data that need to be shown

        space = 0
        if len(self.board) < num:  #if currentlt the board has less than 10 entries
            for i in range(len(self.board)):
                name, score = self.board[i][1], self.board[i][0]  #for each sublist, get the name and score, and draw it
                showName = Text(Point(iniNamePos, 305 - space), name) #Screen size is 400x400
                showScore = Text(Point(iniScorePos, 305 - space), score)

                showName.setSize(12)
                showName.setFace('quicksand')
                showName.setFill('white smoke')
                showScore.setSize(12)
                showScore.setFace('quicksand')
                showScore.setFill('white smoke')
                
                showName.draw(window)
                showScore.draw(window)

                space += 20
        else:   
            for i in range(num):
                name, score = self.board[i][1], self.board[i][0]
                showName = Text(Point(iniNamePos, 305 - space), name) #Screen size is 400x400. Better set iniNamePos 100, iniScorePos 300
                showScore = Text(Point(iniScorePos, 305 - space), score)

                showName.setSize(12)
                showName.setFace('quicksand')
                showName.setFill('white smoke')
                showScore.setSize(12)
                showScore.setFace('quicksand')
                showScore.setFill('white smoke')

                showName.draw(window)
                showScore.draw(window)
                
                space += 20
                    
def main():  #just a testing ground
    win = GraphWin('Leaderboard Test', 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground('black')
    
    board = Leaderboard()
##    board.update('syl', 345)
##    board.update('anna', 89)
    board.show(10, 135, 265, win)

if __name__  == '__main__':
    main()
            
