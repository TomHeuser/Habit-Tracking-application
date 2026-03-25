from cli import manage_menu as mm
from unittest.mock import patch
from analytics.analytics import delete_restore_habit

def test_manage_menu_choice() -> None:
    with patch("builtins.input", return_value=1):
        returned_value = mm.manage_menu_choice()
        assert returned_value == 1

def test_manage_menu_choice_value_error() -> None:
    with patch("builtins.input", side_effect=["f", 1]):
        returned_value = mm.manage_menu_choice()
        assert returned_value == 1

def test_manage_menu_return_to_main() -> None:
    with patch("builtins.input", return_value=6):
        with patch("cli.manage_menu.return_to_main") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_create_habits() -> None:
    with patch("builtins.input", side_effect=[1, 6]):
        with patch("cli.manage_menu.func.create_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_edit_habit_menu() -> None:
    with patch("builtins.input", side_effect=[3, 6]):
        with patch("cli.manage_menu.ehm.edit_habit_menu") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_delete_habit() -> None:
    with patch("builtins.input", side_effect=[2, 1, "y", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_delete_habit_abort() -> None:
    with patch("builtins.input", side_effect=[2, 1, "n", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_delete_habit_wrong_input() -> None:
    with patch("builtins.input", side_effect=[2, 1, "f", 1, "y", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_delete_habit_deleted_habit() -> None:
    with patch("builtins.input", side_effect=[2, 1, 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_delete_habit_invalid_id_1() -> None:
    with patch("builtins.input", side_effect=[2, 0, 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_delete_habit_invalid_id_2() -> None:
    with patch("builtins.input", side_effect=[2, 100, 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_restore_habit() -> None:
    with patch("builtins.input", side_effect=[5, 1, "y",6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_restore_restored_habit() -> None:
    with patch("builtins.input", side_effect=[5, 2, 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_restore_habit_abort() -> None:
    with patch("builtins.input", side_effect=[5, 1, "n",6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_restore_invalid_id_1() -> None:
    with patch("builtins.input", side_effect=[5, 0, 5, 1, "y", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_restore_invalid_id_2() -> None:
    with patch("builtins.input", side_effect=[5, 100, 5, 1, "y", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_restore_invalid_wrong_input() -> None:
    with patch("builtins.input", side_effect=[5, "f", 5, 1, "y", 6]):
        with patch("cli.manage_menu.an.delete_restore_habit") as mock_func:
            delete_restore_habit(1)
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_reset_habit() -> None:
    with patch("builtins.input", side_effect=[4, 1, "y", 6]):
        with patch("cli.manage_menu.an.reset_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_called_once()

def test_manage_menu_reset_habit_abort() -> None:
    with patch("builtins.input", side_effect=[4, 1, "n", 6]):
        with patch("cli.manage_menu.an.reset_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_reset_habit_invalid_input() -> None:
    with patch("builtins.input", side_effect=[4, "f", "s", 6]):
        with patch("cli.manage_menu.an.reset_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_reset_habit_wrong_id_1() -> None:
    with patch("builtins.input", side_effect=[4, 0, "s", 6]):
        with patch("cli.manage_menu.an.reset_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()

def test_manage_menu_reset_habit_wrong_id_2() -> None:
    with patch("builtins.input", side_effect=[4, 100, "s", 6]):
        with patch("cli.manage_menu.an.reset_habit") as mock_func:
            mm.manage_menu()
            mock_func.assert_not_called()