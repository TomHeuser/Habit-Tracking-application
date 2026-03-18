## just a loose file to try out small code snippets ------> delete during/at the end of phase 3

from database import db as db
from main_util.main_util import step
from datetime import date
today = date.today()
iso_today = today.isoformat()
# date has method called isocalendar() returning week number of given date -> use for week calculation later?
