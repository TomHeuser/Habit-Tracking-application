import sqlite3

# define connection and cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# create habit table
# BOOL values are integers in SQlite 0 (false) 1 (true)

command1 = """CREATE TABLE IF NOT EXISTS habit(habit_id INTEGER PRIMARY KEY, name TEXT, desc TEXT, active INTEGER,
 complete_status INTEGER, completed_on TEXT, interval INTEGER, streak_status INTEGER, streak_count INTEGER)"""

cursor.execute(command1)


#list of predefined habits
predefined_habits = [
    (1, "Drink Water", "Drink two litres of water each day", 1, 0, "2026-01-01", 1, 0, 0)
    (2, "Walking", "Spend at least 15 minutes walking outside each day", 1, 0, "2026-01-01", 1, 0, 0)
    (3, "Cleaning", "Clean the apartment", 1, 0, "2026-01-01", 1, 0, 0)
    (4, "Go swimming", "Swim at least 100 laps (50m) each week", 1, 0, "2026-01-01", 1, 0, 0)
    (5, "Check finances", "check your banking accounts", 1, 0, "2026-01-01", 1, 0, 0)
]
# add predefined habits to habit table
cursor.executemany("INSERT INTO habit (?,?,?,?,?,?,?,?,?,?)", predefined_habits)


connection.close()