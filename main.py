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



one_habit = db.load_single_time_habit(1)
print(one_habit)

one_habit.change_name()
print(one_habit)

one_habit.change_desc()
print(one_habit)

one_habit.change_active()
print(one_habit)

one_habit.change_complete_status()
print(one_habit)

one_habit.change_interval()
print(one_habit)


update_data = one_habit.get_update_data()
print(f"update_data = {update_data}")

db.update_single_row(update_data)

one_habit = db.load_single_time_habit(1)
print(f"habit with habit_id = 1: {one_habit}")


new_habit_data = main_util.create_new_habit()
print(type(new_habit_data))
print(new_habit_data)
db.append_single_row(new_habit_data)