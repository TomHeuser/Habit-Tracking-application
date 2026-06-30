from cli import cli_util as cli
from unittest.mock import patch

def test_submenu_choice() -> None:
    with patch("builtins.input", return_value=1):
        result = cli.submenu_choice()
        assert result == 1
    with patch("builtins.input", return_value=2):
        result = cli.submenu_choice()
        assert result == 2
    with patch("builtins.input", return_value=3):
        result = cli.submenu_choice()
        assert result == 3
    with patch("builtins.input", return_value=4):
        result = cli.submenu_choice()
        assert result == 4
    with patch("builtins.input", side_effect=["f", 2]):
        result = cli.submenu_choice()
        assert result == 2

def test_exit_confirmation_choice() -> None:
    with patch("builtins.input", return_value="y"):
        result = cli.exit_confirmation_choice()
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.exit_confirmation_choice()
        assert result == "n"
    #with patch("builtins.input", side_effect=[1, "y"]):
        #result = cli.exit_confirmation_choice()
        #assert result == "y"

def test_new_name_input()-> None:
    old_name = "old name"
    with patch("builtins.input", return_value="new_name"):
        result = cli.new_name_input(old_name)
        assert result == "new_name"

def test_confirm_new_name_input()-> None:
    old_name = "old name"
    new_name = "new name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_new_name(old_name, new_name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_new_name(old_name, new_name)
        assert result == "n"
    with patch("builtins.input", return_value=1):
        result = cli.confirm_new_name(old_name, new_name)
        assert result == 1
    with patch("builtins.input", return_value="a"):
        result = cli.confirm_new_name(old_name, new_name)
        assert result == "a"
    with patch("builtins.input", return_value="word"):
        result = cli.confirm_new_name(old_name, new_name)
        assert result == "word"

def test_new_desc_input()-> None:
    old_desc = "old description"
    with patch("builtins.input", return_value="new description"):
        result = cli.new_desc_input(old_desc)
        assert result == "new description"

def test_confirm_new_desc()-> None:
    new_desc = "new description"
    name = "name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_new_desc(new_desc, name)
        assert result == "y"
    with patch ("builtins.input", return_value="n"):
        result = cli.confirm_new_desc(new_desc, name)
        assert result == "n"

def test_confirm_delete() -> None:
    name = "name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_delete(name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_delete(name)
        assert result == "n"

def test_confirm_restore() -> None:
    name = "name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_restore(name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_restore(name)
        assert result == "n"

def test_confirm_incomplete() -> None:
    name = "name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_incomplete(name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_incomplete(name)
        assert result == "n"

def test_confirm_complete() -> None:
    name = "name"
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_complete(name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_complete(name)
        assert result == "n"

def test_predefined_interval_choice() -> None:
    with patch("builtins.input", return_value=1):
        result = cli.predefined_interval_choice()
        assert result == 1
    with patch("builtins.input", return_value=2):
        result = cli.predefined_interval_choice()
        assert result == 2

def test_manual_interval_input() -> None:
    with patch("builtins.input", return_value="1"):
        result = cli.manual_interval_input()
        assert result == 1
    with patch("builtins.input", return_value="2"):
        result = cli.manual_interval_input()
        assert result == 2
    with patch("builtins.input", side_effects=["f", 1]):
        result = cli.manual_interval_input()
        assert result == 1
    with patch("builtins.input", side_effects=[[],1]):
        result = cli.manual_interval_input()
        assert result == 1

def test_interval_change_type_choice() -> None:
    with patch("builtins.input", return_value=1):
        result = cli.interval_change_type_choice()
        assert result == 1
    with patch("builtins.input", return_value=2):
        result = cli.interval_change_type_choice()
        assert result == 2

def test_confirm_interval_change() -> None:
    name = "name"
    old_interval = 1
    new_interval = 7
    with patch("builtins.input", return_value="y"):
        result = cli.confirm_interval_change(name, old_interval, new_interval)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.confirm_interval_change(name, old_interval, new_interval)
        assert result == "n"

def test_operation_mode() -> None:
    with patch("builtins.input", side_effect=['t','t']):
        result = cli.operation_mode()
        assert result == "t"
    with patch("builtins.input", return_value=1):
        result = cli.operation_mode()
        assert result == 0
    with patch("builtins.input", return_value=[1,2,3]):
        result = cli.operation_mode()
        assert result == 0

def test_get_new_name_input() -> None:
    with patch("builtins.input", return_value="new name"):
        result = cli.get_new_name_input()
        assert result == "new name"

def test_get_new_name_confirm_input() -> None:
    new_habit_name = "new name"
    with patch("builtins.input", return_value="y"):
        result = cli.get_new_name_confirm_input(new_habit_name)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.get_new_name_confirm_input(new_habit_name)
        assert result == "n"

def test_get_new_desc_input() -> None:
    with patch("builtins.input", return_value="new desc"):
        result = cli.get_new_desc_input()
        assert result == "new desc"

def test_get_new_desc_confirm_input() -> None:
    new_habit_desc = "new desc"
    with patch("builtins.input", return_value="y"):
        result = cli.get_new_desc_confirm_input(new_habit_desc)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.get_new_desc_confirm_input(new_habit_desc)
        assert result == "n"

def test_get_interval_approach_input() -> None:
    with patch("builtins.input", return_value=1):
        result = cli.get_interval_approach_input()
        assert result == 1
    with patch("builtins.input", return_value=2):
        result = cli.get_interval_approach_input()
        assert result == 2

def test_get_interval_approach_confirm() -> None:
    new_interval = 1
    with patch("builtins.input", return_value="y"):
        result = cli.get_interval_approach_confirm(new_interval)
        assert result == "y"
    with patch("builtins.input", return_value="n"):
        result = cli.get_interval_approach_confirm(new_interval)
        assert result == "n"
