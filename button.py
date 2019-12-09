# button.py
# for lab 9 on writing classes
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('white')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() #Start off all buttons as active

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    ##check 4.  complete the isClicked() method
    def isClicked(self, pt):
        """Returns true if button active and Point pt is inside"""
        return(self.active and (pt.getX() > self.xmin and pt.getX() < self.xmax and pt.getY() > self.ymin and pt.getY() < self.ymax))
        
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
    
def main():
    win = GraphWin("Button", 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground('lavender')
    
    rollDice = Button(win, Point(200, 150), 100, 40, 'Roll Dice')
    rollDice.activate()
    quitButton = Button(win, Point(200, 100), 50, 25, 'Quit')
    quitButton.deactivate()

    pt = win.getMouse()
##    if rollDice.isClicked(pt):
##        print('Hello')
    while not quitButton.isClicked(pt):
        if rollDice.isClicked(pt):
            quitButton.activate()
        pt = win.getMouse()
            
        
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__": 
    main()
