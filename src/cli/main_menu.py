def submenu_choice():
    while True:

        try:
            choice = int(input("Please choose how to proceed:\n"
                               "[1] habits menu\n"
                               "[2] manage habits menu\n"
                               "[3] analytics menu\n"
                               "[4] close application"))
            return choice

        except ValueError:
            print("Incorrect input, please only enter 1,2,3 or 4.")

def redirect_submenu():
    choice = submenu_choice()
    if choice == 1:
        print("Opening habits menu.....")
        #call habit menu function
    elif choice == 2:
        print("Opening menu to manage habits.....")
        #call manage habits function
    elif choice == 3:
        print("Opening analytics menu.....")
        #call analytics menu function
    elif choice == 4:
        print("Thanks for using 'Unnecessary German Efficiency'\n"
              "Your application for over the top self improvement.\n"
              "We're here to help you become the most automated and indifferent version of yourself!\n")
        # implement closing functionality AND a little stop for the user to confirm
        print("Closing application.....")

def main_menu():
    redirect_submenu()