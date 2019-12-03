from time import *
from graphics import *

class Timer:
    def __init__(self, window, pos):
        self.win = window
        self.clockPos = Text(pos, '')
        self.clockPos.draw(window)
        self.timeUp = False
        
    def countdown(self, time, window):
        mins, secs = divmod(n, 60)
        self.clockPos.setText('{:02d}:{:02d}'.format(mins, secs))
        #print('{:02d}:{:02d}'.format(mins, secs), end = '\n')
        if n == 0:
            print("End of program.")
        else:
            sleep(1)
            self.countdown(n-1, window)
        Text(Point(500, 350), 'Time Up!').draw(window)
        self.timeUp = True

def main():
    win = GraphWin('Time Test', 1000, 800)
    
    time = Timer(win, Point(500, 400))
    time.countdown(10, win)

if __name__ == '__main__':
    main()
