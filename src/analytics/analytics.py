from main_util.main_util import step
from database import db as db

def choose_interval():
    """used during creation of new Habit. Lets the user choose between the desired
    interval [1= daily, 2= weekly], (formatted in days, "daily" returns 1, "weekly" returns 7)"""
    while True:
        # userinput to choose between daily and weekly (eg:1 and 7)
        interval_input = input("Please choose the habits' interval:\n[1]daily\n[2]weekly\n")
        if interval_input == "1":
            return 1
        elif interval_input == "2":
            return 7
        else:
            print("Incorrect input. Please enter 1 or 2.")


def set_interval():
    """used during creation of new habit. Lets the user choose the desired number of days (1-365)"""
    while True:
        try:
            interval_input = int(input("Please enter the desired number of days [1 - 365] for the habits' interval:"))
            if 1 <= interval_input <= 365:
                return interval_input
            else:
                print("Incorrect input. Please enter a number between 1 and 365.")
        except ValueError:
            print("Incorrect input. Please enter a number between 1 and 365.")



## functions for analytics_menu.py

def get_list_of_active_habits():
    print("all active habits:")
    # implement functionality
    print("Your currently active habits are:")
    active_habits = db.fetch_active_names()
    for item in active_habits:
        print(item["habit_id"], item["name"])
    print("")
    # print(type(active_habits))
    step()

def get_list_of_all_habits():
    print("Current habits:")
    all_habits = db.fetch_names()
    for item in all_habits:
        print(f"[{item["habit_id"]}] {item["name"]}")
    print("")

def print_habit_details_of_selected_habit(chosen_id):
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
        print(f"Number of consecutive completions: {habit_details['streak_count']}\n"
              f"")
        step()
    except TypeError or ValueError:
        print("Invalid input")
        print("returning to Analytics Menu...")
        step()

def get_highest_current_streak():
    print("highest current streak:\n")
    highest_streak = db.fetch_highest_current_streak()
    for item in highest_streak:
        print(f"[{item["habit_id"]}] {item["name"]}: currently at {item["streak_count"]} consecutive completions.")
    print("")
    step()

def get_highest_history_streak():
    print("Highest all time streak:\n")
    highest_history_streak = db.fetch_highest_history_streak()
    for item in highest_history_streak:
        name = db.get_name_for_id(item["habit_id"])
        print(f"[{item["habit_id"]}] {name}: all time record at {item["streak_count"]} consecutive completions.")
    print("")
    step()

def print_all_history_entries(chosen_id):
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