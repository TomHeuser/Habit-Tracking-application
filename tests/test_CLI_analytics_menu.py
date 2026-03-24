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

#def test_analytics_menu_calls_list_of_active_habits() -> None:
        #with patch("builtins.input",  side_effect=[1, KeyboardInterrupt]):
            #with patch("cli.analytics_menu.an.get_list_of_active_habits") as mock_func:
                #with patch("cli.analytics_menu.step"):
                    #anm.analytics_menu()
                    #mock_func.assert_called_once()
