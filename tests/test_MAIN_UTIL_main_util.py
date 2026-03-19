from main_util import main_util as mutil

def test_return_to_main() -> None:
    returned_value = mutil.return_to_main()
    assert returned_value == "BACK"