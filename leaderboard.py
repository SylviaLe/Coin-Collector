class Leaderboard:
    def __init__():
        self.names = []
        self.file = 'leaderboard.txt'
        with open(self.file, 'r') as file: #open the file
            data = file.readlines()
            self.board = list[data[-1]]  #cuz I cannot think of a short way to delete the previous session's data, here get the very last line of the file
        
    def update(name, score):
        if name in self.names:  #if user already exist
            for sub_list in self.board:    
                if name in sub_list:
                    pointer = self.board.index(sub_list)   #search for the index of the sublist that has the name in it
            self.board[pointer][0] = score    
            self.board.sort()`                #sort the board
            with open(self.file, 'w') as file:
                file.write(str(self.board))   #write to the file
        else:   
            self.names.append(name)           #append the name to the name list  
            result = [score, name]
            self.board.append(result)
            self.board.sort()
            with open(self.file, 'w') as file:
                file.write(str(self.board))
