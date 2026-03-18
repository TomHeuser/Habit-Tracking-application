from main_util.main_util import step, return_to_main
from cli import edit_habit_menu as ehm
from analytics import analytics as an
from database import db

def manage_menu_choice():
    """Called when user input is needed to choose and option from manage sub menu"""
    while True:
        print("Manage habits menu:")
        try:
            choice = int(input("Choose option:\n"
              "[1] delete habit\n"
              "[2] restore habit\n"
              "[3] edit habit\n"
              "[4] reset habit (Will set streak and consecutive days to 0!)\n"
              "[5] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")


def manage_menu():
    """called when user wants to open manage sub menu from main menu"""
    while True:
        choice = manage_menu_choice()
        if choice == 1:
            print("Which habit would you like to delete? (Can be restored again later)")
            active_habits = db.fetch_active_names()
            if active_habits is not None:
                for item in active_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
            else:
                print("No habits to delete")
            try:
                habit_id = int(input("To choose a habit please enter its associated number above."))
                an.delete_restore_habit(habit_id)
            except ValueError or TypeError:
                print("Invalid option")

        elif choice == 2:
            print("Which habit would you like to restore?")
            inactive_habits = db.fetch_inactive_names()
            if inactive_habits is not None:
                for item in inactive_habits:
                    print(f"[{item["habit_id"]} {item["name"]}]")
            else:
                print("You currently have not habits to delete.")
            try:
                habit_id = int(input("To choose a habit please enter its associated number above."))
                an.delete_restore_habit(habit_id)
            except ValueError or TypeError:
                print("Invalid option")
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
        elif choice == 5:
            return return_to_main()