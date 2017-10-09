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
      Set the color of shgape to a random color.
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

    pass # TODO: Add code here

def hide(objects):
    """
    Argument(s):
      objects :: List of graphical objects.

    Side effects:
      Undraw all objects.
    """

    pass # TODO: Add code here.

def grow(t):
    """Argument(s):
      t :: Text.

    Side effects:
      Step by step, change the font size of t from 5 to 32.

    Return value: None.
    """

    pass # TODO: Add code here.



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


def inCircle(p, c):
    """
    Argument(s):
      p :: Point
      c :: Circle

    Return value :: Bool
      True if p is inside the circle c, otherwise False.
    """

    # TODO: Add code here.

    return False # TODO: Change this.

def inRectangle(p, r):
    """
    Argument(s):
      p :: Point.
      r :: Rectangle.

    Return value:: Bool.
      True if p is inside the rectangle r, otherwise False.
    """

    # TODO: Add code here.

    return False # TODO: Change this. 


def makeGrid():
    """
    Creates all the lines that makes up the grid.

    Argument(s): None

    Side effects: None

    Return value: List of Line objects.
    """

    lines = []

    # TODO: Add code here.

    return lines


