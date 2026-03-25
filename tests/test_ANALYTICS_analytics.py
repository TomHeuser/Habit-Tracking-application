from analytics.analytics import print_habit_details_of_selected_habit
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

def test_print_habit_details_of_selected_habit() -> None:
    with patch("builtins.input", return_value="1"):
        with patch("builtins.print") as mock_print:
            an.print_habit_details_of_selected_habit(1)
            mock_print.assert_called()
            habit_details = db.fetch_single_habit_details(1)
            assert habit_details["habit_id"] == 1
            assert habit_details["name"] == "Drink Water"
            assert habit_details["desc"] == "Drink two liters of water each day"
            assert habit_details["active"] == 1
            assert habit_details["interval"] == 1
            assert habit_details["complete_status"] == 0
            assert habit_details["created_on"] == "2026-03-01"
            assert habit_details["streak_status"] == 1
            assert habit_details["streak_count"] == 28

def test_print_habit_details_of_selected_habit_invalid_arg() -> None:
    with patch("builtins.input", return_value="1"):
        with patch("builtins.print") as mock_print:
            an.print_habit_details_of_selected_habit("a")
            mock_print.assert_called()

def test_get_highest_current_streak() -> None:
    with patch("builtins.input", return_value="1"):
        with patch("builtins.print") as mock_print:
            an.get_highest_current_streak()
            mock_print.assert_called()


def test_get_highest_history_streak() -> None:
    with patch("builtins.input", return_value="1"):
        with patch("builtins.print") as mock_print:
            an.get_highest_history_streak()
            mock_print.assert_called()

def test_print_each_last_entry() -> None:
    with patch("builtins.print") as mock_print:
        an.print_each_last_entry()
        mock_print.assert_called()

def test_print_all_history_entries() -> None:
    with patch("builtins.input", return_value="1"):
        with patch("builtins.print") as mock_print:
            an.print_all_history_entries(1)
            mock_print.assert_called()

def test_save_habit_changes_to_db() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    current_habit_obj.change_name("Drink")
    current_habit_obj.change_complete_status()
    an.save_habit_changes_to_db(current_habit_obj)
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.name == "Drink"
    last_date = db.get_last_entry(1)
    assert last_date == "2026-03-29"
    all_entries = db.load_single_history_all(1)
    len_all_entries = len(all_entries)
    assert len_all_entries == 29
    an.save_habit_changes_to_db(current_habit_obj)
    all_entries = db.load_single_history_all(1)
    len_all_entries = len(all_entries)
    assert len_all_entries == 29

def test_reset_habit() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.complete_status == 0
    assert current_habit_obj.streak_status == 1
    assert current_habit_obj.streak_count == 28
    an.reset_habit(1)
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.complete_status == 0
    assert current_habit_obj.streak_status == 0
    assert current_habit_obj.streak_count == 0

def test_delete_restore_habit() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.active == 1
    assert current_habit_obj.streak_status == 1
    assert current_habit_obj.streak_count == 28
    an.delete_restore_habit(1)
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.active == 0
    assert current_habit_obj.streak_status == 0
    assert current_habit_obj.streak_count == 0

def test_change_habit_name() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.name == "Drink Water"
    an.change_habit_name("1", "Water")
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.name == "Water"

def test_change_habit_description() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.desc == "Drink two liters of water each day"
    an.change_habit_description("1", "2L")
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.desc == "2L"

def test_change_habit_interval() -> None:
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.interval == 1
    an.change_habit_interval("1", "7")
    current_habit_obj = db.load_single_time_habit(1)
    assert current_habit_obj.interval == 7