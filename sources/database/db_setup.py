import sqlite3
import json

# create habit table
# BOOL values are integers in SQlite 0 (false) 1 (true)

def setup_habit_table():
    """used to create an empty habits table"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    habit_table_create = """CREATE TABLE IF NOT EXISTS habit(habit_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, active INTEGER,
    interval INTEGER, complete_status INTEGER, created_on TEXT)"""
    cursor.execute(habit_table_create)
    connection.commit()
    connection.close()

def setup_history_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    history_table_create = """CREATE TABLE IF NOT EXISTS history(history_id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER NOT NULL, 
    date TEXT, streak_status INTEGER, streak_count INTEGER, FOREIGN KEY (habit_id) REFERENCES habit(habit_id))"""
    cursor.execute(history_table_create)
    connection.commit()
    connection.close()


def seed_predefined_habits():
    """used to fill empty habits table with predefined habits"""
    ## read data from JSON file
    with open("initial_data.json", "r") as f:
        data = json.load(f)
    # print(data)
    # print(type(data))

    ##connect to database
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")

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
            "INSERT INTO habit (name, desc, active, complete_status, created_on) VALUES (?,?,?,?,?)",
            (
                habit_data["name"],
                habit_data["desc"],
                habit_data["active"],
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
    connection.close()


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
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS habit")
    connection.commit()
    connection.close()

def flush_history_table():
    """used to flush the history table, only for testing"""
    # define connection and cursor
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS history")
    connection.commit()
    connection.close()