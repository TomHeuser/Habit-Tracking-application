import sqlite3

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

def get_name_for_id(habit_id):
    """used to fetch name from habit for given habit_id"""
    cursor.execute("SELECT name FROM habit WHERE habit_id = ?", (habit_id,))
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return row["name"]

def get_desc_for_id(habit_id):
    """used to fetch description from habit for given habit_id"""
    cursor.execute("SELECT desc FROM habit WHERE habit_id = ?", (habit_id,))
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return row["desc"]

def get_active_for_id(habit_id):
    """used to fetch active (0 or 1) from habit for given habit_id"""
    cursor.execute("SELECT active FROM habit WHERE habit_id = ?", (habit_id,))
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return row["active"]

def get_complete_status_for_id(habit_id):
    cursor.execute("SELECT complete_status FROM habit WHERE habit_id = ?", (habit_id,))
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return row["complete_status"]

def get_interval(habit_id):
    """used to fetch the interval for the habit, with the passed in Habit_id"""
    cursor.execute("SELECT interval FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    connection.commit()
    if row is None:
        return None
    return row["interval"]

def get_creation_date(habit_id):
    """used to fetch the creation date for the habit, with the passed in Habit_id"""
    cursor.execute("SELECT created_on FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    connection.commit()
    if row is None:
        return None
    return row["created_on"]


def get_max_id():
    """used to fetch max id from habit table"""
    cursor.execute("SELECT habit_id FROM habit ORDER BY habit_id DESC LIMIT 1")
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return 0
    return row["habit_id"]

def fetch_all_habit_rows():
    """used to fetch all rows of active habits from the habits table"""
    cursor.execute("SELECT * FROM habit WHERE active = 1")
    connection.commit()
    return cursor.fetchall()

def fetch_all_inactive():
    """used to fetch all habits/rows from the habits table that are inactive"""
    cursor.execute("SELECT * FROM habit WHERE active = 0")
    connection.commit()
    return cursor.fetchall()

def fetch_active_names():
    """used to fetch id and names of all active habits from the habits table"""
    cursor.execute("SELECT habit_id, name FROM habit WHERE active = 1")
    connection.commit()
    rows = cursor.fetchall()
    if rows is None:
        return None
    return [{"habit_id" : row["habit_id"], "name" : row["name"]} for row in rows]

def fetch_active_ids():
    """used to fetch ids of all active habits from the habits table"""
    cursor.execute("SELECT habit_id FROM habit WHERE active = 1")
    connection.commit()
    rows = cursor.fetchall()
    if rows is None:
        return None
    return [row["habit_id"] for row in rows]

def fetch_inactive_names():
    """used to fetch id and names of all inactive habits from the habits table"""
    cursor.execute("SELECT habit_id, name FROM habit WHERE active = 0")
    connection.commit()
    rows = cursor.fetchall()
    if rows is None:
        return None
    return [{"habit_id": row["habit_id"], "name": row["name"]} for row in rows]

def fetch_names():
    """used to fetch id and names of all habits form habit table"""
    cursor.execute("SELECT habit_id, name FROM habit")
    connection.commit()
    rows = cursor.fetchall()
    return [{"habit_id": row["habit_id"], "name": row["name"]} for row in rows]

def fetch_single_habit_details(chosen_id):
    """used to fetch details of a single habit from the habits table and return them as a list of dictionaries"""
    cursor.execute("SELECT habit_id, name, desc, active, interval, complete_status, created_on, streak_status, "
                   "streak_count FROM habit WHERE habit_id = ?", (chosen_id,))
    connection.commit()
    row = cursor.fetchone()
    if row is None:
        return None
    return {"habit_id": row["habit_id"], "name": row["name"], "desc": row["desc"], "active": row["active"],
            "interval": row["interval"], "complete_status": row["complete_status"], "created_on": row["created_on"],
            "streak_status": row["streak_status"], "streak_count": row["streak_count"]}

def fetch_highest_current_streak():
    """used to fetch the highest current streak from habit table (technically identical in both tables)
    returns list of dictionaries"""
    cursor.execute("SELECT habit_id, name, streak_count FROM habit "
                   "WHERE streak_count = (SELECT MAX(streak_count) FROM habit) ORDER BY habit_id")
    connection.commit()
    rows = cursor.fetchall()
    return [{"habit_id": row["habit_id"], "name": row["name"], "streak_count": row["streak_count"]} for row in rows]

def fetch_highest_history_streak():
    """used to fetch the highest streak from history table, returns list of dictionaries"""
    cursor.execute("SELECT habit_id, streak_count FROM history "
                   "WHERE streak_count = (SELECT MAX(streak_count) FROM history) ORDER BY habit_id")
    connection.commit()
    rows = cursor.fetchall()
    return [{"habit_id": row["habit_id"], "streak_count": row["streak_count"]} for row in rows]

def fetch_all_history_for_habit(chosen_id):
    """used to fetch all history entries for a given habit with the chosen id"""
    cursor.execute("SELECT date, complete_status, streak_status, streak_count FROM history "
                   "WHERE habit_id = ?", (chosen_id,))
    connection.commit()
    rows = cursor.fetchall()
    return [{"date": row["date"], "complete_status": row["complete_status"], "streak_status": row["streak_status"],
             "streak_count": row["streak_count"]} for row in rows]

## generate all instances
def load_all_time_habits():
    """generates a TimeHabit instance for each Habit in habit table"""
    rows = fetch_all_habit_rows()
    return [TimeHabit.from_db(row) for row in rows]

#def load_all_basic_habits():
    #"""generates a basic Habit instance for each Habit in habit table, while ignoring their interval values.
    #Not relevant yet"""
    #rows = fetch_all_habit_rows()
    #return [Habit.from_db(row) for row in rows]


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

#def load_single_basic_habit(habit_id):
   #"""generates a simple Habit instance for a single Habit in habit table (ignores interval values).
   # habit_id parameter must be passed. Not relevant yet"""
   # ## , behind id to help python recognize it as a tuple
   # cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    #row = cursor.fetchone()
    #connection.commit()
    #if row is None:
        #return None
    #return Habit.from_db(row)

## updating or appending habit table
def update_single_row(update_data):
    """updates a single row from the habit table with given reference habit_id"""
    #print(cursor.rowcount)
    cursor.execute("UPDATE habit SET name = ?, desc = ?, active = ?, complete_status = ?, interval = ?, streak_status = ?, streak_count = ? "
                   "WHERE habit_id = ?", (update_data["name"], update_data["desc"], update_data["active"],
                                          update_data["complete_status"], update_data["interval"], update_data["streak_status"], update_data["streak_count"], update_data["habit_id"]))


    #print(cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (update_data["habit_id"],)).fetchone())
    #print(update_data["habit_id"])
    #print(cursor.rowcount)
    connection.commit()
    #print(cursor.rowcount)

def append_single_row(new_habit_data):
    """insert a new row at the end of habit table which auto increments new habit_id (represents "creating new habit")"""
    cursor.execute("INSERT INTO habit (name, desc, active, complete_status, interval, created_on, streak_status, streak_count) VALUES (?,?,?,?,?,?,?,?)",
                   (new_habit_data["name"], new_habit_data["desc"], new_habit_data["active"],
                    new_habit_data["complete_status"],new_habit_data["interval"], new_habit_data["created_on"],
                    new_habit_data["streak_status"],new_habit_data["streak_count"]))
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

def append_history(history_data):
    """insert a new row at the end of history table which auto increments new habit_id (represents "adding new event")"""
    cursor.execute("INSERT INTO history (habit_id, date, complete_status, streak_status, streak_count) VALUES (?,?,?,?,?)",
                   (history_data["habit_id"], history_data["date"], history_data["complete_status"], history_data["streak_status"],history_data["streak_count"]))
    connection.commit()

def update_history(history_data):
    """updates a row of the history table where id and date are equal to input data (represents "changing event")"""
    cursor.execute("UPDATE history SET complete_status = ?, streak_status = ?, streak_count = ? "
        "WHERE habit_id = ? AND date = ?", (history_data["complete_status"], history_data["streak_status"],history_data["streak_count"], history_data["habit_id"],history_data["date"]))
    connection.commit()

def check_existing_history_date(habit_id, iso_today):
    """check whether a row exists in history for current date and given habit_id. Returns True of False"""
    cursor.execute("SELECT * FROM history WHERE habit_id = ? AND date = ?", (habit_id, iso_today))
    row = cursor.fetchone()
    connection.commit()
    #print(type(iso_today))
    #print(f"looking for id: {habit_id}, date: {iso_today}")
    #print(cursor.execute("SELECT * FROM history").fetchall())
    #print(row)
    if row is None:
        return False
    else:
        return True

## functions for startup handling
def get_daily_id_list():
    """used to fetch all id for current weekly habits, necessary for startup computation"""
    cursor.execute("SELECT habit_id FROM habit WHERE active = 1 AND interval = 1")
    rows = cursor.fetchall()
    connection.commit()
    return [row["habit_id"] for row in rows]

def get_weekly_id_list():
    """used to fetch all id for current weekly habits, necessary for startup computation"""
    cursor.execute("SELECT habit_id FROM habit WHERE active = 1 AND interval = 7")
    rows = cursor.fetchall()
    connection.commit()
    return [row["habit_id"] for row in rows]

def get_manual_id_list():
    """used to fetch all id for current habits, that are neither daily, nor weekly. Necessary for startup computation"""
    cursor.execute("SELECT habit_id FROM habit WHERE active = 1 AND interval != 7 AND interval != 1")
    rows = cursor.fetchall()
    connection.commit()
    return [row["habit_id"] for row in rows]

def get_last_entry(habit_id):
    """used to fetch last entry for given habit_id where completed == 1 and return date"""
    cursor.execute("SELECT date FROM history WHERE habit_id = ? AND complete_status = 1 ORDER BY date desc LIMIT 1", (habit_id,))
    row = cursor.fetchone()
    connection.commit()
    return row["date"]

def startup_habit_incomplete(habit_id):
    """Sets a habits complete status to 0 in habit table during startup computation"""
    cursor.execute("UPDATE habit SET complete_status = 0 WHERE habit_id = ?", (habit_id,))
    connection.commit()

def startup_habit_reset(habit_id):
    """Sets a habits complete status, streak status and streak count to 0 in habit table during startup computation"""
    cursor.execute("UPDATE habit SET complete_status = 0, streak_status = 0, streak_count = 0 WHERE habit_id = ?", (habit_id,))
    connection.commit()
## when do we close database ? let it close automatically on application close?