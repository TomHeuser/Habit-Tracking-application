import sqlite3

from main_util import main_util as util
from OOP import habit_class
from database import db
from database import db_setup


##during startup
db_setup.flush_history_table()
db_setup.flush_habit_table()
db_setup.database_startup()
#db_setup.seed_predefined_habits()

util.change_complete()
util.change_complete()
