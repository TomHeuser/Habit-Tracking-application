import sqlite3

from cli import manage_menu as mm
from cli import analytics_menu as am
from cli import habits_menu as hm
from main_util import main_util as util
from OOP import habit_class
from database import db
from database import db_setup
from main_util.main_util import welcome_message, step

##during startup
db_setup.flush_history_table()
db_setup.flush_habit_table()
#db_setup.seed_predefined_habits()
db_setup.database_startup()


welcome_message()

def submenu_choice():
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


def main_menu():
    while True:
        choice = submenu_choice()
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
            print("Thanks for using 'Unnecessary German Efficiency'\n"
                  "Your application for over the top self improvement.\n"
                  "It's our job to make you become the most automated and replaceable....ah no wait...\n"
                  "optimal, yeah that's it, optimal version of yourself!\n")
            print("Application closing.....")
            step()
            break
        else:
            print("Invalid input, please only enter 1,2,3 or 4.")


main_menu()