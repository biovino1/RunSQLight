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
    print('If you would like to ignore a certain parameter, simply skip the question.')
    print()

    dates = input('Enter two dates to obtain all runs between: ')
    type = input('Enter a specific type of run: ')
    distance = input('Enter a specific distance: ')
    duration = input('Enter a specific duration: ')
    shoe = input('Enter a specific shoe: ')

def main():
    """=====================================================================================================================
    The main function calls get_input() to ask user for what graph they want to make. The returned list of values is put
    through search_database() to gather the data, which is passed through make_graph().
    ===================================================================================================================="""

    input_tuple = get_input()

main()
