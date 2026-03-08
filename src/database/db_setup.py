import sqlite3
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "initial_data.json")

if __name__ == "__main__":
    from database.db import cursor, connection
else:
    from .db import cursor, connection


def setup_habit_table():
    """used to create an empty habits table"""

    habit_table_create = """CREATE TABLE habit(habit_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, active INTEGER,
    interval INTEGER, complete_status INTEGER, created_on TEXT)"""
    cursor.execute(habit_table_create)
    connection.commit()

def setup_history_table():
    """Used to create an empty history table"""


    history_table_create = """CREATE TABLE history(history_id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER NOT NULL, 
    date TEXT, streak_status INTEGER, streak_count INTEGER, FOREIGN KEY (habit_id) REFERENCES habit(habit_id))"""
    cursor.execute(history_table_create)
    connection.commit()




def seed_predefined_habits():
    """used to seed empty tables with predefined habits"""
    ## read data from JSON file
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
    # print(data)
    # print(type(data))

    ## sorty data by interval: dailies first, then weekly
    data.sort(key=lambda habit: habit["interval"])
    # for habit in data:
    # print(habit)

    ## for loop to iterate through each habit in JSON file one at a time
    for habit in data:
        ##dictionary comprehension - habit.items() gives key-value pairs --> for each pair in key != "history" add it to new dictionary
        habit_data = {a: b for a, b in habit.items() if a != "history"}
        print(habit_data)
        ## only need to get history keys and puts it into a new list containing dictionaries for each entry
        history_data = habit.get("history", [])
        print(history_data)

        ## insert habit_data into habit table
        cursor.execute(
            "INSERT INTO habit (name, desc, active, interval, complete_status, created_on) VALUES (?,?,?,?,?,?)",
            (
                habit_data["name"],
                habit_data["desc"],
                habit_data["active"],
                habit_data["interval"],
                habit_data["complete_status"],
                habit_data["created_on"]
            )
        )

        ## tell python to get newly generated habit_id from habit table
        habit_id = cursor.lastrowid

        ## insert history_data into history table
        for entry in history_data:
            # print("History Row:", entry)
            cursor.execute(
                "INSERT INTO history (habit_id, date, streak_status, streak_count) VALUES (?,?,?,?)",
                (
                    habit_id,
                    entry["date"],
                    entry["streak_status"],
                    entry["streak_count"]
                )
            )

    connection.commit()


def database_startup():
    """runs on application startup and checks if database with predefined habits exists. If not it creates the necessary tables"""
    try:
        setup_habit_table()
        setup_history_table()
        seed_predefined_habits()
        print("Database loading....")
        print("Database setup completed.")
    except:
        print("Database loading....")
        print("Existing Database successfully detected.")



def flush_habit_table():
    """used to flush the habit table, only for testing"""
    # define connection and cursor
    cursor.execute("DROP TABLE IF EXISTS habit")
    connection.commit()

def flush_history_table():
    """used to flush the history table, only for testing"""
    # define connection and cursor
    cursor.execute("DROP TABLE IF EXISTS history")
    connection.commit()