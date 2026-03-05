## just a loose file to try out small code snippets ------> delete during/at the end of phase 3
import sqlite3
from OOP.habit_class import TimeHabit

#from datetime import date
## move to habit creation
        #today = date.today()
        #iso_today = today.isoformat()


connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


def fetch_all_habit_rows():
    """used to fetch all rows from the habits table"""
    cursor.execute("SELECT * FROM habit")
    return cursor.fetchall()

## loads one instance
def load_single_time_habit(habit_id):
    """generates a TimeHabit instance for a single Habit in habit table. habit_id parameter must be passed."""
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return TimeHabit.from_db(row)



one_habit = load_single_time_habit(1)
print(one_habit)

one_habit.change_name()
print(one_habit)

connection.commit()
connection.close()