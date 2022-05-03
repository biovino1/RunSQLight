"""=====================================================================================================================
This scripts creates a graphical interface that interacts with the database.

Ben Iovino  5/3/22   RunSQLight
===================================================================================================================="""

from graphics import *
import sqlite3 as sq3
import uuid
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import timedelta, date


def make_main_window():
    """=================================================================================================================
    This function creates the main window with necessary rectangle objects to interact with the database

    :return win, recs: win is window object, recs are various rectangles
    ================================================================================================================="""

    # Window and title
    win = GraphWin("RunSQLite", 600, 400)
    win.setBackground('light grey')
    title_text = Text(Point(300, 25), "RunSQLite").draw(win)
    title_text.setSize(20)

    # Add interactive rectangles to add to/look at database
    run_ins_rec = Rectangle(Point(50, 75), Point(250, 125)).draw(win)
    run_ins_rec.setFill('white')
    shoe_ins_rec = Rectangle(Point(50, 175), Point(250, 225)).draw(win)
    shoe_ins_rec.setFill('white')
    run_log_rec = Rectangle(Point(350, 75), Point(550, 125)).draw(win)
    run_log_rec.setFill('white')
    shoe_log_rec = Rectangle(Point(350, 175), Point(550, 225)).draw(win)
    shoe_log_rec.setFill('white')
    graph_rec = Rectangle(Point(200, 275), Point(400, 325)).draw(win)
    graph_rec.setFill('white')

    # Add exit rectangle and text
    exit_rec = Rectangle(Point(525, 25), Point(575, 50)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(550, 38), 'X').draw(win)

    # Add text for each rectangle
    run_ins_text = Text(Point(150, 100), "Insert New Run").draw(win)
    shoe_ins_text = Text(Point(150, 200), "Insert New Shoe").draw(win)
    run_log_text = Text(Point(450, 100), "Running Logs").draw(win)
    shoe_log_text = Text(Point(450, 200), "Shoe Logs").draw(win)
    graph_rec_text = Text(Point(300, 300), "Graph Runs").draw(win)

    # Add rectangles to tuple, return win and rectangles
    rectangles = (run_ins_rec, shoe_ins_rec, run_log_rec, shoe_log_rec, graph_rec, exit_rec)
    return win, rectangles


def insert_run(db, dbh):
    """=================================================================================================================
    This function creates the window for inserting runs.

    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    win = GraphWin("Insert New Run", 400, 550)
    win.setBackground('light grey')
    title_text = Text(Point(200, 25), "Insert New Run").draw(win)
    title_text.setSize(20)

    # Date entry box/text
    date_entry = Entry(Point(250, 100), 12).draw(win)
    date_entry.setFill('white')
    date_entry.setText('YYYY-MM-DD')
    date_text = Text(Point(125, 100), 'Enter date: ').draw(win)

    # Time entry box/text
    time_entry = Entry(Point(250, 150), 12).draw(win)
    time_entry.setFill('white')
    time_entry.setText('0:00 AM/PM')
    time_text = Text(Point(125, 150), 'Enter time: ').draw(win)

    # Type entry box/text
    type_entry = Entry(Point(250, 200), 12).draw(win)
    type_entry.setFill('white')
    type_entry.setText(' ')
    type_text = Text(Point(125, 200), 'Enter type: ').draw(win)

    # Distance entry box/text
    distance_entry = Entry(Point(250, 250), 12).draw(win)
    distance_entry.setFill('white')
    distance_entry.setText('0.0')
    distance_text = Text(Point(125, 250), 'Enter distance: ').draw(win)

    # Duration entry box/text
    duration_entry = Entry(Point(250, 300), 12).draw(win)
    duration_entry.setFill('white')
    duration_entry.setText('HH:MM:SS')
    duration_text = Text(Point(125, 300), 'Enter duration: ').draw(win)

    # Notes entry box/text
    notes_entry = Entry(Point(250, 350), 12).draw(win)
    notes_entry.setFill('white')
    notes_entry.setText(' ')
    notes_text = Text(Point(125, 350), 'Notes: ').draw(win)

    # Shoes entry box/text
    shoe_entry = Entry(Point(250, 400), 20).draw(win)
    shoe_entry.setFill('white')
    shoe_entry.setText('Enter shoe from below')
    shoe_text = Text(Point(125, 400), 'Shoe: ').draw(win)

    # Add exit rectangle and text
    exit_rec = Rectangle(Point(325, 25), Point(375, 50)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(350, 38), 'X').draw(win)

    # Store entry boxes in list
    entries = date_entry, time_entry, type_entry, distance_entry, duration_entry, notes_entry, shoe_entry

    # Search db for active shoes
    sq3 = '''
        SELECT *
        FROM shoes
        WHERE retired = 'N'
        '''
    db.execute(sq3)
    rows = db.fetchall()
    shoes = list()
    for row in rows:
        shoes.append(row[0])

    # Write text for active shoes
    for i in range(len(shoes)):
        shoes_text = Text(Point(200, 425+25*i), f'{shoes[i]}').draw(win)
        shoes_text.setSize(8)

    # Rectangle that inserts data into db
    insert_rec = Rectangle(Point(150, 500), Point(250, 525)).draw(win)
    insert_rec.setFill('white')
    insert_rec_text = Text(Point(200, 513), 'Insert').draw(win)

    # Insert entry box data into database when insert_rec is clicked
    input_list = list()
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()

        # Check for exit rec click
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = exit_rec.getP1().getX(), exit_rec.getP1().getY()
            x2, y2 = exit_rec.getP2().getX(), exit_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                win.close()
                return

        # Check for insert rec click
        click = clicked(click, insert_rec)
    for i in range(len(entries)):
        input_list.append(entries[i].getText())

    # Calculate pace from distance and duration
    duration_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], input_list[4].split(":")))
    pace_sec = float(duration_sec) / float(input_list[3])
    pace_min = pace_sec // 60
    pace_sec = pace_sec % 60
    pace = f'{int(pace_min)}:{int(pace_sec)}'
    input_list.insert(5, pace)
    input_list.insert(0, str(uuid.uuid1()))
    input_list[4] = float(input_list[4])

    # Determine how many values are being inserted
    values = ['?'] * len(input_list[0:8])
    values = ", ".join(values)

    # Insert into runs table
    sq3 = f'''
        INSERT INTO runs
        VALUES ({values})
        '''
    db.execute(sq3, input_list[0:8])

    # Update shoes table with distance from run
    params = [float(input_list[4]), input_list[8]]
    sq3 = f'''
        UPDATE shoes
        SET distance = distance + ?
        WHERE shoe = ?
        '''
    db.execute(sq3, params)
    dbh.commit()
    print(f'Inserted into db: {input_list}')

    win.close()


def insert_shoe(db, dbh):
    """=================================================================================================================
    This function creates the window for inserting runs.

    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    win = GraphWin("Insert New Shoe", 400, 300)
    win.setBackground('light grey')
    title_text = Text(Point(200, 25), "Insert New Shoe").draw(win)
    title_text.setSize(20)

    # Shoe entry box/text
    shoe_entry = Entry(Point(250, 100), 12).draw(win)
    shoe_entry.setFill('white')
    shoe_text = Text(Point(125, 100), 'Enter shoe name: ').draw(win)

    # Distance entry box/text
    distance_entry = Entry(Point(250, 150), 12).draw(win)
    distance_entry.setFill('white')
    distance_text = Text(Point(125, 150), 'Enter distance: ').draw(win)

    # Rectangle that inserts data into db
    insert_rec = Rectangle(Point(150, 250), Point(250, 275)).draw(win)
    insert_rec.setFill('white')
    insert_rec_text = Text(Point(200, 263), 'Insert').draw(win)

    # Add exit rectangle and text
    exit_rec = Rectangle(Point(325, 25), Point(375, 50)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(350, 38), 'X').draw(win)

    # Store entry boxes in list
    entries = shoe_entry, distance_entry

    # Insert entry box data into database when insert_rec is clicked
    input_list = list()
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()

        # Check for exit rec click
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = exit_rec.getP1().getX(), exit_rec.getP1().getY()
            x2, y2 = exit_rec.getP2().getX(), exit_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                win.close()
                return

        # Check for insert rec click
        click = clicked(click, insert_rec)
    for i in range(len(entries)):
        input_list.append(entries[i].getText())
    input_list.append('N')

    # Determine how many values are being inserted
    values = ['?'] * len(input_list)
    values = ", ".join(values)

    # Insert into shoes table
    sq3 = f'''
        INSERT INTO shoes
        VALUES ({values})
        '''
    db.execute(sq3, input_list)
    dbh.commit()
    print(f'Inserted into db: {input_list}')

    win.close()


def running_log(db):
    """=================================================================================================================
    This function creates the window for the running log

    :param db: database cursor object
    ================================================================================================================="""

    # Create a window to search for desired month and year
    win = GraphWin("Running Log", 300, 200)
    win.setBackground('light grey')

    # Entry boxes
    month_text = Text(Point(100, 25), 'Month').draw(win)
    year_text = Text(Point(200, 25), 'Year').draw(win)
    month_entry = Entry(Point(100, 50), 8).draw(win)
    month_entry.setFill('white')
    year_entry = Entry(Point(200, 50), 8).draw(win)
    year_entry.setFill('white')

    # Search and exit rectangle
    search_rec = Rectangle(Point(100, 150), Point(200, 175)).draw(win)
    search_rec.setFill('white')
    search_rec_text = Text(Point(150, 163), 'Search').draw(win)
    exit_rec = Rectangle(Point(260, 25), Point(285, 50)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(273, 38), 'X').draw(win)

    # Check for click on search box and store text
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = exit_rec.getP1().getX(), exit_rec.getP1().getY()
            x2, y2 = exit_rec.getP2().getX(), exit_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                win.close()
                return
        click = clicked(click, search_rec)
    month = month_entry.getText()
    year = year_entry.getText()
    win.close()

    # Add 0 to month if not in text box
    if len(month) < 2:
        month = f'0{month}'

    # Search db for active runs
    sq3 = f'''
        SELECT *
        FROM runs
        WHERE date LIKE '{year}-{month}-%%'
        '''
    db.execute(sq3)
    rows = db.fetchall()
    row_len = len(rows)

    # Window displaying months and years
    win = GraphWin("Running Log", 1000, 100+25*row_len)
    win.setBackground('light grey')

    date_text = Text(Point(50, 25), 'Date').draw(win)
    time_text = Text(Point(100, 25), 'Time').draw(win)
    type_text = Text(Point(150, 25), 'Type').draw(win)
    distance_text = Text(Point(215, 25), 'Distance').draw(win)
    duration_text = Text(Point(290, 25), 'Duration').draw(win)
    pace_text = Text(Point(350, 25), 'Pace').draw(win)
    notes_text = Text(Point(700, 25), 'Notes').draw(win)

    # Take each row and print in window
    i = 0
    for row in rows:
        date_text = Text(Point(50, 50+i*25), row[1]).draw(win)
        date_text.setSize(7)
        time_text = Text(Point(100, 50+i*25), row[2]).draw(win)
        time_text.setSize(7)
        type_text = Text(Point(150, 50+i*25), row[3]).draw(win)
        type_text.setSize(7)
        distance_text = Text(Point(215, 50+i*25), row[4]).draw(win)
        distance_text.setSize(7)
        duration_text = Text(Point(290, 50+i*25), row[5]).draw(win)
        duration_text.setSize(7)
        pace_text = Text(Point(350, 50+i*25), row[6]).draw(win)
        pace_text.setSize(7)

        # Break notes up if too long for window (>25 words)
        window = 20
        notes_split = row[7].split(' ')
        notes = list()
        if len(notes_split) > window:
            notes.append(' '.join(notes_split[:window]))
            notes.append(' '.join(notes_split[window:window+window]))
            notes_text1 = Text(Point(700, 50+i*25), notes[0]).draw(win)
            notes_text1.setSize(7)
            notes_text2 = Text(Point(700, 60+i*25), notes[1]).draw(win)
            notes_text2.setSize(7)
        else:
            notes_text1 = Text(Point(700, 50+i*25), row[7]).draw(win)
            notes_text1.setSize(7)
        i += 1


def shoe_log(db, dbh):
    """=================================================================================================================
    This function creates the window for the shoe log

    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    # Search db for all shoes
    sq3 = f'''
        SELECT *
        FROM shoes
        '''
    db.execute(sq3)
    rows = db.fetchall()
    row_len = len(rows)

    # Window displaying months and years
    win = GraphWin("Running Log", 500, 125+25*row_len)
    win.setBackground('light grey')

    # Text
    shoe_text = Text(Point(100, 25), 'Shoe').draw(win)
    distance_text = Text(Point(250, 25), 'Distance').draw(win)
    retired_text = Text(Point(400, 25), 'Retired').draw(win)

    # Take each row and print in window
    i = 0
    for row in rows:
        shoe_text = Text(Point(100, 50+i*25), row[0]).draw(win)
        shoe_text.setSize(7)
        distance_text = Text(Point(250, 50+i*25), row[1]).draw(win)
        distance_text.setSize(7)
        distance_text = Text(Point(400, 50+i*25), row[2]).draw(win)
        distance_text.setSize(7)
        i += 1

    # Entry box to change retirement status of shoe
    retire_text = Text(Point(100, 90+25*row_len), 'Change Retirement Status: ').draw(win)
    retire_entry = Entry(Point(275, 90+25*row_len), 12).draw(win)
    retire_entry.setFill('white')

    # Change and exit recs
    change_rec = Rectangle(Point(350, 75+25*row_len), Point(425, 105+25*row_len)).draw(win)
    change_rec.setFill('white')
    search_rec_text = Text(Point(385, 90+25*row_len), 'Change').draw(win)
    exit_rec = Rectangle(Point(450, 75+25*row_len), Point(485, 105+25*row_len)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(468, 90+25*row_len), 'X').draw(win)

    # Check for click on search box and store text
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = exit_rec.getP1().getX(), exit_rec.getP1().getY()
            x2, y2 = exit_rec.getP2().getX(), exit_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                win.close()
                return
        click = clicked(click, change_rec)
    shoe = retire_entry.getText()

    # Search db for shoe in entry box
    sq3 = f'''
            SELECT *
            FROM shoes
            WHERE shoe = ?
            '''
    db.execute(sq3, [shoe])
    rows = db.fetchall()
    retirement_status = rows[0][2]

    # Update shoes table with new retirement status
    if retirement_status == 'Y':
        new_status = 'N'
    else:
        new_status = 'Y'
    params = [new_status, shoe]
    sq3 = f'''
            UPDATE shoes
            SET retired = ?
            WHERE shoe = ?
            '''
    db.execute(sq3, params)
    dbh.commit()
    print(f'{shoe} is now {new_status}')

    win.close()


def graph_db(db):
    """=================================================================================================================
    This function graphs desired data from user input

    :param db: database cursor object
    ================================================================================================================="""

    # Window displaying months and years
    win = GraphWin("Graphing Runs", 500, 400)
    win.setBackground('light grey')

    # Date text and entry boxes
    graph_text = Text(Point(250, 25), 'Enter two dates to graph between:').draw(win)
    date1_text = Text(Point(150, 75), 'Date 1:').draw(win)
    date2_text = Text(Point(350, 75), 'Date 2:').draw(win)
    date1_entry = Entry(Point(150, 110), 12).draw(win)
    date1_entry.setFill('white')
    date1_entry.setText('2022-04-01')
    date2_entry = Entry(Point(350, 110), 12).draw(win)
    date2_entry.setFill('white')
    date2_entry.setText('2022-04-30')
    entries = date1_entry, date2_entry

    # Graph and exit rec and text
    graph_rec = Rectangle(Point(200, 350), Point(300, 375)).draw(win)
    graph_rec.setFill('white')
    graph_text = Text(Point(250, 363), 'Graph').draw(win)
    exit_rec = Rectangle(Point(425, 25), Point(475, 50)).draw(win)
    exit_rec.setFill('red')
    exit_text = Text(Point(450, 38), 'X').draw(win)

    # Check for click on graph box and store text
    entry_text = list()
    click = win.checkMouse()
    while click is None:
        click = win.checkMouse()

        # Check if graph button was clicked, graph using dates in entry boxes
        if click is not None:
            mx, my = click.getX(), click.getY()
            x1, y1 = graph_rec.getP1().getX(), graph_rec.getP1().getY()
            x2, y2 = graph_rec.getP2().getX(), graph_rec.getP2().getY()
            if (x1 < mx < x2) and (y1 < my < y2):
                date1 = date1_entry.getText()
                date2 = date2_entry.getText()

                # Find all dates in between two given dates
                start_dt = date1.split('-')
                end_dt = date2.split('-')
                start_dt = date(int(start_dt[0]), int(start_dt[1]), int(start_dt[2]))
                end_dt = date(int(end_dt[0]), int(end_dt[1]), int(end_dt[2]))
                delta = end_dt - start_dt

                days = list()
                for i in range(delta.days + 1):
                    day = start_dt + timedelta(days=i)
                    days.append(day)

                sq3 = f'''
                        SELECT *
                        FROM runs
                        WHERE date
                        BETWEEN '{date1}'
                        AND '{date2}'
                        '''
                db.execute(sq3)
                rows = db.fetchall()

                # Gather dates and distances from db
                run_dates = list()
                run_distances = list()
                for row in rows:
                    run_date = row[1].split('-')
                    run_date = date(int(run_date[0]), int(run_date[1]), int(run_date[2]))
                    run_dates.append(run_date)
                    run_distances.append(row[4])

                # Gather all dates in between, assign distance to corresponding day
                dates = list()
                distances = list()
                i = 0
                j = 0
                for day in days:
                    dates.append(day)
                    if run_dates[i] == dates[j]:
                        distances.append(run_distances[i])
                        if i < len(run_dates)-1:
                            i += 1
                    else:
                        distances.append(int(0))
                    j += 1
                array_dates = np.asarray(dates)
                array_distances = np.asarray(distances)

                # Plot date vs distance
                fig, ax = plt.subplots(figsize=(12, 8))
                ax.bar(array_dates, array_distances)
                ax.set_xlabel('Date')
                ax.set_ylabel('Distance (mi)')
                plt.title(f'Runs Between {date1} And {date2}')
                plt.xticks(rotation=90, fontsize=5)
                plt.show()

        click = clicked(click, exit_rec)
    win.close()


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


def control_window(win, rectangles, db, dbh):
    """=================================================================================================================
    This function determines which rectangle object (besides the exit rec) was clicked and returns which window needs
    to be opened.

    :param win: RunSQLite window
    :param rectangles: list of all rectangles in win
        run_ins_rec, shoe_ins_rec, run_log_rec, time_calc_rec, shoe_log_rec, graph_rec
    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    click = win.getMouse()
    mx, my = click.getX(), click.getY()

    # Call insert_run
    x1, y1 = rectangles[0].getP1().getX(), rectangles[0].getP1().getY()
    x2, y2 = rectangles[0].getP2().getX(), rectangles[0].getP2().getY()
    if (x1 < mx < x2) and (y1 < my < y2):
        insert_run(db, dbh)

    # Call insert_shoe
    x1, y1 = rectangles[1].getP1().getX(), rectangles[1].getP1().getY()
    x2, y2 = rectangles[1].getP2().getX(), rectangles[1].getP2().getY()
    if (x1 < mx < x2) and (y1 < my < y2):
        insert_shoe(db, dbh)

    # Call running_log
    x1, y1 = rectangles[2].getP1().getX(), rectangles[2].getP1().getY()
    x2, y2 = rectangles[2].getP2().getX(), rectangles[2].getP2().getY()
    if (x1 < mx < x2) and (y1 < my < y2):
        running_log(db)

    # Call shoe_log
    x1, y1 = rectangles[3].getP1().getX(), rectangles[3].getP1().getY()
    x2, y2 = rectangles[3].getP2().getX(), rectangles[3].getP2().getY()
    if (x1 < mx < x2) and (y1 < my < y2):
        shoe_log(db, dbh)

    # Call graph_db
    x1, y1 = rectangles[4].getP1().getX(), rectangles[4].getP1().getY()
    x2, y2 = rectangles[4].getP2().getX(), rectangles[4].getP2().getY()
    if (x1 < mx < x2) and (y1 < my < y2):
        graph_db(db)

    return click


def main():
    """=================================================================================================================
    The main function calls make_window() and uses clicked() to determine which rectangle objects have been clicked.
    ================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    win, rectangles = make_main_window()

    # Keep window open until exit_rec is clicked
    click = win.checkMouse()
    while click is None:
        click = control_window(win, rectangles, db, dbh)
        click = clicked(click, rectangles[5])
    win.close()
    exit(0)


main()
