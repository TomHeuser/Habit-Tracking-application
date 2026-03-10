import sqlite3
from os import name

from OOP.habit_class import TimeHabit, Habit
from OOP.history_class import HabitHistory

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_path = os.path.join(BASE_DIR, 'database.db')
#print(BASE_DIR)
#print(DB_path)
connection = sqlite3.connect(DB_path)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()



def fetch_all_habit_rows():
    """used to fetch all rows from the habits table"""
    cursor.execute("SELECT * FROM habit WHERE active = 1")
    connection.commit()
    return cursor.fetchall()

def fetch_all_inactive():
    """used to fetch all habits/rows from the habits table that are inactive"""
    cursor.execute("SELECT * FROM habit WHERE active = 0")
    connection.commit()
    return cursor.fetchall()

## generate all instances
def load_all_time_habits():
    """generates a TimeHabit instance for each Habit in habit table"""
    rows = fetch_all_habit_rows()
    return [TimeHabit.from_db(row) for row in rows]

def load_all_basic_habits():
    """generates a basic Habit instance for each Habit in habit table, while ignoring their interval values.
    Not relevant yet"""
    rows = fetch_all_habit_rows()
    return [Habit.from_db(row) for row in rows]

def load_all_inactive_habits():
    """generates a TimeHabit instance for each inactive Habit in habit table."""

## loads one instance
def load_single_time_habit(habit_id):
    """generates a TimeHabit instance for a single Habit in habit table. habit_id parameter must be passed."""
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    connection.commit()
    if row is None:
        return None
    return TimeHabit.from_db(row)

def load_single_basic_habit(habit_id):
    """generates a simple Habit instance for a single Habit in habit table (ignores interval values).
    habit_id parameter must be passed. Not relevant yet"""
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    connection.commit()
    if row is None:
        return None
    return Habit.from_db(row)

## updating or appending habit table
def update_single_row(update_data):
    """updates a single row from the habit table with given reference habit_id"""
    #print(cursor.rowcount)
    cursor.execute("UPDATE habit SET name = ?, desc = ?, active = ?, complete_status = ?, interval = ? "
                   "WHERE habit_id = ?", (update_data["name"], update_data["desc"], update_data["active"],
                                          update_data["complete_status"], update_data["interval"], update_data["habit_id"]))


    #print(cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (update_data["habit_id"],)).fetchone())
    #print(update_data["habit_id"])
    #print(cursor.rowcount)
    connection.commit()
    #print(cursor.rowcount)

def append_single_row(new_habit_data):
    """insert a new row at the end of habit table which auto increments new habit_id (represents "creating new habit")"""
    cursor.execute("INSERT INTO habit (name, desc, active, complete_status, interval, created_on) VALUES (?,?,?,?,?,?)",
                   (new_habit_data["name"], new_habit_data["desc"], new_habit_data["active"],
                    new_habit_data["complete_status"],new_habit_data["interval"], new_habit_data["created_on"]))
    connection.commit()

## fetching from habit table

def fetch_single_habit_history_all(habit_id):
    """fetches all rows from history for the given habit_id"""
    cursor.execute("SELECT * FROM history WHERE habit_id = ?", (habit_id,))
    connection.commit()
    #print(cursor.fetchall())
    return cursor.fetchall()

def fetch_single_habit_history_recent(habit_id):
    """fetches all rows from history for the given habit_id"""
    cursor.execute("SELECT * FROM history WHERE habit_id = ? ORDER BY history_id DESC LIMIT 1", (habit_id,))
    connection.commit()
    #print(cursor.fetchall())
    return cursor.fetchone()

def load_single_history_all(habit_id):
    """generates a HabitHistory instance for a single Habit. habit_id parameter must be passed."""
    ## , behind id to help python recognize it as a tuple
    rows = fetch_single_habit_history_all(habit_id)
    return [HabitHistory.from_db(row) for row in rows]

def load_single_history_recent(habit_id):
    """fetches the most recent row from history for the given habit_id"""
    row = fetch_single_habit_history_recent(habit_id)
    return HabitHistory.from_db(row)
## updating/appending history table




## when do we close database ? let it close automatically on application close?