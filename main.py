from analytics.functions_util import startup
from cli import cli_util as cli
from cli import manage_menu as mm
from cli import analytics_menu as am
from cli import habits_menu as hm
from main_util import handle_dates as hd
from main_util.main_util import step
from database import db_setup



def main_menu():
    while True:
        choice = cli.submenu_choice()
        if choice == 1:
            print("Opening habits menu.....")
            hm.habits_menu()

        elif choice == 2:
            print("Opening menu to manage habits.....")
            mm.manage_menu()

        elif choice == 3:
            print("Opening analytics menu.....\n")
            am.analytics_menu()
        elif choice == 4:
            confirm = cli.exit_confirmation_choice()
            if confirm == "y":
                print("Thanks for using 'Unnecessary German Efficiency'\n"
                      "Your application for over the top self improvement.\n"
                      "It's our job to make you become the most automated and replaceable....ah no wait...\n"
                      "optimal, yeah that's it, optimal version of yourself!\n")
                print("Application closing.....")
                step()
                break
            else:
                print("Aborting exit procedure.... Returning to main menu....")
                step()
        else:
            print("Invalid input, please only enter 1,2,3 or 4.")


#set operation mode and date
op_mode = cli.operation_mode()
if op_mode == "t":
    db_setup.flush_history_table()
    db_setup.flush_habit_table()
    hd.set_test_date()
    hd.set_test_week()
else:
    hd.set_current_date()
    hd.set_current_week()

#startup
startup(hd.current_day, hd.current_week)

#lifecycle
main_menu()