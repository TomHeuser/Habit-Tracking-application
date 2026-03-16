## just a loose file to try out small code snippets ------> delete during/at the end of phase 3


#from datetime import date
        #today = date.today()
        #iso_today = today.isoformat()
# date has method called isocalendar() returning week number of given date -> use for week calculation later?

def id_names():
    names = db.fetch_active_names()
    for habit in names:
        # print(type(names))
        # print(type(names[0]))
        habit_id = habit["habit_id"]
        habit_name = habit["name"]
        print(f"{habit_id} {habit_name}")


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

history_data = one_habit.get_history_data()
db.append_history(history_data)

one_habit = db.load_single_time_habit(1)
print(f"habit with habit_id = 1: {one_habit}")


new_habit_data = main_util.create_new_habit()
print(type(new_habit_data))
print(new_habit_data)
db.append_single_row(new_habit_data)

habit_history_rows = db.fetch_single_habit_history_all(1)
print(habit_history_rows)

habit_history = db.load_single_history_all(1)
print(habit_history)

habit_history_recent = db.load_single_history_recent(1)
print(habit_history_recent)