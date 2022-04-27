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
    print('Enter two dates that you would like to graph: ')
    print()

    date1 = '2021-01-01'
    date2 = '2021-01-31'
    dates = date1, date2

    date, time, type, distance, duration, pace = ['2021-%%-%%', '%:%% %%', 'Long', '%.%', '%%:%%:%%', '%:%%']

    input_tuple = [date, time, type, distance, duration, pace]
    return input_tuple, dates


def make_graph(db, input_tuple, dates):
    """=================================================================================================================
    This function searches the connected database using values inside a tuple

    :param db: database cursor object
    :param input_tuple: tuple of values
    ================================================================================================================="""

    print(dates)
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
    sq31 = f'''
        SELECT *
        FROM runs
        WHERE date
        BETWEEN '{dates[0]}'
        AND '{dates[1]}'
        '''
    db.execute(sq31)
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

    input_tuple, dates = get_input()
    make_graph(db, input_tuple, dates)


main()
