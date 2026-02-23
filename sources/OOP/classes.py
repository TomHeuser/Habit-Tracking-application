from datetime import date

#Habit class tree

#lvl1: Habit superclass
class Habit:
    def __init__(self, name, habit_id):
        self.name = name
        self.habit_id = habit_id
        self.desc = input("Please enter a description for your new habit:")     #user input to add description (str)
        self.complete_status = False
        self.completed_on = "none"
        self.active = True
        today = date.today()
        iso_today = today.isoformat()
        self.created_on = iso_today

    #functions that all habits of any subclass should inherit:
    # rough ideas/setup !!!!!!! needs further attention
    def set_id(self, habit_id):
        self.habit_id = habit_id
    def set_name(self, name):
        self.name = name
    def set_complete(self, complete_status):
        self.complete_status = complete_status
    def set_active(self, active):
        self.active = active
    #def edit_habit(self, habit):
        #set_id()
        #set_name()
        #set_complete()
        #set_active()
    #def habit_history_append(self):
        ## a way to save habit attributes to databank

#lvl 2: implementing the idea of time, while keeping it simple and flexible, rather a foundation that an actual implementation
class IntervalHabit(Habit):
    def __init__(self, name, habit_id):
         Habit.__init__(self, name, habit_id)
         self.streak_count = 0
         self.streak_status = False
         self.interval = 0

    def set_interval(self, interval):
        self.interval = interval
    def change_interval(self, interval):
        self.interval = interval
    def add_streak(self, streak):
        self.streak_count += 1
        if streak > 27:
            self.streak_status = True
    def reset_streak(self):
        self.streak_status = False
        self.streak_count = 0
    def set_streak(self, streak_status, streak_count):
        self.streak_status = streak_status
        self.streak_count = streak_count

#lvl 3: distinguish between PredefinedIntervalHabit and ManualIntervalHabit
class PredefinedIntervalHabit(IntervalHabit):

    def choose_interval(self):
        while True:
            #userinput to choose between daily and weekly (eg:1 and 7)
            interval_input = input("Please choose the habits' interval:\n[1]daily\n[2]weekly\n")
            if interval_input == "1":
                return 1
            elif interval_input == "2":
                return 7
            else:
                print("Incorrect input. Please enter 1 or 2.")

    def __init__(self, name, habit_id):
        IntervalHabit.__init__(self, name, habit_id)
        self.streak_count = 0
        self.streak_status = False
        self.interval = self.choose_interval()


class ManualIntervalHabit(IntervalHabit):
    def __init__(self, name, habit_id):
        IntervalHabit.__init__(self, name, habit_id)
        self.streak_count = 0
        self.streak_status = False
        while True:
            try:
                interval_input = int(input("Please enter the desired number of days [1 - 365] for the habits' interval:"))
                if 1 <= interval_input <= 365:
                    self.interval = interval_input
                    break
            except ValueError:
                print("Incorrect input. Please enter a number between 1 and 365.")

    def set_interval(self, interval):
        pass
        #self.interval = #userinput that lets user input any custom number of days



# room for general testing - NOT THE ACTUAL TESTING - just for myself
test_class1 = Habit("Simple Habit",1)
print(f"name: {test_class1.name}, Id: {test_class1.habit_id}, description: {test_class1.desc}, created on: {test_class1.created_on},"
      f"completed on: {test_class1.completed_on}, complete?: {test_class1.complete_status}, active?: {test_class1.active}")

test_class2 = IntervalHabit("Interval Habit",2)
print(f"name: {test_class2.name}, Id: {test_class2.habit_id}, description: {test_class2.desc}, created on: {test_class2.created_on},"
      f"completed on: {test_class2.completed_on},complete?: {test_class2.complete_status}, active?: {test_class2.active}, "
      f"streak?: {test_class2.streak_status}, streak_count: {test_class2.streak_count}, interval: {test_class2.interval}")

test_class3 = PredefinedIntervalHabit("Predefined Interval Habit",3)
print(f"name: {test_class3.name}, Id: {test_class3.habit_id}, description: {test_class3.desc},created on: {test_class3.created_on},"
      f"completed on: {test_class3.completed_on}, complete?: {test_class3.complete_status}, active?: {test_class3.active}, "
      f"streak?: {test_class3.streak_status}, streak_count: {test_class3.streak_count}, interval: {test_class3.interval}")

test_class4 = ManualIntervalHabit("Manual Interval Habit",4)
print(f"name: {test_class4.name}, Id: {test_class4.habit_id}, description: {test_class4.desc},created on: {test_class4.created_on},"
      f"completed on: {test_class4.completed_on}, complete?: {test_class4.complete_status}, active?: {test_class4.active}, "
      f"streak?: {test_class4.streak_status}, streak_count: {test_class4.streak_count}, interval: {test_class4.interval}")