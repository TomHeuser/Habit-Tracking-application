from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db

habit_rows = db.load_single_history_recent(1)
print(habit_rows)
print(type(habit_rows))


habit_id = 1
iso_today = "2026-03-28"
retuned = db.check_existing_history_date(habit_id, iso_today)
print(retuned)

habit_id = 1
iso_today = "2026-04-29"
retuned = db.check_existing_history_date(habit_id, iso_today)
print(retuned)