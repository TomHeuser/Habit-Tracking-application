from OOP import habit_class
from OOP.habit_class import Habit


def test_habit__init__() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    assert habit.habit_id == 1
    assert habit.name == "test name"
    assert habit.desc == "test description"
    assert habit.active == 1
    assert habit.complete_status == 0
    assert habit.created_on == "2026-03-01"

def test_habit__get_habit_id() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    returned_data = habit.get_update_data()
    assert returned_data["habit_id"] == {1}
    assert returned_data["name"] == {"test name"}
    assert returned_data["desc"] == {"test description"}
    assert returned_data["active"] == {1}
    assert returned_data["complete_status"] == {0}
    assert returned_data["created_on"] == {"2026-03-01"}

def test_habit__from_db() -> None:
    sim_row_obj = {"habit_id": 1, "name": "test name", "desc": "test description", "active": 1, "complete_status": 0, "created_on": "2026-03-01"}
    habit = Habit.from_db(sim_row_obj)
    assert habit.habit_id == 1
    assert habit.name == "test name"
    assert habit.desc == "test description"
    assert habit.active == 1
    assert habit.complete_status == 0
    assert habit.created_on == "2026-03-01"

def test_habit__repr__() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    assert str(habit) == str(habit.__repr__())

def test_change_name() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    new_name = "new test name"
    habit.change_name(new_name)
    assert habit.name == new_name

def test_change_desc() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    new_desc = "new test description"
    habit.change_desc(new_desc)
    assert habit.desc == new_desc

