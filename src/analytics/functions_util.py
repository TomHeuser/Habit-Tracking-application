from database import db_setup as db_setup
from datetime import date
from database import db as db
from main_util.main_util import step
from analytics.analytics import get_list_of_all_habits


#things to run on startup
def welcome_message():
    print("Welcome to 'Unnecessary German Efficiency'! \n"
          "Your application for over the top self improvement.\n")

def date_message(current_date = 0):
    if current_date == 0:
        current_date = date.today()
    print(f"It is the {current_date} today.\n"
          f"Since your last startup, the following things have happened:\n")

def first_startup_message(current_date = 0):
    """Called during startup if first startup is detected"""
    if current_date == 0:
        current_date = date.today()
    print("This application will help you track and improve your habits, to become your better self!\n"
          "However, to ensure that everybody becomes the same identical better self,\n"
          "this application comes with 5 predefined habits.\n"
          "\n"
          "To complete a habit, access the 'habit menu',\n"
          "To delete, create or change habits, you can access the 'manage habits menu',\n"
          "and to analyze you existing habits and behaviour, please access the 'analytics menu'\n"
          "\n"
          "Creating your very own standardised personal predefined habits....")
    step()
    get_list_of_all_habits()
    print(f"It is the {current_date} today.\n")



def startup_complete_message():
    print("How may we help you today at getting closer to the most automated and indifferent version of yourself?\n")

def handle_weekly_reset(current_week = 0):
    """run on startup to check weekly active habits and set unachieved or reset if necessary."""
    # gets actual current week if no other week is being passed in
    if current_week == 0:
        current_week = date.today().isocalendar().year * 52 + date.today().isocalendar().week
    #print(f"current week = {current_week}")
    try:
        habit_ids = db.get_weekly_id_list()
    except TypeError:
        print("No weekly habits which would need to be reset were found.")
    #print(habit_ids)
    try:
        for habit_id in habit_ids:
            name = db.get_name_for_id(habit_id)
            #print(habit_id)
            last_complete = db.get_last_entry(habit_id)
            last_iso_date = date.fromisoformat(last_complete)
            #print(last_complete)
            last_complete_week = last_iso_date.isocalendar().year * 52 + last_iso_date.isocalendar().week
            #print(last_complete_week)
            week_difference = current_week - last_complete_week
            if week_difference == 0:
                print(f"{name} has not left it's interval since your last completion.\n")
            elif week_difference == 1:
                print(f"{name} entered a new interval and was set 'incomplete'\n")
                db.startup_habit_incomplete(habit_id)
            elif week_difference > 1:
                print(f"{name} has not been completed in the last interval.\n"
                      f"{name} has been set to 'incomplete'.\n"
                      f"Its streak and the number consecutive completions have been reset to 0.")
                db.startup_habit_reset(habit_id)
    except TypeError:
        print("No weekly habits which would need to be reset were found.")

def handle_daily_reset(current_day = 0):
    """run on startup to check daily active habits and set unachieved or reset if necessary."""
    if current_day == 0:
        current_day = date.today()
    try:
        habit_ids = db.get_daily_id_list()
    except TypeError:
        print("No daily habits which would need to be reset were found.")
    try:
        for habit_id in habit_ids:
            name = db.get_name_for_id(habit_id)
            last_complete = db.get_last_entry(habit_id)
            #print(last_complete)
            last_iso_date = date.fromisoformat(last_complete)
            #print(last_iso_date)
            day_difference = (current_day - last_iso_date).days
            #print(day_difference)
            if day_difference == 0:
                print(f"{name} has not left it's interval since your last completion.\n")
            elif day_difference == 1:
                print(f"{name} entered a new interval and was set 'incomplete'\n")
                db.startup_habit_incomplete(habit_id)
            elif day_difference > 1:
                print(f"{name} has not been completed in the last interval.\n"
                      f"{name} has been set to 'incomplete'.\n"
                      f"Its streak and the number consecutive completions have been reset to 0.\n")
                db.startup_habit_reset(habit_id)
    except TypeError:
        print("No weekly habits which would need to be reset were found.")

def handle_manual_reset(current_day = 0):
    """run on startup to check manually set active habits and set unachieved or reset if necessary."""
    if current_day == 0:
        current_day = date.today()
    try:
        habit_ids = db.get_manual_id_list()
    except TypeError:
        print("No habits with manually set intervals which would need to be reset were found.")
    try:
        for habit_id in habit_ids:
            print("for loop working.....")
            #get created on and calc intervals rounded down to creation
            name = db.get_name_for_id(habit_id)
            last_complete = db.get_last_entry(habit_id)
            last_iso_date = date.fromisoformat(last_complete)
            print(last_iso_date)
            print("name + date gen. working.....")
            interval = db.get_interval(habit_id)
            print("interval gen. working.....")
            created_on = db.get_creation_date(habit_id)
            created_on_date = date.fromisoformat(created_on)
            print("creation date gen. working.....")
            #calc current interval
            current_days_difference = (current_day - created_on_date).days
            current_interval_number = current_days_difference / interval
            print(current_interval_number)
            current_interval_number_rounded = round(current_interval_number, 0)
            print("Current interval number calc working.....")
            print(current_interval_number_rounded)
            # calc last interval
            last_days_difference = (last_iso_date - created_on_date).days
            print(last_days_difference)
            last_interval_number = last_days_difference / interval
            last_interval_number_rounded = round(last_interval_number, 0)
            print("last interval number calc working.....")
            print(last_interval_number_rounded)
            # calc difference between both interval numbers
            interval_difference = last_interval_number_rounded - current_interval_number_rounded

            if interval_difference == 0:
                print(f"{name} has not left it's interval since your last completion.\n")
            elif interval_difference == 1:
                print(f"{name} entered a new interval and was set 'incomplete'\n")
                db.startup_habit_incomplete(habit_id)
            elif interval_difference > 1:
                print(f"{name} has not been completed in the last interval.\n"
                      f"{name} has been set to 'incomplete'.\n"
                      f"Its streak and the number consecutive completions have been reset to 0.\n")
                db.startup_habit_reset(habit_id)
    except ValueError:
        print("No habits with manually set intervals which would need to be reset were found.")

def startup(current_date = 0, current_week = 0):
    first_startup = db_setup.database_startup()
    if first_startup == False:
        welcome_message()
        step()
        date_message(current_date)
        handle_daily_reset(current_date)
        handle_weekly_reset(current_week)
        handle_manual_reset(current_date)
    elif first_startup == True:
        welcome_message()
        first_startup_message(current_date)
    step()
    startup_complete_message()
