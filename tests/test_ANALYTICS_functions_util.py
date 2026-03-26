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
