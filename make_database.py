"""=====================================================================================================================
This scripts creates a SQLite database and imports data from many files.

Ben Iovino  3/28/2022   RunSQLight
===================================================================================================================="""

import os
import sqlite3 as sq3

def read_directory(path):
    """=================================================================================================================
    This function reads text files in a directory and returns each line as index in a list
    :param path: full directory path
    :return filelist: list of lines from file
    ================================================================================================================="""

    # Read each file in directory
    for file in os.listdir(path):
        with open(path+file, 'r') as f:

            # Assign each line in file to a variable to easily insert into db, some lines missing notes
            lines = f.readlines()
            if len(lines) == 4:
                datetime, runtype, distance, duration = ([lines[i].split(' \n')[0] for i in range(0, 4)])
                varlist = [datetime, runtype, distance, duration]
            if len(lines) == 5:
                datetime, runtype, distance, duration, notes = ([lines[i].split(' \n')[0] for i in range(0, 5)])
                varlist = [datetime, runtype, distance, duration, notes]


def make_database_tables(db):
    """=================================================================================================================
    This function creates tables for the database
    :param db: database cursor
    ================================================================================================================="""

    sq3 = '''
        CREATE TABLE IF NOT EXISTS  Runs
        (   run_id TEXT 
            distance INTEGER)
        '''
    db.execute(sq3)
    

def main():
    """=================================================================================================================
    The main function connects database file and initializes the cursor object. read_file() is called to read each
    file in a directory. The returned list is sent to make_database_tables() where it is added to the database.
    ================================================================================================================="""
    
    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()

    path = 'C:/Users/biovi/PycharmProjects/RunSQLight/Data/Runs/'
    read_directory(path)

    # make_database_tables(db)
    
    
main()
    
