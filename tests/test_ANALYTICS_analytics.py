from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db

#def test_create_habit_obj() -> None:
    #current_habit_obj = db.load_single_time_habit(1)
    #assert current_habit_obj.habit_id ==

#def test_change_habit_obj_complete() -> None:

def test_get_list_of_active_habits() -> None:
    active_habits = db.fetch_active_names()
    test_return = []
    for item in active_habits:
        test_return.append([item["habit_id"], item["name"]])
    assert test_return == [[1, 'Drink Water'], [2, 'Walking'], [3, 'Cleaning'], [4, 'Go swimming'], [5, 'Check finances']]