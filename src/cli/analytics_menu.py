from analytics import analytics as an
from database import db as db
from main_util.main_util import step, return_to_main


def analytics_choice():
    """Called when user input is needed to choose and option from analytics sub menu"""
    while True:
        print("Analytics menu:\n")
        try:
            choice = int(input("Choose option:\n"
              "[1] get list of active habits\n"
              "[2] get habit details of selected habit\n"
              "[3] get highest current streak\n"
              "[4] get highest all time streak\n"
              "[5] get all log entries for given habit\n"
              "[6] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")

def analytics_menu():
    """called when user wants to open analytics sub menu from main menu"""
    while True:
        choice = analytics_choice()
        if choice == 1:
            an.get_list_of_active_habits()
            step()
        elif choice == 2:
            an.get_list_of_all_habits()
            while True:
                try:
                    chosen_id = int(input("Please enter one the above numbers of a habit to see it's details.\n"
                                      "Please only enter one number at a time.\n"
                                      ""))
                    an.print_habit_details_of_selected_habit(chosen_id)
                    break
                except ValueError:
                    print("Invalid input")
                    print("Returning to Analytics menu....\n")
                    break
        elif choice == 3:
            an.get_highest_current_streak()
        elif choice == 4:
            an.get_highest_history_streak()
        elif choice == 5:
            while True:
                print("To choose and get all entries for a habit from the following list:")
                an.get_list_of_all_habits()
                try:
                    chosen_id = input("Please enter one of the above numbers for its associated habit:\n")
                    an.print_habit_details_of_selected_habit(chosen_id)
                except ValueError or TypeError:
                    print("Invalid input")
                break
        elif choice == 6:
            return return_to_main()
        else:
            print("Invalid option")



