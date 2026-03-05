import sqlite3
import db_setup
from OOP.habit_class import TimeHabit, Habit


def fetch_all_habit_rows():
    """used to fetch all rows from the habits table"""
    cursor.execute("SELECT * FROM habit")
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

## loads one instance
def load_single_time_habit(habit_id):
    """generates a TimeHabit instance for a single Habit in habit table. habit_id parameter must be passed."""
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return TimeHabit.from_db(row)

def load_single_basic_habit(habit_id):
    """generates a simple Habit instance for a single Habit in habit table (ignores interval values).
    habit_id parameter must be passed. Not relevant yet"""
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return Habit.from_db(row)

db_setup.flush_history_table()
db_setup.flush_habit_table()
#db_setup.setup_habit_table()
#db_setup.setup_history_table()
#db_setup.seed_predefined_habits()


db_setup.database_startup()

# define connection and cursor
connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

all_habits = load_all_time_habits()
print(all_habits)

one_habit = load_single_time_habit(1)
print(one_habit)

connection.commit()
connection.close()