from analytics import analytics as an
from database import db
from main_util.main_util import step
from cli import cli_util as cli



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
                        old_name = db.get_name_for_id(habit_id)
                        new_name = cli.new_name_input(old_name)
                        while True:
                            confirm = cli.confirm_new_name(old_name, new_name)
                            if confirm == "y":
                                an.change_habit_name(habit_id, new_name)
                                print(f"'{old_name}' has been renamed to '{new_name}'")
                                break
                            else:
                                print(f"Name change aborted. Name reset to '{old_name}'.")
                                break


                        #an.confirm_new_name(old_name, new_name)
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
                        name = db.get_name_for_id(habit_id)
                        old_desc = db.get_desc_for_id(habit_id)
                        new_desc = cli.new_desc_input(name)
                        while True:
                            confirm = cli.confirm_new_desc(name, new_desc)
                            if confirm == "y":
                                an.change_habit_description(habit_id, new_desc)
                                print(f"The description of '{name}' has been changed to '{new_desc}'")
                                break
                            else:
                                print(
                                    f"Description change aborted. Description of '{name}' has been reset to '{old_desc}'.")
                                break
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
                    name = db.get_name_for_id(habit_id)
                    new_interval = None
                    if 0 < habit_id <= max_habit_id:
                        while True:
                            old_interval = db.get_interval(habit_id)
                            change_type = cli.interval_change_type_choice()
                            if change_type == "1":
                                while True:
                                    interval_predefined_choice = cli.predefined_interval_choice()
                                    if interval_predefined_choice == "1":
                                        new_interval = 1
                                        break
                                    elif interval_predefined_choice == "2":
                                        new_interval = 7
                                        break
                                    else:
                                        print("Incorrect input. Please enter 1 or 2.")
                            if change_type == "2":
                                while True:
                                    interval_manual_choice = cli.manual_interval_input()
                                    try:
                                        if 1 <= interval_manual_choice <= 365:
                                            new_interval = interval_manual_choice
                                            break
                                        else:
                                            print("Incorrect input. Please enter a number between 1 and 365.")
                                    except ValueError:
                                        print("Incorrect input. Please enter a number between 1 and 365.")

                            if old_interval != new_interval and new_interval is not None:
                                while True:
                                    confirm = cli.confirm_interval_change(name, old_interval, new_interval)

                                    if confirm == "y":
                                        an.change_habit_interval(habit_id, new_interval)
                                        break
                                    elif confirm == "n":
                                        print(f"Interval of '{name}' remains at '{old_interval}' days.")
                                        break
                                    else:
                                        print("Unexpected input. Please only enter 'y' or 'n'.")

                            else:
                                print("New interval identical to old interval. Interval change aborted.")
                            break

                    else:
                        print("No habit such number found to change interval.")
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
