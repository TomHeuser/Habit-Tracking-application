##Habit class tree
from datetime import date

##lvl1: Habit superclass
class Habit:
    def __init__(self, habit_id, name, desc, active, complete_status, created_on):
        """Creates a new Habit object"""
        self.name = name
        self.habit_id = habit_id
        # user input to add description (str)
        self.desc = desc
        self.complete_status = complete_status
        self.active = active
        self.created_on = created_on

    ##experimental
    def get_update_data(self):
        """saves the current habit data to the database"""
        update_data = {"habit_id": {self.habit_id}, "name": {self.name},"desc": {self.desc}, "active": {self.active},
                        "complete_status": {self.complete_status},
                        "created_on": {self.created_on}}
        return update_data
        #print(update_data)

    @classmethod
    def from_db(cls, row):
        """takes the contents from a table row and then returns the values necessary for __init__ to create a new Habit object"""
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"],
                   complete_status=row["complete_status"], created_on=row["created_on"])

    def __repr__(self):
        """manages how attributes are returned"""
        return f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, created_on={self.created_on})"

    ## methods to change existing habits

    ## needs changing
    def change_name(self):
        """used to change the name attribute of an existing habit object, then applies these changes to database entry"""
        new_name = input(f"Please enter a new name for '{self.name}':")
        old_name = self.name
        while True:
            confirm = input(f"Would you like to rename '{self.name}' to '{new_name}'? (y/n)")
            if confirm == "y":
                self.name = new_name
                # save to db
                print(f"'{old_name}' has been renamed to '{self.name}'")
                break
            else:
                print(f"Name change aborted. Name reset to '{self.name}'.")
                break

    #needs changing
    def change_desc(self):
        """used to change the desc attribute of an existing habit object, then applies these changes to database entry"""
        new_desc = input(f"Please enter a new description for '{self.name}':")
        while True:
            confirm = input(f"Would you like to change the description of '{self.name}' to '{new_desc}'? (y/n)")
            if confirm == "y":
                self.desc = new_desc
                #safe to db
                print(f"The description of '{self.name}' has been changed to '{self.desc}'")
                break
            else:
                print(f"Description change aborted. Description of '{self.name}' has been reset to '{self.desc}'.")
                break

    ## needs changes
    def change_active(self):
        """used to set a habit to active or inactive. Changes the active attribute of an existing habit object,
        between 0 (False, inactive) and 1 (True, active), then applies these changes to database entry"""
        while True:
            if self.active == 1:
                confirm = input(f"Are you sure that you'd like to delete '{self.name}'? (y/n) [Not lost permanently. Can be restored]")
                if confirm == "y":
                    self.active = 0
                    print(f"'{self.name}' has been deleted.")
                    # implement change to habit data
                    # implement saving to habit
                    break
                elif confirm == "n":
                    print(f"'{self.name}' has NOT been deleted.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            elif self.active == 0:
                confirm = input(f"Would you like restore '{self.name}'? (y/n)")
                if confirm == "y":
                    self.active= 1
                    print(f"'{self.name}' has been restored.")
                    # implement change to habit data
                    # implement saving to habit
                    break
                elif confirm == "n":
                    print(f"The habit '{self.name}' was not restored.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            else:
                print("Habit status abnormality detected. Habit was automatically restored to 'active'.")
                self.complete_status = 1
                break


    ## needs changes
    def change_complete_status(self):
        """used to set a habit to complete or incomplete. Changes the complete_status attribute of an existing habit object,
        between 1 (True/complete) and 0 (False/incomplete), then applies these changes to database entry"""
        while True:
            if self.complete_status == 1:
                confirm = input(f"Would you like to reset '{self.name}' to incomplete? (y/n)")
                if confirm == "y":
                    print(f"'{self.name}' has been reset to incomplete.")
                    self.complete_status = 0

                    # implement saving to history
                    break
                elif confirm == "n":
                    print(f"Incompletion aborted. '{self.name}' remains complete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            elif self.complete_status == 0:
                confirm = input(f"Would you like to complete '{self.name}' for the current interval? (y/n)")
                if confirm == "y":
                    self.complete_status = 1
                    print(f"'{self.name}' has been completed successfully!")
                    # implement change to history data
                    # implement a way to delete existing entry for this date
                    # implement saving to history
                    break
                elif confirm == "n":
                    print(f"Completion aborted. '{self.name}' remains incomplete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            else:
                print(f"Abnormality detected. '{self.name}' has automatically been set to incomplete.")
                self.complete_status = 0
                break



##lvl2: TimeHabit subclass
class TimeHabit(Habit):
    """habit subclass that introduces time as a concept and assigns an interval to each TimeHabit object created"""
    def __init__(self, name, habit_id, desc, active, complete_status, created_on, interval, streak_status, streak_count):
        """Creates a new TimeHabit object"""
        Habit.__init__(self, habit_id, name, desc, active, complete_status, created_on)
        self.interval = interval
        self.streak_status = streak_status
        self.streak_count = streak_count

    @classmethod
    def from_db(cls, row):
        """takes the contents from a dictionary and then returns the values necessary for __init__ to create a new TimeHabit object"""
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"], complete_status=row["complete_status"],
                   created_on=row["created_on"], interval=row["interval"], streak_status=row["streak_status"], streak_count=row["streak_count"])

    def __repr__(self):
        """manages how attributes are returned"""
        return (f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, "
                f"created_on={self.created_on}, interval={self.interval}, streak_status={self.streak_status}, streak_count={self.streak_count})")

    def change_interval(self):
        """used to let the user change interval. Either by choosing an existing one or by manually setting
        the number of days. Will reset complete, streak, streak count."""

        def choose_interval():
            """used during change of interval. Lets the user choose between the desired
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
            """used during change of interval. Lets the user choose the desired number of days (1-365)"""
            while True:
                try:
                    interval_input = int(
                        input("Please enter the desired number of days [1 - 365] for the habits' interval:"))
                    if 1 <= interval_input <= 365:
                        return interval_input
                    else:
                        print("Incorrect input. Please enter a number between 1 and 365.")
                except ValueError:
                    print("Incorrect input. Please enter a number between 1 and 365.")

        while True:
            old_interval = self.interval
            change_type = input(f"Would you like to choose a predefined interval or create a individual interval?\n"
                                f"[1] predefined or [2] individual")
            if change_type == "1":
                new_interval = choose_interval()
                break

            elif change_type == "2":
                new_interval = set_interval()
                break
            else:
                print("Incorrect input. Please enter 1 or 2.")

        if old_interval != new_interval:
            while True:
                confirm = input(f"Would you like to change the current interval of '{self.name}' from"
                                f"'{old_interval}' days to '{new_interval}' days?  (y/n)")

                if confirm == "y":
                    self.interval = new_interval
                    print(f"Changed interval of '{self.name}' to '{self.interval}' days.")
                    #save to db
                    break
                elif confirm == "n":
                    print(f"Interval of '{self.name}' remains at '{self.interval}' days.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

        else:
            print("New interval identical to old interval. Interval change aborted.")

    ##experimental
    def get_update_data(self):
        """return current habit data to the database"""
        update_data = {"habit_id": self.habit_id, "name": self.name,"desc": self.desc, "active": self.active,
                        "complete_status": self.complete_status, "interval": self.interval,
                        "created_on": self.created_on, "streak_status": self.streak_status, "streak_count": self.streak_count}
        return update_data
        #print(update_data)

    def get_history_data(self):
        """return current history data"""
        today = date.today()
        iso_today = today.isoformat()
        new_history_data = {"habit_id": self.habit_id, "date": iso_today, "streak_status": self.streak_status,"streak_count": self.streak_count}
        return new_history_data

    ## needs changes
    def change_complete_status(self):
        """used to set a habit to complete or incomplete. Changes the complete_status attribute of an existing habit object,
        between 1 (True/complete) and 0 (False/incomplete), then applies these changes to database entry"""
        while True:
            if self.complete_status == 1:
                confirm = input(f"Would you like to reset '{self.name}' to incomplete? (y/n)")
                if confirm == "y":
                    print(f"'{self.name}' has been reset to incomplete.")
                    self.complete_status = 0
                    self.streak_count -= 1
                    print(f"The number of consecutive completions for '{self.name}' is now at: '{self.streak_count}'.")
                    if self.streak_count * self.interval < 28:
                        self.streak_status = 0
                        print("This habit is currently not on a streak.")
                    # implement saving to history
                    break
                elif confirm == "n":
                    print(f"Incompletion aborted. '{self.name}' remains complete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            elif self.complete_status == 0:
                confirm = input(f"Would you like to complete '{self.name}' for the current interval? (y/n)")
                if confirm == "y":
                    self.complete_status = 1
                    self.streak_count += 1
                    print(f"'{self.name}' has been completed successfully!")
                    print(f"The number of consecutive completions is now at: {self.streak_count}.")
                    if self.streak_count * self.interval >= 28:
                        self.streak_status = 1
                        print("Congrats, this habit is currently on a streak!")
                        print(f"You have completed it for {self.streak_count * self.interval / 7} weeks in a row!")
                    break
                elif confirm == "n":
                    print(f"Completion aborted. '{self.name}' remains incomplete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            else:
                print(f"Abnormality detected. '{self.name}' has automatically been set to incomplete.")
                self.complete_status = 0
                break



## room for general testing - NOT THE ACTUAL TESTING - just for myself
