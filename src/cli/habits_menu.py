from database import db

def habits_menu_choice():
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
    while True:
        choice = habits_menu_choice()
        if choice == 1:
            #function to choose which habit to complete
            #needs to print all active habits
            print("Which habit would you like to complete?")
            #then create an instance for said habit
            #etc.....should all that be called by cli? or main? check later
        else:
            print("Returning to main menu...")
            return_value = "BACK"
            return return_value
