from cli import habits_menu as hm
from unittest.mock import patch
from database import db as db
from analytics.analytics import get_list_of_active_habits

def test_habits_menu_choice():
    with patch("builtins.input", return_value=1):
        returned_value = hm.habits_menu_choice()
        assert returned_value == 1
    with patch("builtins.input", side_effect=["1"]):
        returned_value = hm.habits_menu_choice()
        assert returned_value == 1
    with patch("builtins.input", side_effect=[2]):
        returned_value = hm.habits_menu_choice()
        assert returned_value == 2
    with patch("builtins.input", side_effect=["a", 2]):
        returned_value = hm.habits_menu_choice()
        assert returned_value == 2

def test_habits_menu_complete_complete() -> None:
    with patch("builtins.input", side_effect=[1, 1, "y", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 1

def test_habits_menu_complete_complete_abort() -> None:
    with patch("builtins.input", side_effect=[1, 1, "n", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 0

def test_habits_menu_complete_complete_on_2nd_confirm() -> None:
    with patch("builtins.input", side_effect=[1, 1, "2", "y", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 1

def test_habits_menu_complete_back_to_main() -> None:
    with patch("builtins.input", side_effect=[2]):
        with patch("cli.habits_menu.an.get_list_of_active_habits") as mock_func:
            with patch("cli.habits_menu.return_to_main") as mock_func2:
                hm.habits_menu()
                mock_func.assert_not_called()
                mock_func2.assert_called_once()

def test_habits_menu_complete_complete_incomplete() -> None:
    with patch("builtins.input", side_effect=[1, 1, "y", 1, 1, "y", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 0

def test_habits_menu_complete_complete_incomplete_abort() -> None:
    with patch("builtins.input", side_effect=[1, 1, "y", 1, 1, "n", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 1

def test_habits_menu_complete_complete_incomplete_2nd_confirm() -> None:
    with patch("builtins.input", side_effect=[1, 1, "y", 1, 1, "d", "y", 2]):
        hm.habits_menu()
        test_habit = db.load_single_time_habit(1)
        assert test_habit.complete_status == 0