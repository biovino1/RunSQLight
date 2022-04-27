"""=====================================================================================================================
This scripts prompts the user for data to insert into the connected database.

Ben Iovino  4/19/22   RunSQLight
===================================================================================================================="""

import sqlite3 as sq3
import uuid


def check_flag(input_flag):
    """=================================================================================================================
    This function takes a string value and returns a boolean value.

    :param input_flag: string value i.e. 'Y' for yes, 'N' for no
    :return flag: bool value i.e. True or False
    ================================================================================================================="""

    flag = True
    if input_flag == 'Y':
        flag = False
    elif input_flag == 'N':
        print()

    return flag


def welcome_user():
    """=================================================================================================================
    This function welcomes the user and directs them to the desired database table.

    :return input_table: str of table name to insert data into
    ================================================================================================================="""

    print()
    print('Welcome to RunSQLight! You are connected to your database.')
    print()

    # Ensuring correct input from user
    flag = True
    while flag:
        input_table = input('Would you like to add a run or a shoe?: ')
        if input_table.lower() == 'run':
            input_table = 'runs'
            flag = False
        if input_table.lower() == 'shoe':
            input_table = 'shoes'
            flag = False

    print()
    print(f'You are adding to the {input_table} table.')
    print()

    return input_table


def get_input(table_input):
    """=================================================================================================================
    This function is used to gather user input and return it as a tuple

    :param table_input: table that values go into, decides input required
    :return input_tuple: tuple of values
    ================================================================================================================="""

    # runs table input
    flag = True
    if table_input == 'runs':
        while flag:
            date = input('Enter date and time (i.e. 2022-01-01): ')
            time = input('Enter time (i.e. 4:31 PM: ')
            type = input('Enter type of run: ')
            distance = float(input('Enter distance of run: '))
            duration = input('Enter duration of run (i.e. HH:MM:SS): ')
            notes = input('Notes: ')

            # Break loop if user types Y, continue if N
            print()
            input_flag = input('Does everything look correct? (Y/N): ')
            flag = check_flag(input_flag)

        # Calculate pace from distance and duration
        duration_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], duration.split(":")))
        pace_sec = duration_sec / float(distance)
        pace_min = pace_sec // 60
        pace_sec = pace_sec % 60
        pace = f'{int(pace_min)}:{int(pace_sec)}'

        # Assign uuid and return tuple
        run_id = str(uuid.uuid1())
        input_tuple = [run_id, date, time, type, distance, duration, pace, notes]
        return input_tuple

    # shoes table input
    if table_input == 'shoes':
        while flag:
            shoe = input('Enter name and model of shoe: ')
            distance = input('Enter previous distance on shoe: ')
            retired = 'N'

            print()
            input_flag = input('Does everything look correct? (Y/N): ')
            flag = check_flag(input_flag)

        # Return values as a tuple
        input_tuple = [shoe, distance, retired]
        return input_tuple


def db_insert(dbh, db, input_table, input_tuple):
    """=================================================================================================================
    This function takes input tuple and inserts into connected SQLite db

    :param dbh: SQLite db connection object
    :param db: SQLite db cursor object
    :param input_table: name of table to insert values into
    :param input_tuple: tuple of 6 values
    ================================================================================================================="""

    # Determine how many values are being inserted
    values = ['?'] * len(input_tuple)
    values = ", ".join(values)

    # Insert into db
    sq3 = f'''
           INSERT INTO {input_table}
               VALUES ({values})
           '''
    db.execute(sq3, input_tuple)
    dbh.commit()


def main():
    """=================================================================================================================
    The main function is used to introduce the user to the program, call get_input(), and insert the gathered info
    into the database using insert_data().
    ================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    input_table = welcome_user()

    input_tuple = get_input(input_table)
    db_insert(dbh, db, input_table, input_tuple)


main()
