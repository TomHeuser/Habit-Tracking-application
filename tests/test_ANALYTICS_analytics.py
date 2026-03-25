from main_util.main_util import step
from main_util import handle_dates as hd
from database import db as db
from analytics import analytics as an
from unittest.mock import patch


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

## expand test?
def test_change_habit_obj_complete() -> None:
    an.change_habit_obj_complete(1)
    last_entry = db.get_last_entry(1)
    assert last_entry == "2026-03-29"

def test_get_list_of_active_habits() -> None:
    active_habits = db.fetch_active_names()
    test_return = []
    for item in active_habits:
        test_return.append([item["habit_id"], item["name"]])
    assert test_return == [[1, 'Drink Water'], [2, 'Walking'], [3, 'Cleaning'], [4, 'Go swimming'], [5, 'Check finances']]
    with patch("builtins.print") as mock_print:
        an.get_list_of_active_habits()
        mock_print.assert_called()


def test_get_list_of_all_habits() -> None:
    with patch("builtins.print") as mock_print:
        an.get_list_of_all_habits()
        mock_print.assert_called()

def 