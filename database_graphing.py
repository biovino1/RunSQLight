"""=====================================================================================================================
This scripts searches through an SQLite database and makes graphs based on user parameters.

Ben Iovino  4/19/22   RunSQLight
====================================================================================================================="""

import sqlite3 as sq3
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def get_input():
    """=================================================================================================================
    This function is used to gather user input and return it as a tuple

    :return input_tuple: tuple of values
    ================================================================================================================="""

    print()
    print('Enter various values when prompted to obtain a graph with the desired parameters.')
    print('If you would like a general search, type "%" character in place of specific value.')
    print('If you would like to ignore a certain parameter, simply skip the input.')
    print()
    '''
    date = input('Enter a specific date (i.e. 20%%-04-%%): ')
    time = input('Enter a specific time (i.e. 4:%% PM: ')
    type = input('Enter a specific type of run (i.e. Easy, Long, etc.): ')
    distance = input('Enter a specific distance (i.e. 4.37): ')
    duration = input('Enter a specific duration (i.e. %%:40:%%): ')
    pace = input('Enter a specific pace (i.e. 7:3%): ')
    '''
    date, time, type, distance, duration, pace = ['2021-%%-%%', '%:%% %%', 'Long', '%.%', '%%:%%:%%', '%:%%']

    input_tuple = [date, time, type, distance, duration, pace]
    return input_tuple


def make_graph(db, input_tuple):
    """=================================================================================================================
    This function searches the connected database using values inside a tuple

    :param db: database cursor object
    :param input_tuple: tuple of values
    ================================================================================================================="""

    sq3 = f'''
        SELECT * 
        FROM runs
        WHERE date LIKE '{input_tuple[0]}'
        AND time LIKE '{input_tuple[1]}'
        AND type LIKE '{input_tuple[2]}'
        AND distance LIKE '{input_tuple[3]}'
        AND duration LIKE '{input_tuple[4]}'
        AND pace LIKE '{input_tuple[5]}'
        '''
    db.execute(sq3)
    rows = db.fetchall()

    # Gather dates and distances as np arrays
    dates = list()
    distances = list()
    for row in rows:
        dates.append(row[1])
        distances.append(row[4])
    array_dates = np.asarray(dates)
    array_distances = np.asarray(distances)

    # Plot date vs distance
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(array_dates, array_distances)
    ax.set_xlabel('Date')
    ax.set_ylabel('Distance (mi)')
    plt.xticks(rotation=90, fontsize=5)
    plt.show()


def main():
    """=================================================================================================================
    The main function calls get_input() to ask user for what graph they want to make. The returned list of values is put
    through search_database() to gather the data, which is passed through make_graph().
    ================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    input_tuple = get_input()
    make_graph(db, input_tuple)


main()
