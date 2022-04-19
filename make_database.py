"""=====================================================================================================================
This scripts creates a SQLite database from data inside files.

Ben Iovino  4/9/22   RunSQLight
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
            distance REAL,
            duration TEXT,
            pace TEXT,
            notes TEXT  )
        '''
    db.execute(sq3)

    sq3 = '''
        CREATE TABLE IF NOT EXISTS shoes
        (   shoe TEXT PRIMARY KEY,
            distance INTEGER,
            retired TEXT    )
        '''
    db.execute(sq3)


def database_insert(db, dbh, table, params):
    """=================================================================================================================
    This function inserts data into the desired database table

    :param db: database cursor object
    :param dbh: database connection object
    :param table: database table name
    :param params: tuple of parameters
    ================================================================================================================="""

    # Determine how many values are being inserted
    values = ['?'] * len(params)
    values = ", ".join(values)

    # Insert into db
    sq3 = f'''
        INSERT INTO {table}
            VALUES ({values})
        '''
    db.execute(sq3, params)
    dbh.commit()


def read_directory(path, db, dbh):
    """=================================================================================================================
    This function reads text files in a directory and inserts each line into database by calling database_insert()

    :param path: full directory path
    :param db: database cursor object
    :param dbh: database connection object
    ================================================================================================================="""

    # Read runs file in the directory
    with open(path + 'runs.txt', 'r') as f:
        for line in f:

            # Split tabular line and assign each element to a variable
            line = line.rstrip()
            splitline = line.split('\t')
            run_id, datetime, runtype, distance, duration, pace = ([splitline[i] for i in range(0, 6)])
            if len(splitline) == 7:
                notes = (splitline[6])
            else:
                notes = 'NA'

            # Insert into db
            params = (run_id, datetime, runtype, float(distance), duration, pace, notes)
            database_insert(db, dbh, 'runs', params)

    # Read shoes file in the directory
    with open(path + 'shoes.txt', 'r') as f:
        for line in f:

            # Split tabular line and assign each element to a variable
            line = line.rstrip()
            splitline = line.split('\t')
            shoe_id, distance = ([splitline[i] for i in range(0, 2)])

            # Set retired column to 'Y' for all shoes
            retired = 'Y'

            # Insert into db
            params = (shoe_id, distance, retired)
            database_insert(db, dbh, 'shoes', params)


def main():
    """=================================================================================================================
    The main function connects database file and initializes the cursor object. make_database_tables() is called with
    cursor object to create desired tables. read_directory() is called with initialized path to read files and insert
    data into database.
    ================================================================================================================="""

    dbh = sq3.connect('RunSQLight.db')
    db = dbh.cursor()
    make_database_tables(db)

    # Read directory and insert runs into database
    path = 'C:/Users/biovi/PycharmProjects/RunSQLight/Data/'
    read_directory(path, db, dbh)


main()

