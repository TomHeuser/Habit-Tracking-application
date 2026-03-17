from database import db
from analytics import analytics as an
from main_util.main_util import step, return_to_main

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
            an.get_list_of_active_habits()
            habit_id = int(input("To choose a habit please enter the associated number above.\n"))
            an.change_habit_obj_complete(habit_id)

        else:
            return return_to_main()
