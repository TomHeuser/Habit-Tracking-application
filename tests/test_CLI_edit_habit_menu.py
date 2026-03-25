from cli import edit_habit_menu as ehm
from unittest.mock import patch

def test_attribute_choice() -> None:
    with patch("builtins.input", return_value=1):
        returned_value = ehm.attribute_choice()
        assert returned_value == 1

def test_attribute_choice_value_error() -> None:
    with patch("builtins.input", side_effect=["y", 1]):
        returned_value = ehm.attribute_choice()
        assert returned_value == 1

def test_edit_habit_menu_change_name_successful() -> None:
    with patch("builtins.input", side_effect=[1, 3, "new_name", "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_name") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()

def test_edit_habit_menu_change_name_aborted() -> None:
    with patch("builtins.input", side_effect=[1, 3, "new_name", "n", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_name") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_wrong_id_1() -> None:
    with patch("builtins.input", side_effect=[1, 0, 1]):
        with patch("cli.edit_habit_menu.an.change_habit_name") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_wrong_id_2() -> None:
    with patch("builtins.input", side_effect=[1, 100, 1]):
        with patch("cli.edit_habit_menu.an.change_habit_name") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_invalid_id() -> None:
    with patch("builtins.input", side_effect=[1, "one", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_name") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_desc()-> None:
    with patch("builtins.input", side_effect=[2, 2, "new_desc", "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_description") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()

def test_edit_habit_menu_change_desc_aborted() -> None:
    with patch("builtins.input", side_effect=[1, 3, "new_desc", "n", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_description") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_desc_wrong_id_1() -> None:
    with patch("builtins.input", side_effect=[1, 0, 1]):
        with patch("cli.edit_habit_menu.an.change_habit_description") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_desc_wrong_id_2() -> None:
    with patch("builtins.input", side_effect=[1, 100, 1]):
        with patch("cli.edit_habit_menu.an.change_habit_description") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_desc_invalid_id() -> None:
    with patch("builtins.input", side_effect=[1, "one", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_description") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_interval_predefined() -> None:
    with patch("builtins.input", side_effect=[3, 1, 1, "2", "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()


def test_edit_habit_menu_change_interval_same_to_old() -> None:
    with patch("builtins.input", side_effect=[3, 1, 1, "1", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_interval_predefined_invalid() -> None:
    with patch("builtins.input", side_effect=[3, 1, 1, "3", "2", "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()

def test_edit_habit_menu_change_interval_manual() -> None:
    with patch("builtins.input", side_effect=[3, 1, 2, 5, "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()

def test_edit_habit_menu_change_interval_manual_wrong_interval_1() -> None:
    with patch("builtins.input", side_effect=[3, 1, 2, 0, 1, "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_change_interval_manual_wrong_interval_2() -> None:
    with patch("builtins.input", side_effect=[3, 1, 2, 366, 1, "y", 1]):
        with patch("cli.edit_habit_menu.an.change_habit_interval") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_not_called()

def test_edit_habit_menu_return_to_main() -> None:
    with patch("builtins.input", side_effect=[4,1]):
        with patch("cli.edit_habit_menu.step") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()

def test_edit_habit_menu_return_to_main() -> None:
    with patch("builtins.input", side_effect=[5,1]):
        with patch("cli.edit_habit_menu.step") as mock_func:
            ehm.edit_habit_menu()
            mock_func.assert_called_once()