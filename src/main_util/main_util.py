from datetime import date
today = date.today()
iso_today = today.isoformat()


## process of creating a new name
def get_name():
    """used to generate the name of a new habit during habit creation"""
    while True:
        new_habit_name = input("Please enter the name of the habit: ")
        new_name_confirm = input(f"Do you want to name your new habit to be: '{new_habit_name}'? \n"
                                 f"[y] for yes or [n] for no'")
        if new_name_confirm == "y":
            print(f"Ok, your new habits' name is '{new_habit_name}'")
            return new_habit_name
        elif new_name_confirm == "n":
            print("Ok, lets pick another name then.")
        else:
            print("Invalid input. Please only enter y or n to confirm. Restarting naming process now:")

def get_desc():
    """used to generate the description of a new habit during habit creation"""
    while True:
        new_habit_desc = input(f"Please enter a description for the new habit: ")
        new_desc_confirm = input(f"Do you want the description of your new habit to be:\n"
                                 f"'{new_habit_desc}'? \n"
                                 f"[y] for yes or [n] for no'")
        if new_desc_confirm == "y":
            print(f"Ok, your new habits' description is '{new_habit_desc}'.")
            return new_habit_desc
        elif new_desc_confirm == "n":
            print("Ok, lets pick another description then.")
        else:
            print("Invalid input. Please only enter y or n to confirm. Restarting description process now:")

def get_interval_approach():

    interval_approach = input(f"Do you want to choose a predefined interval or would you like to set the interval manually?\n"
                                  f"[1] for predefined\n"
                                  f"[2] to set in manually")
    return interval_approach


def interval_confirm(new_interval):
    while True:
        interval_confirm = input(f"Do you want the new interval to be {new_interval} days?\n"
                                 f"[y] for yes or [n] for no")
        if interval_confirm == "y":
            return True

        else:
            return False

def set_predefined_interval():
    while True:
        predefined_interval = input("You can choose between daily and weekly \n"
                                "[1] daily"
                                "[2] weekly")
        if predefined_interval == "1":
            new_interval = 1
            return new_interval
        elif predefined_interval == "2":
            new_interval = 7
            return new_interval
        else:
            print("Invalid input. Please enter either 1 or 2.")

def set_manual_interval():
    while True:
        try:
            manual_interval = int(input("Please enter desired number of days [1-365]:"))
            if 1 <= manual_interval <= 365:
                return manual_interval
            else:
                print("Invalid input. Please enter a number between 1 and 365.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 365.")

def get_interval():
    while True:
        interval_approach = get_interval_approach()
        if interval_approach == "1":
            new_interval = set_predefined_interval()
            confirm = interval_confirm(new_interval)
            if confirm == True:
                interval = new_interval
                return interval
            else:
                print("Ok, lets start anew with then selection of your new interval.")
        elif interval_approach == "2":
            new_interval = set_manual_interval()
            confirm = interval_confirm(new_interval)
            if confirm == True:
                interval = new_interval
                return interval
            else:
                print("Ok, lets start anew with then selection of your new interval.")
        else:
            print("Invalid input. Please enter either 1 or 2.")

def create_new_habit():
    print("To create a new habit, we need some information first.")
    ##auto assign active, complete and created_on
    active = 1
    complete_status = 0
    created_on = iso_today
    ## get name
    name = get_name()
    ## get description
    desc = get_desc()
    ##get interval
    interval = get_interval()
    new_habit_data = {"name": name,"desc": desc, "active": active,
                        "complete_status": complete_status, "interval": interval,
                        "created_on": created_on}
    return new_habit_data

    print("You created the following habit:")
    print(f"Habit name: {name}")
    print(f"Habit description: {desc}")
    print(f"active: {active}")
    print(f"interval: {interval}")
    print(f"complete_status: {complete_status}")
    print(f"Creation date: {created_on}")




