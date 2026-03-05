## just a loose file to try out small code snippets ------> delete during/at the end of phase 3
import sqlite3

connection = sqlite3.connect("../database/database.db")
## to enable SQlite to make every row behave like a dictionary. -> call/access values by column name
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


class Habit:
    def __init__(self, habit_id, name, desc, active, complete_status, created_on):
        self.name = name
        self.habit_id = habit_id
        # user input to add description (str)
        self.desc = desc
        self.complete_status = complete_status
        self.active = active
        self.created_on = created_on

    @classmethod
    def from_db(cls, row):
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"],
                   complete_status=row["complete_status"], created_on=row["created_on"])

    ## manages how return is returned
    def __repr__(self):
        return f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, created_on={self.created_on})"

class TimeHabit(Habit):
    def __init__(self, name, habit_id, desc, active, complete_status, created_on, interval):
         Habit.__init__(self, habit_id, name, desc, active, complete_status, created_on)
         self.interval = interval

    @classmethod
    def from_db(cls, row):
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"], complete_status=row["complete_status"], created_on=row["created_on"], interval=row["interval"])

    ## manages how return is returned
    def __repr__(self):
        return f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, created_on={self.created_on}, interval={self.interval})"

## function to fetch ALL rows of a table
def fetch_all_rows():
    cursor.execute("SELECT * FROM habit")
    return cursor.fetchall()

## generate all instances
def load_all_time_habits():
    rows = fetch_all_rows()
    return [TimeHabit.from_db(row) for row in rows]

def load_all_basic_habits():
    rows = fetch_all_rows()
    return [Habit.from_db(row) for row in rows]

## loads one instance
def load_single_time_habit(habit_id):
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return TimeHabit.from_db(row)

def load_single_basic_habit(habit_id):
    ## , behind id to help python recognize it as a tuple
    cursor.execute("SELECT * FROM habit WHERE habit_id = ?", (habit_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return Habit.from_db(row)


all_habits = load_all_time_habits()
print(all_habits)

one_habit = load_single_time_habit(1)
print(one_habit)


connection.commit()
connection.close()









#from datetime import date
## move to habit creation
        #today = date.today()
        #iso_today = today.isoformat()