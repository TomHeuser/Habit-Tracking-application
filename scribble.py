from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db
import datetime

habit_ids = [1, 2]
for habit in habit_ids:
    last_complete = db.get_last_entry(habit)
    print(last_complete)
    last_iso_date = datetime.date.fromisoformat(last_complete)
    current_day = datetime.date.fromisoformat("2026-03-29")
    day_difference = (current_day - last_iso_date).days
    print(day_difference)