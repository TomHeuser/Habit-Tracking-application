from database import db as db
from OOP.habit_class import TimeHabit
from OOP.history_class import HabitHistory
import sqlite3

def test_get_name_for_id() -> None:
    returned_value = db.get_name_for_id(1)
    assert returned_value == "Drink Water"

def test_get_name_for_id_none() -> None:
    returned_value = db.get_name_for_id(100)
    assert returned_value is None

def test_get_interval_daily() -> None:
    returned_value = db.get_interval(1)
    assert returned_value == 1

def test_get_interval_weekly() -> None:
    returned_value = db.get_interval(3)
    assert returned_value == 7

def test_get_interval_none() -> None:
    returned_value = db.get_interval(100)
    assert returned_value is None

def test_get_creation_date() -> None:
    returned_value = db.get_creation_date(1)
    assert returned_value == "2026-03-01"


def test_get_creation_date_none() -> None:
    returned_value = db.get_creation_date(100)
    assert returned_value is None

def test_get_max_id() -> None:
    returned_value = db.get_max_id()
    assert returned_value == 5
## test return 0 if no habits for above?

def test_fetch_all_habit_rows() -> None:
    returned_value = db.fetch_all_habit_rows()
    assert len(returned_value) == 5

def test_fetch_all_inactive() -> None:
    returned_value = db.fetch_all_inactive()
    assert len(returned_value) == 0

def test_fetch_active_names() -> None:
    returned_value = db.fetch_active_names()
    assert returned_value == [{'habit_id': 1, 'name': 'Drink Water'}, {'habit_id': 2, 'name': 'Walking'}, {'habit_id': 3, 'name': 'Cleaning'},
                              {'habit_id': 4, 'name': 'Go swimming'}, {'habit_id': 5, 'name': 'Check finances'}]

def test_fetch_active_ids() -> None:
    returned_value = db.fetch_active_ids()
    assert returned_value == [1, 2, 3, 4, 5]

def test_fetch_inactive_names() -> None:
    returned_value = db.fetch_inactive_names()
    assert returned_value == []

def test_fetch_names() -> None:
    returned_value = db.fetch_names()
    assert returned_value == [{'habit_id': 1, 'name': 'Drink Water'}, {'habit_id': 2, 'name': 'Walking'}, {'habit_id': 3, 'name': 'Cleaning'},
                              {'habit_id': 4, 'name': 'Go swimming'}, {'habit_id': 5, 'name': 'Check finances'}]

def test_fetch_single_habit_details() -> None:
    returned_value = db.fetch_single_habit_details(1)
    assert returned_value == {'habit_id': 1, 'name': 'Drink Water', 'desc': 'Drink two liters of water each day', 'active': 1, 'interval': 1,
                              'complete_status': 0, 'created_on': '2026-03-01', 'streak_status': 1, 'streak_count': 28}

def test_fetch_single_habit_details_none() -> None:
    retuned_value = db.fetch_single_habit_details(100)
    assert retuned_value is None

## test what happens if there are multiple equals
## also what happens if all streaks are 0?
def test_fetch_highest_current_streak() -> None:
    returned_value = db.fetch_highest_current_streak()
    assert returned_value == [{'habit_id': 1, 'name': 'Drink Water', 'streak_count': 28}]


def test_fetch_highest_history_streak() -> None:
    returned_value = db.fetch_highest_history_streak()
    assert returned_value == [{'habit_id': 1, 'streak_count': 28}]

def test_fetch_all_history_for_habit() -> None:
    returned_value = db.fetch_all_history_for_habit(5)
    assert returned_value == [{'date': '2026-03-04', 'complete_status': 1, 'streak_status': 0, 'streak_count': 1}]

def test_fetch_all_history_for_habit_len_daily() -> None:
    returned_value = db.fetch_all_history_for_habit(1)
    assert len(returned_value) == 28

def test_fetch_all_history_for_habit_len_weekly() -> None:
    returned_value = db.fetch_all_history_for_habit(3)
    assert len(returned_value) == 4

def test_load_all_time_habits() -> None:
    returned_value = db.load_all_time_habits()
    assert len(returned_value) == 5
    assert isinstance(returned_value[0], TimeHabit)
    assert returned_value[0].habit_id == 1
    assert returned_value[0].name == 'Drink Water'
    assert returned_value[0].desc == 'Drink two liters of water each day'
    assert returned_value[0].active == 1
    assert returned_value[0].interval == 1
    assert returned_value[0].complete_status == 0
    assert returned_value[0].created_on == '2026-03-01'
    assert returned_value[0].streak_status == 1
    assert returned_value[0].streak_count == 28
    assert isinstance(returned_value[1], TimeHabit)
    assert isinstance(returned_value[3], TimeHabit)
    assert isinstance(returned_value[4], TimeHabit)

def test_load_single_time_habit() -> None:
    returned_value = db.load_single_time_habit(1)
    assert isinstance(returned_value, TimeHabit)
    assert returned_value.habit_id == 1
    assert returned_value.name == 'Drink Water'
    assert returned_value.desc == 'Drink two liters of water each day'
    assert returned_value.active == 1
    assert returned_value.interval == 1
    assert returned_value.complete_status == 0
    assert returned_value.created_on == '2026-03-01'
    assert returned_value.streak_status == 1
    assert returned_value.streak_count == 28

def test_update_single_row() -> None:
    update_data = {"habit_id": 1, "name": "Drink","desc": "2L", "active": 0,
                        "complete_status": 0, "interval": 7,
                        "created_on": "2026-03-01", "streak_status": 0, "streak_count": 0}
    db.update_single_row(update_data)
    returned_value = db.load_single_time_habit(1)
    assert returned_value.habit_id == 1
    assert returned_value.name == 'Drink'
    assert returned_value.desc == '2L'
    assert returned_value.active == 0
    assert returned_value.complete_status == 0
    assert returned_value.interval == 7
    assert returned_value.created_on == '2026-03-01'
    assert returned_value.streak_status == 0
    assert returned_value.streak_count == 0

def test_append_single_row() -> None:
    new_habit_data = {"name": "TEST","desc": "test", "active": 1,
                        "complete_status": 0, "interval": 1,
                        "created_on": "2026-03-29", "streak_status": 0, "streak_count": 0}
    db.append_single_row(new_habit_data)
    returned_value = db.load_single_time_habit(6)
    assert returned_value.habit_id == 6
    assert returned_value.name == 'TEST'
    assert returned_value.desc == 'test'
    assert returned_value.active == 1
    assert returned_value.complete_status == 0
    assert returned_value.interval == 1
    assert returned_value.created_on == '2026-03-29'
    assert returned_value.streak_status == 0
    assert returned_value.streak_count == 0

def test_fetch_single_habit_history_all() -> None:
    returned_value = db.fetch_single_habit_history_all(1)
    assert len(returned_value) == 28
    assert isinstance(returned_value[0], sqlite3.Row)
    assert isinstance(returned_value, list)
    returned_value = db.fetch_single_habit_history_all(3)
    assert len(returned_value) == 4
    assert isinstance(returned_value[0], sqlite3.Row)
    assert isinstance(returned_value, list)

def test_fetch_single_habit_history_recent() -> None:
    returned_value = db.fetch_single_habit_history_recent(1)
    assert len(returned_value) == 6
    assert isinstance(returned_value, sqlite3.Row)
    assert returned_value["history_id"] == 28
    assert returned_value["habit_id"] == 1
    assert returned_value["date"] == "2026-03-28"
    assert returned_value["complete_status"] == 1
    assert returned_value["streak_status"] == 1
    assert returned_value["streak_count"] == 28
    returned_value = db.fetch_single_habit_history_recent(5)
    assert len(returned_value) == 6
    assert isinstance(returned_value, sqlite3.Row)
    assert returned_value["history_id"] == 64
    assert returned_value["habit_id"] == 5
    assert returned_value["date"] == "2026-03-04"
    assert returned_value["complete_status"] == 1
    assert returned_value["streak_status"] == 0
    assert returned_value["streak_count"] == 1

def test_load_single_history_all() -> None:
    returned_value = db.load_single_history_all(1)
    assert len(returned_value) == 28
    assert isinstance(returned_value[0], HabitHistory)
    assert isinstance(returned_value, list)

def test_load_single_history_recent() -> None:
    retuned_value = db.load_single_history_recent(1)
    assert isinstance(retuned_value, HabitHistory)
    assert retuned_value.habit_id == 1
    assert retuned_value.date == "2026-03-28"
    assert retuned_value.complete_status == 1
    assert retuned_value.streak_status == 1
    assert retuned_value.streak_count == 28

def test_append_history() -> None:
    new_habit_data = {"habit_id": 1,"date": "2026-03-29", "complete_status": 1, "streak_status": 1, "streak_count": 29}
    db.append_history(new_habit_data)
    retuned_value = db.load_single_history_recent(1)
    assert isinstance(retuned_value, HabitHistory)
    assert retuned_value.habit_id == 1
    assert retuned_value.date == "2026-03-29"
    assert retuned_value.complete_status == 1
    assert retuned_value.streak_status == 1
    assert retuned_value.streak_count == 29

def test_check_existing_history_date_true() -> None:
    habit_id = 1
    iso_today = "2026-03-28"
    returned_value = db.check_existing_history_date(habit_id, iso_today)
    assert returned_value == True

def test_check_existing_history_date_false() -> None:
    habit_id = 1
    second_iso_today = "2026-04-29"
    returned_value = db.check_existing_history_date(habit_id, second_iso_today)
    assert returned_value == False

def test_get_daily_id_list() -> None:
    retuned_value = db.get_daily_id_list()
    assert retuned_value == [1,2]

def test_get_weekly_id_list() -> None:
    retuned_value = db.get_weekly_id_list()
    assert retuned_value == [3,4,5]

def get_manual_id_list() -> None:
    retuned_value = db.get_manual_id_list()
    assert retuned_value == []

def test_get_last_entry() -> None:
    returned_value = db.get_last_entry(1)
    assert returned_value == "2026-03-28"
    returned_value = db.get_last_entry(2)
    assert returned_value == "2026-03-28"
    returned_value = db.get_last_entry(3)
    assert returned_value == "2026-03-28"
    returned_value = db.get_last_entry(5)
    assert returned_value == "2026-03-04"

def test_startup_habit_incomplete() -> None:
    db.startup_habit_incomplete(1)
    returned_value = db.fetch_single_habit_details(1)
    assert returned_value["complete_status"] == 0

def test_startup_habit_reset() -> None:
    db.startup_habit_reset(1)
    returned_value = db.fetch_single_habit_details(1)
    assert returned_value["complete_status"] == 0
    assert returned_value["streak_status"] == 0
    assert returned_value["streak_count"] == 0