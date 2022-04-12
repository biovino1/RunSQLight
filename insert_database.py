"""=====================================================================================================================
This scripts prompts the user for data to insert into the connected database.

Ben Iovino  4/12/22   RunSQLight
===================================================================================================================="""

import sqlite3 as sq3


def get_input():
    """=================================================================================================================
    This function is used to gather user input and return it as a tuple

    :return userinput: tuple of values
    ================================================================================================================="""

    flag = True
    while flag == True:
        datetime = input('Enter date and time (i.e. 2022-01-01 12:00 AM): ')
        type = input('Enter type of run: ')
        distance = float(input('Enter distance of run: '))
        duration = input('Enter duration of run (i.e. HH:MM:SS): ')
        notes = input('Notes: ')

        # Break loop if user types Y, continue if N
        print()
        input_flag = input('Does everything look correct? (Y/N): ')
        if input_flag == 'Y':
            flag = False
        elif input_flag == 'N':
            print()
            continue

    # Calculate pace from distance and duration
    duration_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], duration.split(":")))
    pace_sec = duration_sec / float(distance)
    pace_min = pace_sec // 60
    pace_sec = pace_sec % 60
    pace = f'{int(pace_min)}:{int(pace_sec)}'

    # Return input
    input_tuple = [datetime, type, distance, duration, pace, notes]
    print(input_tuple)
    return input_tuple


def main():
    """=================================================================================================================
    The main function is used to introduce the user to the program, call get_input(), and insert the gathered info
    into the database using insert_data().
    ================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    print()
    print('Welcome to RunSQLight! You are connected to your database.')
    print()
    get_input()


main()
