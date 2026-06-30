from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db

## functions for habit_menu.py
def create_habit_obj(habit_id):
    """used in habit_menu to create habit object for habits stored in database that hold habit_idd == to passed in habit_id"""
    current_habit_obj = db.load_single_time_habit(habit_id)
    return current_habit_obj

def change_habit_obj_complete(habit_id):
    """Used in habit menu to automatically handle object completion and table updating.
    1. Creates an object for habit that shares passed in habit_id
    2. Computes completion and streak status and count
    3. Automatically updates row in habit table
    4. Automatically decides whether to append or update row in habits table"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.change_complete_status()
    update_data = current_habit_obj.get_update_data()
    db.update_single_row(update_data)
    history_data = current_habit_obj.get_history_data()
    habit_id = current_habit_obj.habit_id
    current_day = hd.current_day
    #print(current_day)
    existing_history_date = db.check_existing_history_date(habit_id, current_day)
    if existing_history_date == False:
        db.append_history(history_data)
    elif existing_history_date == True:
        db.update_history(history_data)
    else:
        print("Error writing to history table.")

def get_list_of_active_habits():
    """Used in menus to get list of all active habits"""
    active_habits = db.fetch_active_names()
    for item in active_habits:
        print(item["habit_id"], item["name"])
    print("")
    # print(type(active_habits))

## functions for analytics_menu.py

def get_list_of_all_habits():
    """Used in analytics_menu to get list of all habits"""
    print("Current habits:")
    all_habits = db.fetch_names()
    for item in all_habits:
        print(f"[{item["habit_id"]}] {item["name"]}")
    print("")

def print_habit_details_of_selected_habit(chosen_id):
    """Used in analytics_menu to print habit details for habit in habit table with habit_id ==  the passed in habit_id"""
    try:
        habit_details = db.fetch_single_habit_details(chosen_id)
        # print(type(habit_detail))
        # print(habit_details["habit_id"], habit_details["name"], habit_details["desc"], habit_details["active"],
        # habit_details["interval"], habit_details["complete_status"], habit_details["created_on"],
        # habit_details["streak_status"], habit_details["streak_count"])
        #print("habit details:")
        print(f"Habit details:\n"
              f"Habit name: {habit_details['name']}\n"
              f"Habit description: {habit_details['desc']}")
        if habit_details["active"] == 1:
            print("This habit is currently active.")
        else:
            print("This habit is currently inactive.")
        print(f"Habit interval: {habit_details['interval']}")
        if habit_details["complete_status"] == 1:
            print("currently completed.")
        else:
            print("Currently incomplete.")
        print(f"Created at {habit_details['created_on']}")
        if habit_details["streak_status"] == 1:
            print("This habit is currently on a streak.")
        else:
            print("This habit is not on a streak at the moment.")
        print(f"Number of consecutive completions: {habit_details['streak_count']}"
              f"")
        try:
            last_completion = db.get_last_entry(chosen_id)
            print(f"Last date of completion: {last_completion}\n")
        except TypeError:
            print("Last date of completion: Has not ever been completed yet.\n")

        step()
    except TypeError or ValueError:
        print("Invalid input")
        print("returning to Analytics Menu...")
        step()

def get_highest_current_streak():
    """Used in analytics_menu to print the highest current streak and its associated habit name
    If multiple habits have equal values, all of them will be printed out in order of habit_id"""
    print("highest current streak:\n")
    highest_streak = db.fetch_highest_current_streak()
    for item in highest_streak:
        print(f"[{item["habit_id"]}] {item["name"]}: currently at {item["streak_count"]} consecutive completions.")
    print("")
    step()

def get_highest_history_streak():
    """Used in analytics_menu to print the highest streak in history and its associated habit name
        If multiple habits have equal values, all of them will be printed out in order of habit_id"""
    print("Highest all time streak:\n")
    highest_history_streak = db.fetch_highest_history_streak()
    for item in highest_history_streak:
        name = db.get_name_for_id(item["habit_id"])
        print(f"[{item["habit_id"]}] {name}: all time record at {item["streak_count"]} consecutive completions.")
    print("")
    step()

def print_each_last_entry():
    print("List of last completion for each currently active habit:")
    active_habits_ids = db.fetch_active_ids()
    #print(active_habits_ids)
    #print(type(active_habits_ids))
    for habit_id in active_habits_ids:
        try:
            last_entry = db.get_last_entry(habit_id)
            name = db.get_name_for_id(habit_id)
            print(f"{name}: {last_entry}")
        except TypeError:
            name = db.get_name_for_id(habit_id)
            print(f"{name} has not ever been completed yet.")

def print_all_history_entries(chosen_id):
    """Used in analytics_menu to print all history entries for the habit with habit_id == passed in habit_id"""
    habit_name = db.get_name_for_id(chosen_id)
    habit_history_data = db.fetch_all_history_for_habit(chosen_id)
    print(f"Here are all history entries for the habit '{habit_name}':")
    for item in habit_history_data:
        if item["complete_status"] == 1:
            complete_status = "Completed"
        else:
            complete_status = "Incomplete"
        if item["streak_status"] == 1:
            streak_status = "Streak"
        else:
            streak_status = "no Streak"
        print(
            f"[{item["date"]}], {complete_status}, {streak_status}, "
            f"Number of consecutive completions: {item["streak_count"]}")
    step()


## functions for manage_menu

def save_habit_changes_to_db(current_habit_obj):
    """used to save changes from a habit instance to its corresponding habit and history table"""
    update_data = current_habit_obj.get_update_data()
    db.update_single_row(update_data)
    history_data = current_habit_obj.get_history_data()
    habit_id = current_habit_obj.habit_id
    current_day = hd.current_day
    existing_history_date = db.check_existing_history_date(habit_id, current_day)
    if existing_history_date == False:
        db.append_history(history_data)
    elif existing_history_date == True:
        db.update_history(history_data)
    else:
        print("Error writing to history table.")

def reset_habit(habit_id):
    """used in manage menu to reset habit instance and save the data to the database"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.reset()
    save_habit_changes_to_db(current_habit_obj)

def delete_restore_habit(habit_id):
    """used in manage menu to set habits active attribute to 0 and save to db"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.change_active()
    save_habit_changes_to_db(current_habit_obj)

def change_habit_name(habit_id, new_name):
    """used in edit habit menu to change habit name"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.change_name(new_name)
    save_habit_changes_to_db(current_habit_obj)

def change_habit_description(habit_id, new_desc):
    """used in edit habit menu to change habit description"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.change_desc(new_desc)
    save_habit_changes_to_db(current_habit_obj)

def change_habit_interval(habit_id, new_interval):
    """used in edit habit menu to change habit interval"""
    current_habit_obj = create_habit_obj(habit_id)
    current_habit_obj.change_interval(new_interval)
    save_habit_changes_to_db(current_habit_obj)

