##Habit class tree
from main_util import handle_dates as hd
from cli import cli_util as cli

##lvl1: Habit superclass
class Habit:
    def __init__(self, habit_id, name, desc, active, complete_status, created_on):
        """Creates a new Habit object"""
        self.name = name
        self.habit_id = habit_id
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

    def change_name(self, new_name):
        """used to change the name attribute of an existing habit object, then applies these changes to database entry"""
        self.name = new_name

    def change_desc(self, new_desc):
        """used to change the desc attribute of an existing habit object, then applies these changes to database entry"""
        self.desc = new_desc

    def change_active(self):
        """used to set a simple habit (no streak/interval) to active or inactive. Changes the active attribute of an existing habit object,
        between 0 (False, inactive) and 1 (True, active), then applies these changes to database entry"""
        if self.active == 1:
            self.active = 0
            self.complete_status = 0
        else:
            self.active = 1


    ## needs changes
    def change_complete_status(self):
        """used to set a habit to complete or incomplete. Changes the complete_status attribute of an existing habit object,
        between 1 (True/complete) and 0 (False/incomplete), then applies these changes to database entry"""
        if self.complete_status == 1:
            self.complete_status = 0
        else:
            self.complete_status = 1



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



    def change_interval(self, new_interval):
        """used to let the user change interval. Either by choosing an existing one or by manually setting
        the number of days. Will reset complete, streak, streak count."""
        self.interval = new_interval
        print(f"Changed interval of '{self.name}' to '{self.interval}' days.")
        self.streak_count = 0
        self.streak_status = 0


    def change_active(self):
        """used to set a time habit to active or inactive. Changes the active attribute of an existing habit object,
        between 0 (False, inactive) and 1 (True, active), then applies these changes to database entry"""

        if self.active == 1:
            self.active = 0
            self.complete_status = 0
            self.streak_status = 0
            self.streak_count = 0
        elif self.active == 0:
            self.active = 1
        else:
            print("Habit status abnormality detected. Habit was automatically restored to 'active'.")
            self.complete_status = 1


    def reset(self):
        """resets objects complete_status, streak_status and streak_count to zero"""
        self.complete_status = 0
        self.streak_status = 0
        self.streak_count = 0


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
        current_day = hd.current_day
        new_history_data = {"habit_id": self.habit_id, "date": current_day, "complete_status": self.complete_status, "streak_status": self.streak_status,"streak_count": self.streak_count}
        return new_history_data

    ## needs changes
    def change_complete_status(self):
        """used to set a habit to complete or incomplete. Changes the complete_status attribute of an existing habit object,
        between 1 (True/complete) and 0 (False/incomplete), then applies these changes to database entry"""

        if self.complete_status == 1:
            self.complete_status = 0
            self.streak_count -= 1
            print(f"The number of consecutive completions for '{self.name}' is now at: '{self.streak_count}'.")
            if self.streak_count * self.interval < 28:
                self.streak_status = 0
                print("This habit is currently not on a streak.")
        elif self.complete_status == 0:
            self.complete_status = 1
            self.streak_count += 1
            print(f"The number of consecutive completions is now at: {self.streak_count}.")
            if self.streak_count * self.interval >= 28:
                self.streak_status = 1
                print("Congrats, this habit is currently on a streak!")
                consecutive_weeks = self.streak_count * self.interval / 7
                rounded_consecutive_weeks = round(consecutive_weeks, 1)
                print(f"You have completed it for {rounded_consecutive_weeks} weeks in a row!")
        else:
            print(f"Abnormality detected. '{self.name}' has automatically been set to incomplete.")
            self.complete_status = 0