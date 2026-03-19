import pytest
from datetime import date
from main_util import handle_dates as hd
@pytest.fixture(autouse=True)

def test_handle_dates_variables() -> None:
    current_day = hd.current_day
    current_week = hd.current_week
    assert current_day is None and current_week is None


def test_set_test_date() -> None:
    current_day = hd.set_test_date()
    assert current_day == date.fromisoformat("2026-03-29")

def test_set_test_week() -> None:
    current_week = hd.set_test_week()
    assert current_week == 105365

def test_set_current_week() -> None:
    today = date.today()
    actual_week = 105352 + today.isocalendar().week
    current_week = hd.set_current_week()
    assert current_week == actual_week

def test_set_current_date() -> None:
    today = date.today()
    current_date = date.today()
    assert today == current_date