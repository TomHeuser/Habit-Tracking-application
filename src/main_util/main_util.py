import sys as sys

## general stuff
def step():
    """just a mal input that will be dropped instantly, creates a pause until use wants to continue
    (often also called stop or pause)"""
    if sys.stdin.isatty():
        sys.stdin.flush()
    input("\nPress any key to continue...\n")

def return_to_main():
    """returns command to return to main, currently not necessary"""
    print("Returning to main menu....")
    return_value = "BACK"
    return return_value