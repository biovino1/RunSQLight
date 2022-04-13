"""=====================================================================================================================
This scripts prompts the user for data to insert into the connected database. Weather data is taken from weather
underground and inserted as well.

Ben Iovino  4/12/22   RunSQLight
===================================================================================================================="""

import sqlite3 as sq3
import selenium


def get_weather(zipcode):
    """=================================================================================================================
    This function is used to get weather data from weather underground

    :param zipcode: 5 digit number i.e. 47906
    =============================================================================================================="""

    driver = webdriver.Firefox()
    driver.get('https://www.wunderground.com')

    search_bar = driver.find_element_by_id('wuSearch')
    search_bar.sendKeys(zipcode)


def get_input():
    """=================================================================================================================
    This function is used to gather user input and return it as a tuple

    :return userinput: tuple of values
    ================================================================================================================="""

    flag = True
    while flag == True:
        datetime = input('Enter date and time (i.e. 2022-01-01 12:00 AM): ')
        #type = input('Enter type of run: ')
        #distance = float(input('Enter distance of run: '))
        #duration = input('Enter duration of run (i.e. HH:MM:SS): ')
        zipcode = input('Enter zipcode to get weather: ')
        #notes = input('Notes: ')
        '''
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
    '''

    # Scrape weather by putting zipcode into get_weather()
    get_weather(zipcode)

    '''
    # Return input
    input_tuple = [datetime, type, distance, duration, pace, notes]
    print(input_tuple)
    return input_tuple
    '''


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
