from database import db_setup as db_setup
from datetime import date
from database import db as db
from main_util.main_util import step


#things to run on startup
def welcome_message():
    print("Welcome to 'Unnecessary German Efficiency'! \n"
              "Your application for over the top self improvement.\n")

def date_message(current_date = 0):
    if current_date == 0:
        current_date = date.today()
    print(f"It is the {current_date}.\n"
          f"Since your last startup, the following things have happened:\n")

def startup_complete_message():
    print("How may we help you become the most automated and indifferent version of yourself today?\n")

def handle_weekly_reset(current_week = 0):
    # gets actual current week if no other week is being passed in
    if current_week == 0:
        current_week = date.today().isocalendar().year * 52 + date.today().isocalendar().week
    #print(f"current week = {current_week}")
    habit_ids = db.get_weekly_id_list()
    #print(habit_ids)
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

def handle_daily_reset(current_day = 0):
    if current_day == 0:
        current_day = date.today()
    #print(current_day)
    habit_ids = db.get_daily_id_list()
    #print(habit_ids)
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

def startup(current_date = 0, current_week = 0):
    db_setup.database_startup()
    welcome_message()
    step()
    date_message(current_date)
    handle_daily_reset(current_date)
    handle_weekly_reset(current_week)
    step()
    startup_complete_message()
