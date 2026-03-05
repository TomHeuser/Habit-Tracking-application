def choose_interval():
    """used during creation of new Habit. Lets the user choose between the desired
    interval [1= daily, 2= weekly], (formatted in days, "daily" returns 1, "weekly" returns 7)"""
    while True:
        # userinput to choose between daily and weekly (eg:1 and 7)
        interval_input = input("Please choose the habits' interval:\n[1]daily\n[2]weekly\n")
        if interval_input == "1":
            return 1
        elif interval_input == "2":
            return 7
        else:
            print("Incorrect input. Please enter 1 or 2.")


def set_interval():
    """used during creation of new habit. Lets the user choose the desired number of days (1-365)"""
    while True:
        try:
            interval_input = int(input("Please enter the desired number of days [1 - 365] for the habits' interval:"))
            if 1 <= interval_input <= 365:
                return interval_input
            else:
                print("Incorrect input. Please enter a number between 1 and 365.")
        except ValueError:
            print("Incorrect input. Please enter a number between 1 and 365.")