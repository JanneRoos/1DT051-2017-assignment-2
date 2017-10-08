from graphics import *

def main():

    window = GraphWin("Nippon", 150, 150)
    circ = Circle(Point(75, 75), 50)
    circ.setFill("red")
    circ.draw(window)

    window.getMouse()

main()
