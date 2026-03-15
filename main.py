import sqlite3

from main_util import main_util
from OOP import habit_class
from database import db
from database import db_setup


##during startup
#db_setup.flush_history_table()
#db_setup.flush_habit_table()
db_setup.database_startup()
#db_setup.seed_predefined_habits()


one_habit = db.load_single_time_habit(2)
print(one_habit)

one_habit.change_complete_status()
print(one_habit)

update_data = one_habit.get_update_data()
print(f"update_data = {update_data}")

db.update_single_row(update_data)

history_data = one_habit.get_history_data()
db.append_history(history_data)


one_habit = db.load_single_time_habit(2)
print(f"habit with habit_id = 2: {one_habit}")

one_habit.change_complete_status()
print(one_habit)

update_data = one_habit.get_update_data()
print(f"update_data = {update_data}")

db.update_single_row(update_data)

history_data = one_habit.get_history_data()
db.append_history(history_data)


one_habit = db.load_single_time_habit(2)
print(f"habit with habit_id = 2: {one_habit}")

