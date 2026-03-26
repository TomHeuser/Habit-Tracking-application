from database import db_setup as db_setup
from datetime import date
from main_util import handle_dates as hd
from cli import cli_util as cli
from database import db as db
from main_util.main_util import step
from analytics.analytics import get_list_of_all_habits
from math import floor


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
    #print(f"test runs")
    if current_week == 0:
        current_week = date.today().isocalendar().year * 52 + date.today().isocalendar().week
    #print(f"current week = {current_week}")
    try:
        habit_ids = db.get_weekly_id_list()
    except TypeError:
        print("No weekly habits which would need to be reset were found.")
    #print(habit_ids)
    try:
        #print("For testing purposes to check print mock, disable later!")
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
    except:
        print("No weekly habits which would need to be reset were found.")

def handle_daily_reset(current_day = 0):
    """run on startup to check daily active habits and set unachieved or reset if necessary."""
    if current_day == 0:
        current_day = date.today()
    try:
        habit_ids = db.get_daily_id_list()
        #print(habit_ids)
    except TypeError:
        print("No daily habits which would need to be reset were found.")
    try:
        for habit_id in habit_ids:
            name = db.get_name_for_id(habit_id)
            #print(name)
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
            #print("for loop working.....")
            #get created on and calc intervals rounded down to creation
            name = db.get_name_for_id(habit_id)
            last_complete = db.get_last_entry(habit_id)
            last_iso_date = date.fromisoformat(last_complete)
            #print(f"last_iso_date {last_iso_date}")
            #print("name + date gen. working.....")
            interval = db.get_interval(habit_id)
            #print("interval gen. working.....")
            created_on = db.get_creation_date(habit_id)
            created_on_date = date.fromisoformat(created_on)
            #print("creation date gen. working.....")
            #calc current interval
            current_days_difference = (current_day - created_on_date).days

            #print(f"current_days_difference {current_days_difference}")
            current_interval_number = current_days_difference / interval
            #print(f"current_interval_number {current_interval_number}")
            current_interval_number_rounded = floor(current_interval_number)
            #print("Current interval number calc working.....")
            #print(f"current_interval_number_rounded {current_interval_number_rounded}")
            # calc last interval
            last_days_difference = (last_iso_date - created_on_date).days
            #print(f"last_days_difference {last_days_difference}")
            last_interval_number = last_days_difference / interval
            last_interval_number_rounded = floor(last_interval_number)
            #print("last interval number calc working.....")
            #print(f"last_interval_number{last_interval_number}")
            #print(f"last_interval_number_rounded {last_interval_number_rounded}")
            # calc difference between both interval numbers
            interval_difference = current_interval_number_rounded - last_interval_number_rounded
            #print(f"interval_difference {interval_difference}")

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
    except TypeError:
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

##process of creating new habit
## process of creating a new name
def get_name():
    """used to generate the name of a new habit during habit creation"""
    while True:
        new_habit_name = cli.get_new_name_input()
        new_name_confirm = cli.get_new_name_confirm_input(new_habit_name)
        if new_name_confirm == "y":
            print(f"Ok, your new habits' name is '{new_habit_name}'")
            return new_habit_name
        elif new_name_confirm == "n":
            print("Ok, lets pick another name then.")
        else:
            print("Invalid input. Please only enter y or n to confirm. Restarting naming process now:")

def get_desc():
    """used to generate the description of a new habit during habit creation"""
    while True:
        new_habit_desc = cli.get_new_desc_input()
        new_desc_confirm = cli.get_new_desc_confirm_input(new_habit_desc)
        if new_desc_confirm == "y":
            print(f"Ok, your new habits' description is '{new_habit_desc}'.")
            return new_habit_desc
        elif new_desc_confirm == "n":
            print("Ok, lets pick another description then.")
        else:
            print("Invalid input. Please only enter y or n to confirm. Restarting description process now:")

def interval_confirm(new_interval):
    while True:
        interval_confirm = cli.get_interval_approach_confirm(new_interval)
        if interval_confirm == "y":
            return True

        else:
            return False

def set_predefined_interval():
    while True:
        predefined_interval = cli.predefined_interval_choice()
        if predefined_interval == "1":
            new_interval = 1
            return new_interval
        elif predefined_interval == "2":
            new_interval = 7
            return new_interval
        else:
            print("Invalid input. Please enter either 1 or 2.")

def set_manual_interval():
    while True:
        try:
            manual_interval = cli.manual_interval_input()
            if 1 <= manual_interval <= 365:
                return manual_interval
            else:
                print("Invalid input. Please enter a number between 1 and 365.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 365.")

def get_interval():
    while True:
        interval_approach = cli.get_interval_approach_input()
        if interval_approach == "1":
            new_interval = set_predefined_interval()
            confirm = interval_confirm(new_interval)
            if confirm == True:
                interval = new_interval
                return interval
            else:
                print("Ok, lets start anew with then selection of your new interval.")
        elif interval_approach == "2":
            new_interval = set_manual_interval()
            confirm = interval_confirm(new_interval)
            if confirm == True:
                interval = new_interval
                return interval
            else:
                print("Ok, lets start anew with then selection of your new interval.")
        else:
            print("Invalid input. Please enter either 1 or 2.")

def create_new_habit(current_date):
    print("To create a new habit, we need some information first.")
    ##auto assign active, complete and created_on
    active = 1
    complete_status = 0
    streak_status = 0
    streak_count = 0
    created_on = current_date
    ## get name
    name = get_name()
    ## get description
    desc = get_desc()
    ##get interval
    interval = get_interval()
    new_habit_data = {"name": name,"desc": desc, "active": active, "complete_status": complete_status,"interval": interval,
                    "created_on": created_on, "streak_status": streak_status, "streak_count": streak_count}
    return new_habit_data

def create_habit(current_date = 0):
    """used in manage menu to create new habit"""
    current_day = hd.current_day
    new_habit_data = create_new_habit(current_day)
    db.append_single_row(new_habit_data)