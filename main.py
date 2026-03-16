import sqlite3

from main_util import main_util as util
from OOP import habit_class
from database import db
from database import db_setup
from main_util.main_util import welcome_message

##during startup
#db_setup.flush_history_table()
#db_setup.flush_habit_table()
db_setup.database_startup()
#db_setup.seed_predefined_habits()

welcome_message()

util.change_complete()
util.change_complete()
