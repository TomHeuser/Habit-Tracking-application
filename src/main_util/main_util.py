from datetime import date
from cli import cli_util as cli
import sys as sys


## testing data
def get_operation_mode_input():
    op_mode = cli.operation_mode()
    return op_mode

def real_or_test_dates_day(op_mode):
    dates_choice = op_mode
    if dates_choice == "t":
        current_day = date.fromisoformat("2026-03-29")
        return current_day
    else:
        today = date.today()
        return today

def real_or_test_dates_week(op_mode):
    dates_choice = op_mode
    if dates_choice == "t":
        current_week = 2026 * 52 + 13
        return current_week
    else:
        today = date.today()
        current_week = 2026 * 52 + today.isocalendar().week
        return current_week


## general stuff
def step():
    """just a mal input that will be dropped instantly, creates a pause until use wants to continue
    (often also called stop or pause)"""
    sys.stdin.flush()
    input("\nPress any key to continue...\n")

def return_to_main():
    """returns command to return to main, currently not necessary"""
    print("Returning to main menu....")
    return_value = "BACK"
    return return_value