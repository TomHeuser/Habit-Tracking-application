import pytest
from datetime import date
from main_util import handle_dates as hd
@pytest.fixture(autouse=True)



def test_set_test_date() -> None:
    hd.set_test_date()
    assert hd.current_day == date.fromisoformat("2026-03-29")

def test_set_test_week() -> None:
    hd.set_test_week()
    assert hd.current_week == 105365

def test_set_current_week() -> None:
    today = date.today()
    actual_week = 105352 + today.isocalendar().week
    hd.set_current_week()
    assert hd.current_week == actual_week

def test_set_current_date() -> None:
    today = date.today()
    hd.set_current_date()
    #print(hd.current_day)
    assert today == hd.current_day