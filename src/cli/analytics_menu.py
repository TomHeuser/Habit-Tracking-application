from database import db as db
from main_util.main_util import step


def analytics_choice():
    while True:
        print("Analytics menu:\n")
        try:
            choice = int(input("Choose option:\n"
              "[1] get list of active habits\n"
              "[2] get habit details of selected habit\n"
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
            print("Your currently active habits are:")
            active_habits = db.fetch_active_names()
            for item in active_habits:
                print(item["habit_id"], item["name"])
            print("")
            #print(type(active_habits))
            step()
        elif choice == 2:
            print("habit details:\n"
                  "\n"
                  "Current habits:")
            #implementet functionality
            all_habits = db.fetch_names()
            for item in all_habits:
                print(f"[{item["habit_id"]}] {item["name"]}")
            while True:
                try:
                    chosen_id = int(input("Please enter one the above numbers of a habit to see it's details.\n"
                                      "Please only enter one number at a time.\n"
                                      ""))
                    try:
                        habit_details = db.fetch_single_habit_details(chosen_id)
                        #print(type(habit_detail))
                        #print(habit_details["habit_id"], habit_details["name"], habit_details["desc"], habit_details["active"],
                              #habit_details["interval"], habit_details["complete_status"], habit_details["created_on"],
                              #habit_details["streak_status"], habit_details["streak_count"])
                        print(f"Habit name: {habit_details['name']}\n"
                              f"Habit description: {habit_details['desc']}")
                        if habit_details["active"] == 1:
                            print("This habit is currently active.")
                        else:
                            print("This habit is currently inactive.")
                        print(f"habit interval: {habit_details['interval']}")
                        if habit_details["complete_status"] == 1:
                            print("currently completed.")
                        else:
                            print("Currently incomplete.")
                        print(f"Created at {habit_details['created_on']}")
                        if habit_details["streak_status"] == 1:
                            print("This habit is currently on a streak.")
                        else:
                            print("This habit is not on a streak at the moment.")
                        print(f"Number of consecutive completions: {habit_details['streak_count']}\n"
                              f"")
                        step()
                        break
                    except TypeError:
                        print("Invalid input")
                except ValueError:
                    print("Invalid input")
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



