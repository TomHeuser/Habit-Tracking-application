def analytics_choice():
    while True:
        print("Analytics menu:\n")
        try:
            choice = int(input("Choose option:\n"
              "[1] get list of active habits\n"
              "[2] get habit details\n"
              "[3] get highest current streak\n"
              "[4] get highest all time streak\n"
              "[5] return to main menu\n"))
            return choice
        except ValueError:
            print("Invalid option")

def analytics_menu():
    while True:
        choice = analytics_choice()
        if choice == 1:
            print("all active habits:")
            #implement functionality
        elif choice == 2:
            print("habit details:")
            #implementet functionality
        elif choice == 3:
            print("highest current streak:")
            #implement functionality
        elif choice == 4:
            print("highest all time streak:")
            #implement functionality
        elif choice == 5:
            print("Returning to main menu....")
            return_value = "BACK"
            return return_value
        else:
            print("Invalid option")



