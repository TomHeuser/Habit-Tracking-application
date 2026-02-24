import sqlite3
import db_setup

db_setup.flush_history_table()
db_setup.flush_habit_table()
#db_setup.setup_habit_table()
#db_setup.add_predefined_habits()
#db_setup.setup_history_table()
#db_setup.add_history_data()

db_setup.database_startup()

# define connection and cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


#print rows from habit table
for row in cursor.execute("select * from habit"):
    print(row)

#print rows from history table
for row in cursor.execute("select * from history"):
    print(row)

#print specific row
for row in cursor.execute("select * from habit WHERE active = 1"):
    print(row)

for row in cursor.execute("select * from habit WHERE habit_id = 1"):
    print(row)

connection.commit()
connection.close()