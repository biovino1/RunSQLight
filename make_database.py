"""=====================================================================================================================
This scripts creates a SQLite database and imports data from many files.

Ben Iovino  3/28/2022   RunSQLight
===================================================================================================================="""

import os
import sqlite3 as sq3


def make_database_tables(db):
    """=================================================================================================================
    This function creates tables for the database
    :param db: database cursor from SQLite3
    ================================================================================================================="""

    sq3 = '''
        CREATE TABLE IF NOT EXISTS runs
        (   run_id TEXT PRIMARY KEY,
            datetime TEXT,
            type TEXT,
            distance FLOAT,
            duration TEXT,
            notes TEXT  )
        '''
    db.execute(sq3)

    sq3 = '''
        CREATE TABLE IF NOT EXISTS shoes
        (   shoe TEXT PRIMARY KEY,
            distance INTEGER    )
        '''
    db.execute(sq3)

def read_directory(path, db):
    """=================================================================================================================
    This function reads text files in a directory and inserts each line into database
    :param path: full directory path
    :return filelist: list of lines from file
    ================================================================================================================="""

    # Read each file in directory
    for file in os.listdir(path):
        with open(path+file, 'r') as f:

            # Assign each line in file to a variable to easily insert into db, some lines missing notes
            run_id = file.strip('.txt')
            lines = f.readlines()
            datetime, runtype, distance, duration = ([lines[i].split(' \n')[0] for i in range(0, 4)])
            if len(lines) == 5:
                notes = (lines[4].split(' \n')[0])
            else:
                notes = 'NA'

            # Insert into db
            params = (run_id, datetime, runtype, float(distance), duration, notes)
            sq3 = '''
                INSERT INTO runs
                    VALUES (?, ?, ?, ?, ?, ? );
                '''
            db.execute(sq3, params)


def main():
    """=================================================================================================================
    The main function connects database file and initializes the cursor object. read_file() is called to read each
    file in a directory. The returned list is sent to make_database_tables() where it is added to the database.
    ================================================================================================================="""
    
    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()
    make_database_tables(db)

    # Read directory and insert runs into database
    path = 'C:/Users/biovi/PycharmProjects/RunSQLight/Data/Runs/'
    read_directory(path, db)
    
    
main()
    
