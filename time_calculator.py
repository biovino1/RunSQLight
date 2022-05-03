"""=====================================================================================================================
# This program creates a graphical window that accepts multiple times and adds them together.
It also displays total time in h:m:s format.

Ben Iovino  5/3/22   RunSQLight
===================================================================================================================="""

from graphics import *


def main_window():
    """=================================================================================================================
    This function creates the main window with necessary rectangle objects

    :return exit_rec, win: exit rectangle and window objects
    ================================================================================================================="""

    win = GraphWin("Time Calculator", 300, 500)
    win.setBackground('light grey')

    # Initialize entry box lists
    time_entries = list()

    # Create 6 entry boxes and text objects
    for i in range(0, 6):
        if i == 5:

            # Create the text object next to the total time entry box and above entry boxes
            time_text = Text(Point(100, 100 + 50 * i), 'Total Time: ').draw(win)
            time_text.setSize(15)
            example_text = Text(Point(175, 75), 'MM:SS').draw(win)

            # Create the total time entry box
            time_entry = Entry(Point(200, 100 + 50 * i), 10).draw(win)
            time_entry.setFill('white')
            time_entries.append(time_entry)

        else:

            # Create the text object next to the time entry box
            time_text = Text(Point(90, 100 + 50 * i), 'Time ' + str(i + 1) + ': ').draw(win)
            time_text.setSize(15)

            # Create entry boxes for times
            time_entry = Entry(Point(175, 100 + 50 * i), 10).draw(win)
            time_entry.setFill('white')
            time_entry.setText('00:00')
            time_entries.append(time_entry)

    # Line object that separates the time entries and total time
    line1 = Line(Point(50, 325), Point(250, 325)).draw(win)
    line1.setWidth(3)

    # Exit rec
    exit_rec = Rectangle(Point(175, 400), Point(275, 440)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(225, 420), "EXIT").draw(win)
    exit_text.setFill('white')

    # Calculate rec
    calc_rec = Rectangle(Point(25, 400), Point(125, 440)).draw(win)
    calc_rec.setFill('white')
    calc_text = Text(Point(75, 420), "CALCULATE").draw(win)

    # Check for exit rec click
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = calc_rec.getP1().getX(), calc_rec.getP1().getY()
            x2, y2 = calc_rec.getP2().getX(), calc_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                time1, time2, time3, time4, time5 = (time_entries[i].getText() for i in range(0, 5))
                times = [time1, time2, time3, time4, time5]
                total_time = calculate_time(times)
                time_entries[5].setText(total_time)
        click = clicked(click, exit_rec)
    win.close()


def calculate_time(times):
    """=================================================================================================================
    This function takes time values and adds them together

    :param times: list of times in MM:SS format
    :return totaltime: HH:MM:SS
    ================================================================================================================="""

    # Calculate total seconds
    total_seconds = 0
    for time in times:
        if time != ' ':
            minutes, seconds = time.split(":")
            total_seconds += 60 * int(minutes) + int(seconds)

    # Calculate m:s
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    if minutes < 10 and seconds < 10:
        total_time = f'0{minutes}:0{seconds}'
        return total_time
    if minutes < 10:
        total_time = f'0{minutes}:{seconds}'
        return total_time
    if seconds < 10:
        total_time = f'{minutes}:0{seconds}'
        return total_time
    total_time = f'{minutes}:{seconds}'
    return total_time


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
    The main function calls main_window() function to create graphical interface
    ================================================================================================================="""

    main_window()


main()