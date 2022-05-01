"""=====================================================================================================================
This scripts creates a graphical interface that interacts with the database.

Ben Iovino  4/23/22   RunSQLight
===================================================================================================================="""

from graphics import *
import sqlite3 as sq3
import uuid


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
    date_entry.setText('2022-04-27')
    date_text = Text(Point(125, 100), 'Enter date: ').draw(win)

    # Time entry box/text
    time_entry = Entry(Point(250, 150), 12).draw(win)
    time_entry.setFill('white')
    time_entry.setText('9:00 AM')
    time_text = Text(Point(125, 150), 'Enter time: ').draw(win)

    # Type entry box/text
    type_entry = Entry(Point(250, 200), 12).draw(win)
    type_entry.setFill('white')
    type_entry.setText('Easy')
    type_text = Text(Point(125, 200), 'Enter type: ').draw(win)

    # Distance entry box/text
    distance_entry = Entry(Point(250, 250), 12).draw(win)
    distance_entry.setFill('white')
    distance_entry.setText('6.0')
    distance_text = Text(Point(125, 250), 'Enter distance: ').draw(win)

    # Duration entry box/text
    duration_entry = Entry(Point(250, 300), 12).draw(win)
    duration_entry.setFill('white')
    duration_entry.setText('00:45:00')
    duration_text = Text(Point(125, 300), 'Enter duration: ').draw(win)

    # Notes entry box/text
    notes_entry = Entry(Point(250, 350), 12).draw(win)
    notes_entry.setFill('white')
    notes_entry.setText('Fun')
    notes_text = Text(Point(125, 350), 'Notes: ').draw(win)

    # Shoes entry box/text
    shoe_entry = Entry(Point(250, 400), 12).draw(win)
    shoe_entry.setFill('white')
    shoe_entry.setText('ReebokForever Floatride Energy 2v8')
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
        shoes.append(row[0]+' '+str(row[1]))

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


def running_log(db, dbh):
    """=================================================================================================================
    This function creates the window for the running log

    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    win = GraphWin("Running Log", 800, 800)
    win.setBackground('light grey')
    title_text = Text(Point(500, 25), "Running Log").draw(win)
    title_text.setSize(20)

    # Search db for active runs
    sq3 = '''
            SELECT *
            FROM runs
            WHERE date LIKE '2022-04-%%'
            '''
    db.execute(sq3)
    rows = db.fetchall()
    i = 0
    for row in rows:
        runs_text = Text(Point(500, 50 + 25 * i), f'{row[1], row[2], row[3], row[4], row[5], row[6], row[7]}').draw(win)
        runs_text.setSize(7)
        i += 1


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
        running_log(db, dbh)

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


main()
