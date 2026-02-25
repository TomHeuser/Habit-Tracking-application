## just a loose file to try out small code snippets ------> delete during/at the end of phase 3
import db_setup
import json
import sqlite3

## prepare/clean database
db_setup.flush_history_table()
db_setup.flush_habit_table()
db_setup.setup_habit_table()
db_setup.setup_history_table()


## read data from JSON file
with open("initial_data.json", "r") as f:
    data = json.load(f)
#print(data)
#print(type(data))

##connect to database
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
connection.execute("PRAGMA foreign_keys = ON;")


## sorty data by interval dailies first, then weekly
data.sort(key=lambda habit: habit["interval"])
#for habit in data:
    #print(habit)

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
        #print("History Row:", entry)
        cursor.execute(
            "INSERT INTO history (habit_id, date, streak_status, streak_count) VALUES (?,?,?,?)",
            (
                habit_id,
                entry["date"],
                entry["streak_status"],
                entry["streak_count"]
            )
        )

    #for i in data:
    #if


connection.commit()
connection.close()