def analytics_choice():
    print("Analytics menu:")
    try:
        choice = int(input("Choose option:\n"
          "[1] get list of active habits\n"
          "[2] get habit details\n"
          "[3] get highest current streak\n"
          "[4] get highest all time streak\n"
          "[5] return to main menu"))
        return choice
    except ValueError:
        print("Invalid option")
        analytics_choice()

def analytics_menu():
    choice = analytics_choice()
    if choice == 1:
        print("all active habits:")
        #implement functionality
        analytics_menu()
    elif choice == 2:
        print("habit details:")
        #implementet functionality
        analytics_menu()
    elif choice == 3:
        print("highest current streak:")
        #implement functionality
        analytics_menu()
    elif choice == 4:
        print("highest all time streak:")
        #implement functionality
        analytics_menu()
    elif choice == 5:
        print("Returning to main menu....")
        #implement functionality
    else:
        print("Invalid option")
        analytics_menu()



