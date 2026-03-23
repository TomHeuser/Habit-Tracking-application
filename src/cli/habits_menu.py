from analytics import analytics as an
from main_util.main_util import return_to_main
from database import db as db
from cli import cli_util as cli


def habits_menu_choice():
    """Called when user input is needed to choose and option from habit sub menu"""
    while True:
        print("Habit Menu:\n"
              "\n")
        try:
            choice = int(input("What would you like to do?\n"
                               "[1] complete habit\n"
                               "[2] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")


def habits_menu():
    """called when user wants to open habits sub menu from main menu"""
    while True:
        choice = habits_menu_choice()
        if choice == 1:
            print("Choose a habit to complete from the following list:")
            print("Your currently active habits are:")
            an.get_list_of_active_habits()
            habit_id = int(input("To choose a habit please enter the associated number above.\n"))
            while True:
                name = db.get_name_for_id(habit_id)
                complete_status = db.get_complete_status_for_id(habit_id)
                if complete_status == 1:
                    confirm = cli.confirm_incomplete(name)
                    if confirm == "y":
                        print(f"'{name}' has been reset to incomplete.")
                        an.change_habit_obj_complete(habit_id)
                        break
                    elif confirm == "n":
                        print(f"Incompletion aborted. '{name}' remains complete.")
                        break
                    else:
                        print("Unexpected input. Please only enter 'y' or 'n'.")
                elif complete_status == 0:
                    confirm = cli.confirm_complete(name)
                    if confirm == "y":
                        print(f"'{name}' has been completed successfully!")
                        an.change_habit_obj_complete(habit_id)
                        break
                    elif confirm == "n":
                        print(f"Completion aborted. '{name}' remains incomplete.")
                        break
                    else:
                        print("Unexpected input. Please only enter 'y' or 'n'.")
                else:
                    print(f"Abnormality detected. '{name}' has automatically been set to incomplete.")
                    an.change_habit_obj_complete(habit_id)
                    break
        else:
            return return_to_main()


