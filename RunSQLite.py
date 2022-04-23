"""=====================================================================================================================
This scripts creates a graphical interface that interacts with the database.

Ben Iovino  4/23/22   RunSQLight
===================================================================================================================="""

from graphics import *
import sqlite3 as sq3


def make_window():
    """=================================================================================================================
    This function creates a window with necessary rectangle objects to interact with the database

    :return win, recs: win is window object, recs are various rectangles
    ================================================================================================================="""

    # Window and title
    win = GraphWin("RunSQLite", 600, 400)
    win.setBackground('light grey')
    title_text = Text(Point(300, 25), "RunSQLite")
    title_text.setSize(20)
    title_text.draw(win)

    # Add interactive rectangles to add to/look at database
    rec1 = Rectangle(Point(50, 100), Point(250, 150))
    rec1.setFill('white')
    rec1.draw(win)
    rec2 = Rectangle(Point(50, 200), Point(250, 250))
    rec2.setFill('white')
    rec2.draw(win)
    rec3 = Rectangle(Point(350, 100), Point(550, 150))
    rec3.setFill('white')
    rec3.draw(win)
    rec4 = Rectangle(Point(350, 200), Point(550, 250))
    rec4.setFill('white')
    rec4.draw(win)
    exit_rec = Rectangle(Point(525, 350), Point(575, 375))
    exit_rec.setFill('red')
    exit_rec.draw(win)
    rtext1 = Text(Point(150, 125), "Insert New Run")
    rtext1.draw(win)
    rtext2 = Text(Point(150, 225), "Insert New Shoe")
    rtext2.draw(win)
    rtext3 = Text(Point(450, 125), "Running Logs")
    rtext3.draw(win)
    rtext4 = Text(Point(450, 225), "Shoe Logs")
    rtext4.draw(win)

    # Return the necessary objects
    return win, rec1, rec2, rec3, rec4, exit_rec


def clicked(click, rectangle):
    """=================================================================================================================
    This function accepts a mouse and rectangle object and returns a boolean object if the click is inside a rectangle.

    :return bool: True if click is inside rectangle, False if outside or no click
    ================================================================================================================="""

    if click is not None:
        mx, my = click.getX(), click.getY()

        # Retrieve coordinates of the rectangle corners
        x1, y1 = rectangle.getP1().getX(), rectangle.getP1().getY()
        x2, y2 = rectangle.getP2().getX(), rectangle.getP2().getY()

        # Return True if mouse click is within the rectangle
        if (x1 < mx < x2) and (y1 < my < y2):
            return True
        else:
            return None
    else:
        return None


def main():
    """=================================================================================================================
    The main function calls make_window() and uses clicked() to determine which rectangle objects have been clicked.
    ================================================================================================================="""

    win, rec1, rec2, rec3, rec4, exit_rec = make_window()

    # Keep window open until exit_rec is clicked
    click = win.checkMouse()
    while click == None:
        click = win.checkMouse()
        click = clicked(click, exit_rec)
    win.close()


main()
