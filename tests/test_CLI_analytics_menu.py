from cli import analytics_menu as anm
from unittest.mock import patch

def test_analytics_choice() -> None:
    with patch("builtins.input", return_value=1):
        returned_value = anm.analytics_choice()
        assert returned_value == 1

def test_analytics_choice_type_error() -> None:
    with patch("builtins.input", side_effects=["f",1]):
        returned_value = anm.analytics_choice()
        assert returned_value == 1

def test_analytics_menu_calls_list_of_active_habits() -> None:
        with patch("builtins.input",  side_effect=[1, 1, 7]):
            with patch("cli.analytics_menu.an.get_list_of_active_habits") as mock_func:
                anm.analytics_menu()
                mock_func.assert_called_once()

def test_analytics_menu_habit_details() -> None:
    with patch("builtins.input", side_effect=[2, 1, 7]):
        with patch("cli.analytics_menu.an.get_list_of_all_habits") as mock_func:
            with patch("cli.analytics_menu.an.print_habit_details_of_selected_habit") as mock_func_2:
                anm.analytics_menu()
                mock_func.assert_called_once()
                mock_func_2.assert_called_once()

def test_analytics_menu_habit_details_value_error() -> None:
    with patch("builtins.input", side_effect=[2, "y", 7]):
        with patch("cli.analytics_menu.an.get_list_of_all_habits") as mock_func:
            with patch("cli.analytics_menu.an.print_habit_details_of_selected_habit") as mock_func_2:
                anm.analytics_menu()
                mock_func.assert_called_once()
                mock_func_2.assert_not_called()

def test_analytics_menu_get_highest_current_streak() -> None:
    with patch("builtins.input", side_effect=[3, 7]):
        with patch ("cli.analytics_menu.an.get_highest_current_streak") as mock_func:
            anm.analytics_menu()
            mock_func.assert_called_once()

def test_analytics_menu_get_highest_history_streak() -> None:
    with patch("builtins.input", side_effect=[4, 7]):
        with patch ("cli.analytics_menu.an.get_highest_history_streak") as mock_func:
            anm.analytics_menu()
            mock_func.assert_called_once()

def test_analytics_menu_get_highest_habit_streak() -> None:
    with patch("builtins.input", side_effect=[5, 1, 7]):
        with patch("cli.analytics_menu.an.get_list_of_all_habits") as mock_func:
            with patch("cli.analytics_menu.an.print_all_history_entries") as mock_func_2:
                anm.analytics_menu()
                mock_func.assert_called_once()
                mock_func_2.assert_called_once()

def test_analytics_menu_get_highest_habit_streak_value_error() -> None:
    with patch("builtins.input", side_effect=[5, "y", 7]):
        with patch("cli.analytics_menu.an.get_list_of_all_habits") as mock_func:
            with patch("cli.analytics_menu.an.print_all_history_entries") as mock_func_2:
                anm.analytics_menu()
                mock_func.assert_called_once()
                mock_func_2.assert_not_called()



def test_analytics_menu_list_of_last_completions() -> None:
    with patch("builtins.input", side_effect=[6, 1, 7]):
        with patch("cli.analytics_menu.an.print_each_last_entry") as mock_func:
            anm.analytics_menu()
            mock_func.assert_called_once()

def test_analytics_menu_return_to_main() -> None:
    with patch("builtins.input", return_value=7):
        returned_value = anm.analytics_menu()
        assert returned_value == "BACK"

def test_analytics_menu_invalid_analytics_choice() -> None:
    with patch("builtins.input", side_effect=["f", 7]):
        returned_value = anm.analytics_menu()
        assert returned_value == "BACK"