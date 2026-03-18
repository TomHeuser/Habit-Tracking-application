## contains user input commands necessary for processes outside of menu loops to work correctly

## input functions for main_menu loop

def submenu_choice():
    """generates and returns user input to choose main menu option"""
    while True:
        try:
            choice = int(input("Please choose how to proceed:\n"
                                "[1] habits menu\n"
                                "[2] manage habits menu\n"
                                "[3] analytics menu\n"
                                "[4] close application\n"))
            return choice

        except ValueError:
            print("Incorrect input, please only enter 1,2,3 or 4.")

## used in class tree
# change name method
def new_name_input(old_name):
    """generates and returns user input to get new value for name"""
    new_name = input(f"Please enter a new name for '{old_name}':")
    return new_name

def confirm_new_name(old_name, new_name):
    """generates and returns user input to confirm name change in habit method"""
    confirm = input(f"Would you like to rename '{old_name}' to '{new_name}'? (y/n)")
    return confirm
# change desc method
def new_desc_input(name):
    """generates and returns user input to get new value for description"""
    new_desc = input(f"Please enter a new description for '{name}':")
    return new_desc
def confirm_new_desc(name, new_desc):
    """generates and returns  user input to confirm description change in habit method"""
    confirm = input(f"Would you like to change the description of '{name}' to '{new_desc}'? (y/n)")
    return confirm
# change active method
def confirm_delete(name):
    """generates and returns user input to confirm active change to 0 (inactive) in habit method"""
    confirm = input(f"Are you sure that you'd like to delete '{name}'? (y/n) [Not lost permanently. Can be restored]")
    return confirm
def confirm_restore(name):
    """generates and returns user input to confirm active change to 1 (active) in habit method"""
    confirm = input(f"Would you like restore '{name}'? (y/n)")
    return confirm
#change complete method
def confirm_incomplete(name):
    """generates and returns user input to confirm change of complete to 0 (incomplete) in habit method"""
    confirm = input(f"Would you like to reset '{name}' to incomplete? (y/n)")
    return confirm
def confirm_complete(name):
    """generates and returns user input to confirm change of complete to 1 (complete) in habit method"""
    confirm = input(f"Would you like to complete '{name}' for the current interval? (y/n)")
    return confirm
#change interval method
def predefined_interval_choice():
    """used to generate and return user input to choose predefined interval (daily or weekly)"""
    interval_input = input("Please choose the habits' interval:\n[1]daily\n[2]weekly\n")
    return interval_input
def manual_interval_input():
    """used to generate and return user input to choose manual interval (1-365 days)"""
    try:
        interval_input = int(input("Please enter the desired number of days [1 - 365] for the habits' interval:"))
        return interval_input
    except ValueError or TypeError:
        return 0
def interval_change_type_choice():
    """used to generate and return user input to choose interval change type (predefined or manual)"""
    change_type = input(f"Would you like to choose a predefined interval or create a individual interval?\n"
                        f"[1] predefined or [2] individual")
    return change_type
def confirm_interval_change(name, old_interval, new_interval):
    """used to generate and return user input to confirm interval change"""
    confirm = input(f"Would you like to change the current interval of '{name}' from"
          f" '{old_interval}' days to '{new_interval}' days?\n"
          f"IMPORTANT: This will also reset its streak!\n"
          f"(y/n)")
    return confirm