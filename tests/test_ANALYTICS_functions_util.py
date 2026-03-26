from analytics import functions_util as fn
from unittest.mock import patch
from datetime import date
from database import db as db
from main_util import handle_dates as hd
from main_util.handle_dates import current_day


def test_welcome_message() -> None:
    with patch("builtins.print") as mock_print:
        fn.welcome_message()
        mock_print.assert_called()

def test_date_message() -> None:
    with patch("builtins.print") as mock_print:
        current_date = "2026-03-29"
        fn.date_message(current_date)
        mock_print.assert_called()

def test_first_startup_message() -> None:
    with patch("builtins.input", return_value="s"):
        with patch("builtins.print") as mock_print:
            with patch("analytics.functions_util.get_list_of_all_habits") as mock_func:
                current_date = "2026-03-29"
                fn.first_startup_message(current_date)
                mock_print.assert_called()
                mock_func.assert_called_with()


def test_startup_complete_message() -> None:
    with patch("builtins.print") as mock_print:
        fn.startup_complete_message()
        mock_print.assert_called()

def test_handle_weekly_reset() -> None:
    with patch("analytics.functions_util.db.get_weekly_id_list", return_value = [3, 4, 5]) as mock_func:
        with patch ("analytics.functions_util.db.startup_habit_reset") as mock_func2:
            with patch("builtins.print") as mock_print:
                current_week = 2026 * 52 + 13
                fn.handle_weekly_reset(current_week)
                mock_print.assert_called()
                mock_func.assert_called_once()
                mock_func2.assert_called_once()

def test_handle_weekly_reset_future_reset() -> None:
    with patch("analytics.functions_util.db.get_weekly_id_list", return_value = [3, 4, 5]) as mock_func:
        with patch ("analytics.functions_util.db.startup_habit_reset") as mock_func2:
            with patch("builtins.print") as mock_print:
                current_week = 2026 * 52 + 15
                fn.handle_weekly_reset(current_week)
                mock_print.assert_called()
                mock_func.assert_called_once()
                assert mock_func2.call_count == 3

def test_handle_weekly_reset_future_incomplete() -> None:
    with patch("analytics.functions_util.db.get_weekly_id_list", return_value = [3, 4, 5]) as mock_func:
        with patch ("analytics.functions_util.db.startup_habit_incomplete") as mock_func2:
            with patch("builtins.print") as mock_print:
                current_week = 2026 * 52 + 14
                fn.handle_weekly_reset(current_week)
                mock_print.assert_called()
                mock_func.assert_called_once()
                assert mock_func2.call_count == 2

def test_handle_daily_reset() -> None:
    with patch("analytics.functions_util.db.get_daily_id_list", return_value = [1, 2]) as mock_func:
        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func2:
            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func3:
                with patch("builtins.print") as mock_print:
                    current_day = "2026-03-28"
                    fn.handle_daily_reset(current_day)
                    mock_print.assert_called()
                    mock_func.assert_called_once()
                    assert mock_func2.call_count == 0
                    assert mock_func3.call_count == 0

def test_handle_daily_reset_incomplete() -> None:
    with patch("analytics.functions_util.db.get_daily_id_list", return_value = [1, 2]) as mock_func:
        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func2:
            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func3:
                with patch("builtins.print") as mock_print:
                    current_day = date.fromisoformat("2026-03-29")
                    fn.handle_daily_reset(current_day)
                    mock_print.assert_called()
                    mock_func.assert_called_once()
                    assert mock_func2.call_count == 2
                    assert mock_func3.call_count == 0

def test_handle_daily_reset_reset() -> None:
    with patch("analytics.functions_util.db.get_daily_id_list", return_value = [1, 2]) as mock_func:
        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func2:
            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func3:
                #with patch("builtins.print") as mock_print:
                    current_day = date.fromisoformat("2026-03-30")
                    fn.handle_daily_reset(current_day)
                    #mock_print.assert_called()
                    mock_func.assert_called_once()
                    assert mock_func2.call_count == 0
                    assert mock_func3.call_count == 2

def test_handle_manual_reset() -> None:
    with patch("analytics.functions_util.db.get_manual_id_list", return_value=[6]):
        with patch("analytics.functions_util.db.get_name_for_id", return_value = "Manual Test"):
            with patch("analytics.functions_util.db.get_last_entry", return_value = "2026-03-25"):
                with patch("analytics.functions_util.db.get_interval", return_value=5):
                    with patch("analytics.functions_util.db.get_creation_date", return_value="2026-03-20"):
                        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func:
                            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func2:
                                current_day = date.fromisoformat("2026-03-29")
                                fn.handle_manual_reset(current_day)
                                mock_func.assert_not_called()
                                mock_func2.assert_not_called()

def test_handle_manual_reset_incomplete() -> None:
    with patch("analytics.functions_util.db.get_manual_id_list", return_value=[6]):
        with patch("analytics.functions_util.db.get_name_for_id", return_value = "Manual Test"):
            with patch("analytics.functions_util.db.get_last_entry", return_value = "2026-03-25"):
                with patch("analytics.functions_util.db.get_interval", return_value=5):
                    with patch("analytics.functions_util.db.get_creation_date", return_value="2026-03-20"):
                        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func:
                            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func2:
                                current_day = date.fromisoformat("2026-03-30")
                                fn.handle_manual_reset(current_day)
                                mock_func.assert_called_once()
                                mock_func2.assert_not_called()

def test_handle_manual_reset_reset() -> None:
    with patch("analytics.functions_util.db.get_manual_id_list", return_value=[6]):
        with patch("analytics.functions_util.db.get_name_for_id", return_value = "Manual Test"):
            with patch("analytics.functions_util.db.get_last_entry", return_value = "2026-03-25"):
                with patch("analytics.functions_util.db.get_interval", return_value=5):
                    with patch("analytics.functions_util.db.get_creation_date", return_value="2026-03-20"):
                        with patch("analytics.functions_util.db.startup_habit_incomplete") as mock_func:
                            with patch("analytics.functions_util.db.startup_habit_reset") as mock_func2:
                                current_day = date.fromisoformat("2026-04-04")
                                fn.handle_manual_reset(current_day)
                                mock_func.assert_not_called()
                                mock_func2.assert_called_once()

def test_startup_false () -> None:
    with patch("analytics.functions_util.db_setup.database_startup", return_value=False):
        with patch("builtins.input", side_effect=["s", "s"]):
            with patch("analytics.functions_util.handle_daily_reset") as mock_func:
                with patch("analytics.functions_util.handle_weekly_reset") as mock_func2:
                    with patch("analytics.functions_util.handle_manual_reset") as mock_func3:
                        with patch("builtins.print") as mock_print:
                            current_date = date.fromisoformat("2026-03-29")
                            current_week = 2026 * 52 + 13
                            fn.startup(current_date, current_week)
                            mock_print.assert_called()
                            mock_func.assert_called_once()
                            mock_func2.assert_called_once()
                            mock_func3.assert_called_once()

def test_startup_true () -> None:
    with patch("analytics.functions_util.db_setup.database_startup", return_value=True):
        with patch("builtins.input", returned_value ="s"):
            with patch("analytics.functions_util.handle_daily_reset") as mock_func:
                with patch("analytics.functions_util.handle_weekly_reset") as mock_func2:
                    with patch("analytics.functions_util.handle_manual_reset") as mock_func3:
                        with patch("builtins.print") as mock_print:
                            current_date = date.fromisoformat("2026-03-29")
                            current_week = 2026 * 52 + 13
                            fn.startup(current_date, current_week)
                            mock_print.assert_called()
                            mock_func.assert_not_called()
                            mock_func2.assert_not_called()
                            mock_func3.assert_not_called()

def test_get_name() -> None:
    with patch("builtins.input", side_effect = ["new name", "y"]):
        new_name = fn.get_name()
        assert new_name == "new name"
    with patch("builtins.input", side_effect = ["new name", "n", "another name", "y"]):
            new_name = fn.get_name()
            assert new_name == "another name"
    with patch("builtins.input", side_effect = ["new name", "f", "3rd name", "y"]):
        new_name = fn.get_name()
        assert new_name == "3rd name"

def test_get_desc() -> None:
    with patch("builtins.input", side_effect = ["new desc", "y"]):
        new_desc = fn.get_desc()
        assert new_desc == "new desc"
    with patch("builtins.input", side_effect = ["new desc", "n", "another desc", "y"]):
        new_desc = fn.get_desc()
        assert new_desc == "another desc"
    with patch("builtins.input", side_effect = ["new desc", "f", "3rd desc", "y"]):
        new_desc = fn.get_desc()
        assert new_desc == "3rd desc"

def test_interval_confirm() -> None:
    with patch("builtins.input", side_effect = ["y"]):
        return_value = fn.interval_confirm(5)
        assert return_value is True
    with patch("builtins.input", side_effect = ["n"]):
        return_value = fn.interval_confirm(5)
        assert return_value is False
    with patch("builtins.input", side_effect = ["f"]):
        return_value = fn.interval_confirm(5)
        assert return_value is False

def test_set_predefined_interval() -> None:
    with patch("builtins.input", side_effect = ["1"]):
        new_interval = fn.set_predefined_interval()
        assert new_interval == 1
    with patch("builtins.input", side_effect = ["2"]):
        new_interval = fn.set_predefined_interval()
        assert new_interval == 7
    with patch("builtins.input", side_effect = ["3", "2"]):
        new_interval = fn.set_predefined_interval()
        assert new_interval == 7

def test_set_manual_interval() -> None:
    with patch("builtins.input", side_effect = ["5"]):
        new_interval = fn.set_manual_interval()
        assert new_interval == 5
    with patch("builtins.input", side_effect = ["0", "5"]):
        new_interval = fn.set_manual_interval()
        assert new_interval == 5
    with patch("builtins.input", side_effect = ["366", "5"]):
        new_interval = fn.set_manual_interval()
        assert new_interval == 5

def test_get_interval() -> None:
    with patch("builtins.input", side_effect = ["1", "1","y"]):
        new_interval = fn.get_interval()
        assert new_interval == 1
    with patch("builtins.input", side_effect = ["1", "1", "n", "1", "2", "y"]):
        new_interval = fn.get_interval()
        assert new_interval == 7
    with patch("builtins.input", side_effect = ["2", "5", "y"]):
        new_interval = fn.get_interval()
        assert new_interval == 5
    with patch("builtins.input", side_effect = ["2", "7", "n", "2", "5", "y"]):
        new_interval = fn.get_interval()
        assert new_interval == 5
    with patch("builtins.input", side_effect = ["3","2", "5", "y"]):
        new_interval = fn.get_interval()
        assert new_interval == 5

def test_create_new_habits() -> None:
    with patch("builtins.input", side_effect = ["new name", "y", "new desc", "y", "1", "1","y"]):
        current_date = "2026-03-29"
        new_habit_data = fn.create_new_habit(current_date)
        assert new_habit_data["name"] == "new name"
        assert new_habit_data["desc"] == "new desc"
        assert new_habit_data["active"] == 1
        assert new_habit_data["complete_status"] == 0
        assert new_habit_data["interval"] == 1
        assert new_habit_data["streak_status"] == 0
        assert new_habit_data["streak_count"] == 0
        assert new_habit_data["created_on"] == "2026-03-29"

def test_create_habit() -> None:
    with patch("builtins.input", side_effect=["new name", "y", "new desc", "y", "1", "1", "y"]):
        current_date = "2026-03-29"
        fn.create_habit(current_date)
        test_habit = db.load_single_time_habit(6)
        assert test_habit.name == "new name"
        assert test_habit.desc == "new desc"
        assert test_habit.active == 1
        assert test_habit.complete_status == 0
        assert test_habit.interval == 1
        assert test_habit.streak_status == 0
        assert test_habit.streak_count == 0
        assert test_habit.created_on == "2026-03-29"