from graphics import *

# Use the funtions from utils.py as part the solution. 
from utils import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
PLAYER_MOVE_DISTANCE = 100

def main():
    """
    The main function of the game.

    Side effects:
      Shows a splash screen.
      When the player clicks on the play button, lets the user play the game.
      If the user clicks on the quit button, close the window. 
    """

    w = GraphWin("The Hunger Games", SCREEN_WIDTH, SCREEN_HEIGHT)
    splash(w)
    game(w)

def splash(w):
    """
    Argument(s):
      w :: Graphical window.

    Side effects:
      Shows the splash screen with two buttons and a "hidden"
      Easter egg.

      Buttons:
        play -  play the game.
        quit - close the window w.

      Easter egg:
        When the user clicks on a "secret area" of the splash screen,
        the "secret area" changes to a random color. 
    """

    w.setBackground("black")

    # TODO: Add code here.

    # Make use of the functions from utils.py as part of your solution.

    # Structure the code by creating new functions, for example one function
    # for each of the following tasks:
    # 
    #    1) Create (and return) the Easter egg circle.
    #    2) Create (and return) the text "The Hunger Games".
    #    3) create (and return) a tuple with the play button circle and
    #       text. 
    #    4) Create (and return) a tuple with the quit button rectangle
    #       and text.
    tSize = 18

    def easterCircle():
        p = Point(250, -125)
        c = Circle(p, 250)
        c.setFill("medium orchid")

        return c

    def hungerText():
        t = Text(Point(250, 250), "The Hunger Games")
        t.setStyle("bold")
        t.setTextColor("yellow")
        t.setSize(5)
        return t

    def playButton():
        p = Point(150, 350)
        c = Circle(p, 50)
        c.setFill("red")

        t = Text(Point(150, 350), "Play")
        t.setStyle("bold")
        t.setSize(tSize)

        return (c, t)

    def quitButton():
        r = Rectangle(Point(280, 300), Point(380, 400))
        r.setFill("red")
        t = Text(Point(330, 350), "Quit")
        t.setStyle("bold")
        t.setSize(tSize)

        return (r, t)

    easterCircle = easterCircle()
    hungerText = hungerText()
    playButton = playButton()
    quitButton = quitButton()

    items = [easterCircle,
             hungerText,
             playButton[0],
             quitButton[0],
             playButton[1],
             quitButton[1]]
    
    for x in items:
        x.draw(w)
    grow(hungerText)

    while True:
        point = w.getMouse()

        if inCircle(point, playButton[0]):
            hide(items)
            fade(w)
            game(w)
        elif inRectangle(point, quitButton[0]):
            hide(items)
            fade(w)
            w.close()
        elif inCircle(point, easterCircle):
            easterCircle.setFill(randomColor())


def makeHero(p):
    """
    Argument(s):
      p :: Point.

    Return value: A circle with center p representing the hero. 
    """

    h = Circle(p, 35)
    h.setWidth(10)
    h.setFill("yellow")

    return h

def makeFood(p):
    """
    Argument(s):
      p :: Point.

    Return value: A circle with center p representing the food. 
    """

    f = Circle(p, 20)
    f.setWidth(10)
    f.setFill("red")

    return f

def gameOver(hero, food):
    """
    Argument(s):
      hero :: Circle
      food :: Circle

    Return value :: Bool
      Returns True if the center of the hero is the same as the center of the food,
      otherwise returns False. 
    """
    hCenter = hero.getCenter()
    fCenter = food.getCenter()
    hx = hCenter.getX()
    hy = hCenter.getY()
    fx = fCenter.getX()
    fy = fCenter.getY()
    
    if hx == fx and hy == fy:
        return True
    else:
        return False


def delta(hero, key):
    """
    Argument(s):
      hero :: Circle
      key  :: String ("Up", "Down", "Left" or "Right").

    Return value :: a tuple (dx, dy).
      dx - how much to move the hero circle in the x-direction.
      dy - how much to move the hero circle in the y-direction. 
    """

    (dx, dy) = (0, 0)

    # TODO: Add code here.

    if key == "Up":
        dy -= PLAYER_MOVE_DISTANCE
    elif key == "Down":
        dy += PLAYER_MOVE_DISTANCE
    elif key == "Left":
        dx -= PLAYER_MOVE_DISTANCE
    elif key == "Right":
        dx += PLAYER_MOVE_DISTANCE
        
    return (dx, dy)

def game(w):
    """
    Argument(s):
      w :: Graphical window.

    Side effects:
      Let the user play the game by moving the hero around on the grid. 
    """
    w.setBackground("white")
    grid = makeGrid()

    (h, f) = randomPoints()
    hero = makeHero(h)
    food = makeFood(f)

    objects = grid + [hero, food]
    show(objects, w)

    while True:
        if gameOver(hero, food):
            hide(objects)
            splash(w)

        key = w.getKey()

        (dx, dy) = delta(hero, key)

        hero.move(dx, dy)

        cCenter = hero.getCenter()
        hx = cCenter.getX()
        hy = cCenter.getY()

        if hx < 0:
            hero.move(SCREEN_WIDTH, 0)
        elif hx > SCREEN_WIDTH:
            hero.move(-SCREEN_WIDTH, 0)
        elif hy < 0:
            hero.move(0, SCREEN_HEIGHT)
        elif hy > SCREEN_HEIGHT:
            hero.move(0, -SCREEN_HEIGHT)
        

if __name__ == "__main__":
    main()
