"""=====================================================================================================================
This scripts searches through an SQLite database and makes graphs based on user parameters.

Ben Iovino  4/19/22   RunSQLight
===================================================================================================================="""

import sqlite3 as sq3
import matplotlib


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
    dates = input('Enter two dates to obtain all runs between (i.e. 2022-04-24): ')
    type = input('Enter a specific type of run (i.e. Easy, Long, etc.): ')
    distance = input('Enter a specific distance (i.e. 4): ')
    duration = input('Enter a specific duration (i.e. 00:40:00): ')
    pace = input('Enter a specific pace (i.e. 7:37): ')
    shoe = input('Enter a specific shoe: ')
    '''

    dates, type, distance, pace, duration, shoe = ['', 'Easy', '6.%', '', '', '']

    input_tuple = [dates, type, distance, pace, duration, shoe]
    return input_tuple


def make_graph(db, input_tuple):
    """=================================================================================================================
    This function unpacks a tuple and searches the connected database using values inside tuple

    :param db: database cursor object
    :param input_tuple: tuple of values
    ================================================================================================================="""

    sq3 = '''
        SELECT * 
        FROM 
        '''
    db.execute(sq3)
    rows = db.fetchall()
    for row in rows:
        print(row)

def main():
    """=====================================================================================================================
    The main function calls get_input() to ask user for what graph they want to make. The returned list of values is put
    through search_database() to gather the data, which is passed through make_graph().
    ===================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    input_tuple = get_input()
    make_graph(db, input_tuple)


main()
