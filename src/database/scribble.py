## just a loose file to try out small code snippets ------> delete during/at the end of phase 3


#from datetime import date
        #today = date.today()
        #iso_today = today.isoformat()


def get_interval_approach():
    while True:
        interval_approach = input(f"Do you want to choose a predefined interval or would you like to set the interval manually?\n"
                                  f"[1] for predefined\n"
                                  f"[2] to set in manually")
        while True:
            if interval_approach == "1":
                predefined_interval = input("You can choose between daily and weekly \n"
                                            "[1] daily"
                                            "[2] weekly")
                if predefined_interval == "1":
                    new_interval = 1
                    break
                elif predefined_interval == "2":
                    new_interval = 7
                    break
                else:
                    print("Invalid input. Please enter either 1 or 2.")
                    continue
            elif interval_approach == "2":
                try:
                    manual_interval = int(input("Please enter desired number of days [1-365]:"))
                    if 1 <= manual_interval <= 365:
                        new_interval = manual_interval
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 365.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 365.")
                    continue
            else:
                print("Please enter either 1 or 2.")
                continue

        while True:
            try:
                interval_confirm = input(f"Do you want the new interval to be {new_interval} days?\n"
                                         f"[y] for yes or [n] for no")
                if interval_confirm == "y":
                    interval = new_interval
                    break
                else:
                    print("Ok, lets start anew with then selection of your new interval.")
                    continue
            except:
                print("Ok, lets start anew with then selection of your new interval.")
                continue
        break
