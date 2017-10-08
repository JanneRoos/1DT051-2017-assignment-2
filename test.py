from graphics import *

def update(window):
    c = Circle(Point(50, 50), 10)
    c.draw(window)
    r = Rectangle(Point(40, 40), Point(60, 60))
    r.draw(window)
    return r

window = GraphWin("Uppgift7c", 300, 300)
r = update(window)

r.setWidth(3)
