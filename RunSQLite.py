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
    run_ins_rec = Rectangle(Point(50, 75), Point(250, 125))
    run_ins_rec.setFill('white')
    run_ins_rec.draw(win)
    shoe_ins_rec = Rectangle(Point(50, 175), Point(250, 225))
    shoe_ins_rec.setFill('white')
    shoe_ins_rec.draw(win)
    time_calc_rec = Rectangle(Point(50, 275), Point(250, 325))
    time_calc_rec.setFill('white')
    time_calc_rec.draw(win)
    run_log_rec = Rectangle(Point(350, 75), Point(550, 125))
    run_log_rec.setFill('white')
    run_log_rec.draw(win)
    shoe_log_rec = Rectangle(Point(350, 175), Point(550, 225))
    shoe_log_rec.setFill('white')
    shoe_log_rec.draw(win)
    graph_rec = Rectangle(Point(350, 275), Point(550, 325))
    graph_rec.setFill('white')
    graph_rec.draw(win)

    # Add exit rectangle and text
    exit_rec = Rectangle(Point(525, 25), Point(575, 50))
    exit_rec.setFill('red')
    exit_rec.draw(win)
    exit_text = Text(Point(550, 38), 'X')
    exit_text.draw(win)

    # Add text for each rectangle
    run_ins_text = Text(Point(150, 100), "Insert New Run")
    run_ins_text.draw(win)
    shoe_ins_text = Text(Point(150, 200), "Insert New Shoe")
    shoe_ins_text.draw(win)
    time_calc_text = Text(Point(150, 300), "Time Calculator")
    time_calc_text.draw(win)
    run_log_text = Text(Point(450, 100), "Running Logs")
    run_log_text.draw(win)
    shoe_log_text = Text(Point(450, 200), "Shoe Logs")
    shoe_log_text.draw(win)
    graph_rec_text = Text(Point(450, 300), "Graph Runs")
    graph_rec_text.draw(win)

    # Return the necessary objects
    return win, run_ins_rec, shoe_ins_rec, run_log_rec, time_calc_rec, shoe_log_rec, graph_rec, exit_rec


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

    win, run_ins_rec, shoe_ins_rec, time_calc_rec, run_log_rec, shoe_log_rec, graph_rec, exit_rec = make_window()

    # Keep window open until exit_rec is clicked
    click = win.checkMouse()
    while click == None:
        click = win.checkMouse()
        click = clicked(click, exit_rec)
    win.close()


main()
