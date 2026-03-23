from main_util.main_util import step, return_to_main
from main_util.handle_dates import current_day
from cli import edit_habit_menu as ehm
from cli import cli_util as cli
from analytics import analytics as an
from analytics import functions_util as func
from database import db

def manage_menu_choice():
    """Called when user input is needed to choose and option from manage sub menu"""
    while True:
        print("Manage habits menu:")
        try:
            choice = int(input("Choose option:\n"
              "[1] create new habit\n"
              "[2] delete habit\n"
              "[3] edit habit\n"
              "[4] reset habit (Will set streak and consecutive days to 0!)\n"
              "[5] restore habit\n"
              "[6] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")


def manage_menu():
    """called when user wants to open manage sub menu from main menu"""
    while True:
        choice = manage_menu_choice()
        if choice == 2:
            print("Which habit would you like to delete? (Can be restored again later)")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
            else:
                print("No habits to delete")
            try:
                habit_id = int(input("To choose a habit please enter its associated number above."))
                while True:
                    name = db.get_name_for_id(habit_id)
                    active = db.get_active_for_id(habit_id)
                    if active == 1:
                        confirm = cli.confirm_delete(name)
                        if confirm == "y":
                            print(f"'{name}' has been deleted.")
                            an.delete_restore_habit(habit_id)
                            break
                        elif confirm == "n":
                            print(f"'{name}' has NOT been deleted.")
                            break
                        else:
                            print("Unexpected input. Please only enter 'y' or 'n'.")

                    elif active == 0:
                        print(f"'{name}' has already been deleted before. To restore {name}, please choose the 'restore habit' option above.")
                        break

                    else:
                        print("Habit status abnormality detected. Habit was automatically restored to 'active'.")
                        an.delete_restore_habit(habit_id)
                        break

            except ValueError or TypeError:
                print("Invalid option")


        elif choice == 5:
            inactive_habits = db.fetch_inactive_names()
            #print(inactive_habits)
            if inactive_habits != []:
                print("Which habit would you like to restore?")
                for item in inactive_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
                try:
                    habit_id = int(input("To choose a habit please enter its associated number above."))
                    while True:
                        name = db.get_name_for_id(habit_id)
                        active = db.get_active_for_id(habit_id)
                        if active == 1:
                            print(f"{name} is already active and therefore cant be 'restored'.")

                        elif active == 0:
                            confirm = cli.confirm_restore(name)
                            if confirm == "y":
                                an.delete_restore_habit(habit_id)
                                print(f"'{name}' has been restored.")
                                break
                            elif confirm == "n":
                                print(f"The habit '{name}' was not restored.")
                                break
                            else:
                                print("Unexpected input. Please only enter 'y' or 'n'.")

                        else:
                            print("Habit status abnormality detected. Habit was automatically restored to 'active'.")
                            an.delete_restore_habit(habit_id)
                            break

                except ValueError or TypeError:
                    print("Invalid option")
            else:
                print("You currently have not habits to restore.")
        elif choice == 3:
            ehm.edit_habit_menu()
        elif choice == 4:
            print("Which habit would you like to reset?")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
            else:
                print("You currently have not habits to reset.")
            try:
                habit_id = int(input("To choose a habit please enter its associated number above."))
                max_habit_id = db.get_max_id()
                if 0 < habit_id <= max_habit_id:
                    an.reset_habit(habit_id)
                else:
                    print("Can not reset non existent habit.\n"
                          "Returning to Manage Menu....")
                    step()
            except ValueError or TypeError:
                print("Invalid option")
        elif choice == 1:
            func.create_habit(current_day)
        elif choice == 6:
            return return_to_main()