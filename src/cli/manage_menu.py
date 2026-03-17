from main_util.main_util import step, return_to_main

def manage_menu_choice():
    while True:
        print("Manage habits menu:")
        try:
            choice = int(input("Choose option:\n"
              "[1] delete habit\n"
              "[2] restore habit\n"
              "[3] change habit interval\n"
              "[4] reset habit (Will set streak and consecutive days to 0!)\n"
              "[5] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")
            manage_menu_choice()

def manage_menu():
    while True:
        choice = manage_menu_choice()
        if choice == 1:
            print("Which habit would you like to delete? (Can be restored again later)")
            # function to set attribute to inactive using class object and methods etc
        elif choice == 2:
            print("Which habit would you like to restore?")
            # function to set attribute of inactive habit to active using class object and methods etc
        elif choice == 3:
            print("Which habit's interval would you like to change?")
            # function to set attribute of inactive habit to active using class object and methods etc
        elif choice == 4:
            print("Which habit would you like to reset?")
            # function to set streak related attributes of active habit to zero
        elif choice == 5:
            return return_to_main()