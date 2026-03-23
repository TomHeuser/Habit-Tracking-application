from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db
from analytics import analytics as an

def test_create_habit_obj() -> None:
    current_habit_obj = an.create_habit_obj(1)
    assert current_habit_obj.habit_id == 1
    assert current_habit_obj.name == 'Drink Water'
    assert current_habit_obj.desc == 'Drink two liters of water each day'
    assert current_habit_obj.active == 1
    assert current_habit_obj.interval == 1
    assert current_habit_obj.complete_status == 0
    assert current_habit_obj.created_on == "2026-03-01"
    assert current_habit_obj.streak_status == 1
    assert current_habit_obj.streak_count == 28

def test_get_list_of_active_habits() -> None:
    active_habits = db.fetch_active_names()
    test_return = []
    for item in active_habits:
        test_return.append([item["habit_id"], item["name"]])
    assert test_return == [[1, 'Drink Water'], [2, 'Walking'], [3, 'Cleaning'], [4, 'Go swimming'], [5, 'Check finances']]