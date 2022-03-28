"""=====================================================================================================================
This scripts creates a SQLite database and imports data from many files.

Ben Iovino  3/28/2022   RunSQLight
===================================================================================================================="""

import os
import sqlite3 as sq3

def read_file(file):
    """=================================================================================================================
    This function reads a text file delimited by '\n' and returns each line as index in a list
    :param file: .txt file
    :return filelist: list of lines from file
    ================================================================================================================="""



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

    for file in
    make_database_tables(db)
    
    
main()
    
