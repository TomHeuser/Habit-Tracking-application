##Habit class tree

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

    @classmethod
    def from_db(cls, row):
        """takes the contents from a dictionary and then returns the values necessary for __init__ to create a new Habit object"""
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"],
                   complete_status=row["complete_status"], created_on=row["created_on"])

    def __repr__(self):
        """manages how attributes are returned"""
        return f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, created_on={self.created_on})"

    ## methods to change existing habits

    ## needs changing
    def change_name(self):
        """used to change the name attribute of an existing habit object, then applies these changes to database entry"""
        new_name = input("Please enter a new name for this habit:")
        old_name = self.name
        while True:
            confirm = input(f"Would you like to rename this habit to {new_name}? (y/n)")
            if confirm == "y":
                self.name = new_name
                # save to db
                print(f"{old_name} has been renamed to {self.name}")
                break
            else:
                print(f"Name change aborted. Name reset to {self.name}.")
                break

    #needs changing
    def change_desc(self):
        """used to change the desc attribute of an existing habit object, then applies these changes to database entry"""
        new_desc = input("Please enter a new description for this habit:")
        while True:
            confirm = input(f"Would you like to rename this habit to {new_desc}? (y/n)")
            if confirm == "y":
                self.desc = new_desc
                #safe to db
                print(f"The description has been renamed to {self.desc}")
                break
            else:
                print(f"Description change aborted. Description reset to {self.desc}.")
                break

    ## needs changes
    def change_active(self):
        """used to set a habit to active or inactive. Changes the active attribute of an existing habit object,
        between 0 (False, inactive) and 1 (True, active), then applies these changes to database entry"""
        while True:
            if self.active == 1:
                confirm = input(f"Are you sure that you'd like to delete {self.name}? (y/n) [Not lost permanently. Can be restored]")
                if confirm == "y":
                    self.active = 0
                    print(f"{self.name} has been deleted.")
                    # implement change to habit data
                    # implement saving to habit
                    break
                elif confirm == "n":
                    print(f"{self.name} has NOT been deleted.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            elif self.active == 0:
                confirm = input(f"Would you like restore {self.name}? (y/n)")
                if confirm == "y":
                    self.active= 1
                    print(f"{self.name} has been restored.")
                    # implement change to habit data
                    # implement saving to habit
                    break
                elif confirm == "n":
                    print(f"The habit {self.name} was not restored.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            else:
                print("Complete status abnormality detected. Complete status automatically restored to False.")
                self.complete_status = False
                break


    ## needs changes
    def change_complete_status(self):
        """used to set a habit to complete or incomplete. Changes the complete_status attribute of an existing habit object,
        between 1 (True/complete) and 0 (False/incomplete), then applies these changes to database entry"""
        while True:
            if self.complete_status == 1:
                confirm = input(f"Would you like to reset {self.name} to incomplete? (y/n)")
                if confirm == "y":
                    print(f"{self.name} has been reset to incomplete.")
                    self.complete_status = 0
                    # implement change to history data
                    # implement saving to history
                    break
                elif confirm == "n":
                    print(f"Incompletion aborted. {self.name} remains complete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            elif self.complete_status == 0:
                confirm = input(f"Would you like to complete {self.name} for the current interval? (y/n)")
                if confirm == "y":
                    self.complete_status = 1
                    print(f"{self.name} has been completed successfully!")
                    # implement change to history data
                    # implement a way to delete existing entry for this date
                    # implement saving to history
                    break
                elif confirm == "n":
                    print(f"Completion aborted. {self.name} remains incomplete.")
                    break
                else:
                    print("Unexpected input. Please only enter 'y' or 'n'.")

            else:
                print(f"Abnormality detected. {self.name} has automatically been set to incomplete.")
                self.complete_status = 0
                break



##lvl2: TimeHabit subclass
class TimeHabit(Habit):
    """habit subclass that introduces time as a concept and assigns an interval to each TimeHabit object created"""
    def __init__(self, name, habit_id, desc, active, complete_status, created_on, interval):
        """Creates a new TimeHabit object"""
        Habit.__init__(self, habit_id, name, desc, active, complete_status, created_on)
        self.interval = interval

    @classmethod
    def from_db(cls, row):
        """takes the contents from a dictionary and then returns the values necessary for __init__ to create a new TimeHabit object"""
        return cls(habit_id=row["habit_id"], name=row["name"], desc=row["desc"], active=row["active"], complete_status=row["complete_status"], created_on=row["created_on"], interval=row["interval"])

    def __repr__(self):
        """manages how attributes are returned"""
        return f"Habit(habit_id={self.habit_id},name={self.name}, desc={self.desc}, active={self.active}, complete_status={self.complete_status}, created_on={self.created_on}, interval={self.interval})"

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
            change_type = input(f"Would you like to choose a predefined interval or create a individual interval?\n"
                                f"[1] predefined or [2] individual")
            if change_type == "1":
                self.interval = choose_interval()
                #apply changes to db
                break

            elif change_type == "2":
                self.interval = set_interval()
                #apply changes to db
                break
            else:
                print("Incorrect input. Please enter 1 or 2.")













## room for general testing - NOT THE ACTUAL TESTING - just for myself
