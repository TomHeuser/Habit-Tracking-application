from datetime import date


current_day = None
current_week = None

def set_test_date():
    global current_day
    current_day = date.fromisoformat("2026-03-29")

def set_current_date():
    global current_day
    current_day = date.today()
    #print(current_day)

def set_test_week():
    global current_week
    current_week = 2026 * 52 + 13

def set_current_week():
    global current_week
    actual_date = date.today()
    current_week = 2026 * 52 + actual_date.isocalendar().week
    #print(current_week)