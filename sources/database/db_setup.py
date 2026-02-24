import sqlite3

# create habit table
# BOOL values are integers in SQlite 0 (false) 1 (true)

def setup_habit_table():
    """used to create an empty habits table"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    habit_table_create = """CREATE TABLE IF NOT EXISTS habit(habit_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, active INTEGER,
    interval INTEGER, complete_status INTEGER)"""
    cursor.execute(habit_table_create)
    connection.commit()
    connection.close()

def setup_history_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    history_table_create = """CREATE TABLE IF NOT EXISTS history(history_id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER NOT NULL,
    created_on TEXT, date TEXT, streak_status INTEGER, streak_count INTEGER, FOREIGN KEY (habit_id) REFERENCES habit(habit_id))"""
    cursor.execute(history_table_create)
    connection.commit()
    connection.close()


def add_predefined_habits():
    """used to fill empty habits table with predefined habits"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    #list of predefined habits
    predefined_habits = [
        (1, "Drink Water", "Drink two liters of water each day", 1, 1, 0),
        (2, "Walking", "Spend at least 15 minutes walking outside each day", 1, 1, 0),
        (3, "Cleaning", "Clean the apartment", 1, 7, 0),
        (4, "Go swimming", "Swim at least 100 laps (50m) each week", 1, 7, 0),
        (5, "Check finances", "check your banking accounts", 1, 7,0)
    ]
    # add predefined habits to habit table
    cursor.executemany("INSERT INTO habit values (?,?,?,?,?,?)", predefined_habits)
    connection.commit()
    connection.close()

def add_history_data():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    history_data = [
        (1, 1, "2026-01-01", "2026-01-01", 0, 0),
        (2, 2, "2026-01-01", "2026-01-01", 0, 0),
        (3, 3, "2026-01-01", "2026-01-01", 0, 0),
        (4, 4, "2026-01-01", "2026-01-01", 0, 0),
        (5, 5, "2026-01-01", "2026-01-01", 0, 0)
    ]

    cursor.executemany("INSERT INTO history values (?,?,?,?,?,?)", history_data)
    connection.commit()
    connection.close()

def database_startup():
    """runs on application startup and checks if database with predefined habits exists. If not it creates the necessary tables"""
    try:
        setup_habit_table()
        add_predefined_habits()
        setup_history_table()
        add_history_data()
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