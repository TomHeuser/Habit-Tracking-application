from datetime import date
from analytics import analytics as an
from database import db
from main_util.main_util import step


def attribute_choice():
    """Called when user input is needed to choose and option from change habit sub-sub menu"""
    while True:
        print("What would you like to change?")
        try:
            choice = int(input("Choose option:\n"
                               "[1] change name\n"
                               "[2] change description\n"
                               "[3] change interval\n"
                               "[4] return to manage habit menu\n"))
            return choice
        except ValueError:
            print("Invalid option")


def edit_habit_menu():
    """Called when user chooses the edit habit option from manage menu"""
    while True:
        print("Currently changeable habits:")
        active_habits = db.fetch_all_habit_rows()
        for item in active_habits:
            print(f"[{item["habit_id"]}] {item["name"]}, Description: {item["desc"]}, Interval in days: {item["interval"]}")
        print("")
        attribute = attribute_choice()
        if attribute == 1:
            print("Which habit's name would you like to change?")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
                try:
                    habit_id = int(input("To choose a habit please enter its associated number above."))
                    max_habit_id = db.get_max_id()
                    if 0 < habit_id <= max_habit_id:
                        current_habit_obj = an.create_habit_obj(habit_id)
                        current_habit_obj.change_name()
                        update_data = current_habit_obj.get_update_data()
                        db.update_single_row(update_data)
                        history_data = current_habit_obj.get_history_data()
                        habit_id = current_habit_obj.habit_id
                        today = date.today()
                        iso_today = today.isoformat()
                        existing_history_date = db.check_existing_history_date(habit_id, iso_today)
                        if existing_history_date == False:
                            db.append_history(history_data)
                        elif existing_history_date == True:
                            db.update_history(history_data)
                        else:
                            print("Error writing to history table.")
                    else:
                        print("No habit to change name found.")
                except ValueError or TypeError:
                    print("Invalid option")
            else:
                print("No habit to change name found.")
        elif attribute == 2:
            print("Which habit's description would you like to change?")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
                try:
                    habit_id = int(input("To choose a habit please enter its associated number above."))
                    max_habit_id = db.get_max_id()
                    if 0 < habit_id <= max_habit_id:
                        current_habit_obj = an.create_habit_obj(habit_id)
                        current_habit_obj.change_desc()
                        update_data = current_habit_obj.get_update_data()
                        db.update_single_row(update_data)
                        history_data = current_habit_obj.get_history_data()
                        habit_id = current_habit_obj.habit_id
                        today = date.today()
                        iso_today = today.isoformat()
                        existing_history_date = db.check_existing_history_date(habit_id, iso_today)
                        if existing_history_date == False:
                            db.append_history(history_data)
                        elif existing_history_date == True:
                            db.update_history(history_data)
                        else:
                            print("Error writing to history table.")
                    else:
                        print("No habit to change description found.")
                except ValueError or TypeError:
                    print("Invalid option")
            else:
                print("No habit to change description found.")
        elif attribute == 3:
            print("Which habit's interval would you like to change?")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
                try:

                    habit_id = int(input("To choose a habit please enter its associated number above."))
                    max_habit_id = db.get_max_id()
                    if 0 < habit_id <= max_habit_id:
                        current_habit_obj = an.create_habit_obj(habit_id)
                        current_habit_obj.change_interval()
                        update_data = current_habit_obj.get_update_data()
                        db.update_single_row(update_data)
                        history_data = current_habit_obj.get_history_data()
                        habit_id = current_habit_obj.habit_id
                        today = date.today()
                        iso_today = today.isoformat()
                        existing_history_date = db.check_existing_history_date(habit_id, iso_today)
                        if existing_history_date == False:
                            db.append_history(history_data)
                        elif existing_history_date == True:
                            db.update_history(history_data)
                        else:
                            print("Error writing to history table.")
                    else:
                        print("No habit to change interval found.")
                except ValueError or TypeError:
                    print("Invalid option")
            else:
                print("No habit to change interval found.")
        elif attribute == 4:
            print("Returning to manage habits menu.....")
        else:
            print("Invalid option")
            print("Returning to manage habits menu.....")
        step()
        break
