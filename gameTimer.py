from time import *
from graphics import *

class Timer:
    def __init__(self, window, pos):
        self.win = window
        self.clockPos = Text(pos, '')
        self.clockPos.draw(window)
        self.timeUp = False
        
    def countdown(self, time, window):
        while time:
            mins, secs = divmod(time, 60)
            strformat = '{:02d}:{:02d}'.format(mins, secs)
            self.clockPos.setText(strformat)
            sleep(1)
            time -= 1
        Text(Point(500, 350), 'Time Up!').draw(window)
        self.timeUp = True

def main():
    win = GraphWin('Time Test', 1000, 800)
    
    time = Timer(win, Point(500, 400))
    time.countdown(10, win)

if __name__ == '__main__':
    main()
