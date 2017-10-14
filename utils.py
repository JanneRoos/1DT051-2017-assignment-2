from graphics import *
from time import sleep
from random import choice, shuffle

def randomColor():
    """
    Argument(s): None

    Return value :: A random color name (string).
    """

    return choice(["red", "blue", "green", "pink", "orange", "RoyalBlue1", "green3"])

def randomColorFill(shape):
    '''
    Argument(s):
      shape :: Circle or Rectangle

    Return value :: None

    Side effects:
      Set the color of shape to a random color.
    '''

    shape.setFill(randomColor())

def randomPoints():
    """
    Argument(s): None

    Return value: A tuple (p1, p2) with random points.
      p1 :: Point
      p2 :: Point
    """

    values = range(50, 500, 100)
    positions = [(x, y) for x in values for y in values]
    shuffle(positions)

    (x1, y1) = positions[0]
    (x2, y2) = positions[1]

    return (Point(x1, y1), Point(x2, y2))

def show(objects, w):
    """
    Argument(s):
      objects :: List of graphical objects.
      w       :: Graphical window.

    Side effects:
      Draw all objects in window w.
    """

    for x in objects:
        x.draw(w)

def hide(objects):
    """
    Argument(s):
      objects :: List of graphical objects.

    Side effects:
      Undraw all objects.
    """

    for x in objects:
        x.undraw()

def grow(t):
    """Argument(s):
      t :: Text.

    Side effects:
      Step by step, change the font size of t from 5 to 32.

    Return value: None.
    """
    n = 5
    while n < 33:
        t.setSize(n)
        sleep(.008)
        n += 1


def fade(w):
    """
    Argument(s):
      w :: graphical window.

    Side effects:
      Step by step, change the background color of w to a brighter and brighter
      shade of gray.

    Return value: None
    """

    # A list of grays, darkest shade first and brightest shade last.
    grays = ['gray1',  'gray2',  'gray3',  'gray4',  'gray5',
             'gray6',  'gray7',  'gray8',  'gray9',  'gray10',
             'gray11', 'gray12', 'gray13', 'gray14', 'gray15',
             'gray16', 'gray17', 'gray18', 'gray19', 'gray20',
             'gray21', 'gray22', 'gray23', 'gray24', 'gray25',
             'gray26', 'gray27', 'gray28', 'gray29', 'gray30',
             'gray31', 'gray32', 'gray33', 'gray34', 'gray35',
             'gray36', 'gray37', 'gray38', 'gray39', 'gray40']

    # TODO: Add code here.
    for gray in grays:
        w.setBackground(gray)
        sleep(.025)


def inCircle(p, c):
    """
    Argument(s):
      p :: Point
      c :: Circle

    Return value :: Bool
      True if p is inside the circle c, otherwise False.
    """

    # TODO: Add code here.
    r = c.getRadius()
    cCenter = c.getCenter()

    dx = cCenter.getX() - p.getX()
    dy = cCenter.getY() - p.getY()

    d = dx**2 + dy**2

    if d <=  r**2:
        return True
    else:
        return False
    

def inRectangle(p, r):
    """
    Argument(s):
      p :: Point.
      r :: Rectangle.

    Return value:: Bool.
      True if p is inside the rectangle r, otherwise False.
    """

    p1 = r.p1
    p2 = r.p2

    if p1.getX() <= p.getX() <= p2.getX() and p1.getY() <= p.getY() <= p2.getY():
        return True
    else:
        return False


def makeGrid():
    """
    Creates all the lines that makes up the grid.

    Argument(s): None

    Side effects: None

    Return value: List of Line objects.
    """

    lines = []

    # TODO: Add code here.
    n = 0

    while n < 6:
        l = Line(Point(0, n * 100), Point(500, n * 100))
        l.setWidth(5)
        l.setFill("blue")
        m = Line(Point(n * 100, 0), Point(n * 100, 500))
        m.setWidth(5)
        m.setFill("blue")
        lines.append(l)
        lines.append(m)
        n += 1

    return lines

def yellow():
    return "yellow"
