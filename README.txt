**************************************************************************************************************
# RunSQLite 1.0: Application For Logging Your Runs
**************************************************************************************************************

This project creates an easy to use graphical interface that interacts with an SQLite database to store runs
and shoes using SQLite and the graphics.py library. In order for the graphics library to work, graphics.py must 
be located in the same directory as RunSQLight.py.

This repository already contains all the necessary components for this application to work without running any
of the other scripts. Below is the outline of steps that were taken to create the necessary files.

1. Run parse_tabular.py on log.txt (personal data downloaded from runningahead.com) --> ./Data
2. Run make_database.py on ./Data --> RunSQLite.db

RunSQLite.py connects to RunSQLite.db to insert/update/query data from the original log.txt file. time_calculator.py
another graphical interface that can be used to add together time, separate from RunSQLite.py so they can be run
side by side.

To protect some personal data, notes from the original log.txt file have been removed and replaced with strings
of random characters and spaces.

When trying to exit out of a window, make sure to press the red box with an 'X' or 'EXIT' inside the graphic to keep
the program running.



