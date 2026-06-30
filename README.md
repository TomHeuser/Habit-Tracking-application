# Unnecessary German Efficiency -
## a slightly sarcastic habit tracking app

###
####
This is a classic and rather basic habit tracking application, that helps you track and master your habits.

## Requirements:
- Python 3.12.5
- everything else is listed inside the requirements.txt file

## Features:
- add, change, delete or choose from predefined habits
- keep track of these habits by regularly checking them off, resulting in a streak
- not checking off a habit within a defined number of days will result in te habits streak to be reset
- daily, weekly and custom habit intervals (1-365 days) included
- access history, records and other analytics
- one user only
- CLI based

## project contents:
- Python based program
- database using SQLite 3
- JSON file that holds data for testing purposes
- src container holding source code
- main.py holding the program lifecycle
- 5 modules listed below

### files and modules:

- analytics:
  - analytics.py holding purely analytic functions
  - functions_util.py holding non-object-oriented function that are not strictly purely analytical
- cli:
  - analytics_menu.py
  - edit_habit_menu.py
  - habits_menu.py
  - manage_menu.py
  - cli_util.py
- database:
  - SQLite3 database
  - db.py holding all functions to handle reading and writing to and from database
  - initial_data.json hold predefined data for testing purposes
  - db_setup.py  responsible for handling database setup and seeding of predefined data
- main_util:
  - handle_dates.py handles global date variables, that might need to be manipulated when in testing mode
  - main_util.py holding classic, basic functions that are useful everywhere throughout the program
- OOP:
  - habit_class.py handling short term processes
  - history_class.py handling long term processes and data, if necessary


## installation instructions:

- Installation:
  1. Setup and activate virtual environment (venv) running on Python 3.12.5
  2. install dependencies:
      - pip install -r requirements.txt
  3. running tests:
    - conftest.py handles automatic database setup and resets etc.
    - run basic tests:
      - pytest
    - run pytest with coverage:
      - pytest --cov
####
- when testing or evaluating the program DURING PROGRAM RUNTIME:
  - please always enter testing mode, otherwise the handling of the current date etc. will be flawed
  - to enter testing mode:
    - when the application starts up the user is prompted to press 'enter' to start
    - BUT instead of hitting enter, we can simply hit 't'
    - THEN we are asked whether we want to enter testing mode → to do so press 't' again
    - NOW the global variables that handle dates will be synchronized to the dates from our testing data allowing us to properly test
    - this feature is 'hidden' to keep users from accidentally entering testing mode, since that will wipe the existing database tables


## possible future improvements:
- graph visualization of analytic results
- habits that don't rely on an actual time interval ("To-Do-lists")
- implementation of database backup and export
- implementation of a basic GUI

