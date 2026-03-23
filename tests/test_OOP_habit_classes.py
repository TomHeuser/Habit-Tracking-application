from OOP import habit_class
from OOP.habit_class import Habit, TimeHabit

# test basic habits
def test_habit__init__() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    assert habit.habit_id == 1
    assert habit.name == "test name"
    assert habit.desc == "test description"
    assert habit.active == 1
    assert habit.complete_status == 0
    assert habit.created_on == "2026-03-01"

def test_habit_get_habit_id() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    returned_data = habit.get_update_data()
    assert returned_data["habit_id"] == {1}
    assert returned_data["name"] == {"test name"}
    assert returned_data["desc"] == {"test description"}
    assert returned_data["active"] == {1}
    assert returned_data["complete_status"] == {0}
    assert returned_data["created_on"] == {"2026-03-01"}

def test_habit_from_db() -> None:
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

def test_habit_change_name() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    new_name = "new test name"
    habit.change_name(new_name)
    assert habit.name == new_name

def test_habit_change_desc() -> None:
    habit = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    new_desc = "new test description"
    habit.change_desc(new_desc)
    assert habit.desc == new_desc

def test_habit_change_active() -> None:
    habit1 = Habit(1, "test name", "test description", 1, 1, "2026-03-01")
    habit2 = Habit(1, "test name", "test description", 0, 0, "2026-03-01")
    habit1.change_active()
    habit2.change_active()
    assert habit1.active == 0
    assert habit1.complete_status == 0
    assert habit2.active == 1

def test_habit_change_complete_status() -> None:
    habit1 = Habit(1, "test name", "test description", 1, 1, "2026-03-01")
    habit2 = Habit(1, "test name", "test description", 1, 0, "2026-03-01")
    habit1.change_complete_status()
    habit2.change_complete_status()
    assert habit1.complete_status == 0
    assert habit2.complete_status == 1

#test time habits
def test_timehabit__init__() -> None:
    timehabit = TimeHabit(1, "test name", "test description", 1, 1, 1,"2026-03-01", 1,28)

    assert timehabit.habit_id == 1
    assert timehabit.name == "test name"
    assert timehabit.desc == "test description"
    assert timehabit.active == 1
    assert timehabit.interval == 1
    assert timehabit.complete_status == 1
    assert timehabit.created_on == "2026-03-01"
    assert timehabit.streak_status == 1
    assert timehabit.streak_count == 28

def test_timehabit_from_db() -> None:
    sim_row_obj = {"habit_id": 1, "name": "test name", "desc": "test description", "active": 1, "interval": 1,
                   "complete_status": 0, "created_on": "2026-03-01", "streak_status": 1, "streak_count": 28}
    timehabit = TimeHabit.from_db(sim_row_obj)
    assert timehabit.habit_id == 1
    assert timehabit.name == "test name"
    assert timehabit.desc == "test description"
    assert timehabit.active == 1
    assert timehabit.complete_status == 0
    assert timehabit.created_on == "2026-03-01"
    assert timehabit.streak_status == 1
    assert timehabit.streak_count == 28

def test_timehabit__repr__() -> None:
    timehabit = TimeHabit(1, "test name", "test description", 1, 1, 1,"2026-03-01", 1,28)
    assert str(timehabit) == str(timehabit.__repr__())

def test_timehabit_change_interval() -> None:
    timehabit = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    timehabit.change_interval(7)
    assert timehabit.interval == 7
    assert timehabit.streak_status == 0
    assert timehabit.streak_count == 0

def test_timehabit_change_active() -> None:
    timehabit1 = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    timehabit2 = TimeHabit(1, "test name", "test description", 0, 1, 1, "2026-03-01", 1, 28)
    timehabit3 = TimeHabit(1, "test name", "test description", 4, 1, 1, "2026-03-01", 1, 28)
    timehabit1.change_active()
    timehabit2.change_active()
    timehabit3.change_active()
    assert timehabit1.active == 0
    assert timehabit1.complete_status == 0
    assert timehabit1.streak_status == 0
    assert timehabit1.streak_count == 0
    assert timehabit2.active == 1
    assert timehabit2.complete_status == 1
    assert timehabit3.active == 1
    assert timehabit3.complete_status == 1

def test_timehabit_reset() -> None:
    timehabit1 = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    timehabit1.reset()
    assert timehabit1.complete_status == 0
    assert timehabit1.streak_status == 0
    assert timehabit1.streak_count == 0

def test_timehabit_get_update_data() -> None:
    timehabit1 = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    update_data = timehabit1.get_update_data()
    assert update_data["habit_id"] == 1
    assert update_data["name"] == "test name"
    assert update_data["desc"] == "test description"
    assert update_data["active"] == 1
    assert update_data["interval"] == 1
    assert update_data["complete_status"] == 1
    assert update_data["created_on"] == "2026-03-01"
    assert update_data["streak_status"] == 1
    assert update_data["streak_count"] == 28

def test_timehabit_get_history_data() -> None:
    timehabit1 = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    new_history_data = timehabit1.get_history_data()
    assert new_history_data["habit_id"] == 1
    assert new_history_data["date"].isoformat() == "2026-03-29"
    assert new_history_data["complete_status"] == 1
    assert new_history_data["streak_status"] == 1
    assert new_history_data["streak_count"] == 28

def test_timehabit_change_comlete_status() -> None:
    timehabit1 = TimeHabit(1, "test name", "test description", 1, 1, 1, "2026-03-01", 1, 28)
    timehabit1.change_complete_status()
    assert timehabit1.complete_status == 0
    assert timehabit1.streak_status == 0
    assert timehabit1.streak_count == 27
    timehabit1.change_complete_status()
    assert timehabit1.complete_status == 1
    assert timehabit1.streak_status == 1
    assert timehabit1.streak_count == 28
    timehabit2 = TimeHabit(1, "test name", "test description", 1, 1, 3, "2026-03-01", 1, 28)
    timehabit2.change_complete_status()
    assert timehabit2.complete_status == 0
    assert timehabit2.streak_status == 1
    assert timehabit2.streak_count == 28
    timehabit2.change_complete_status()
    assert timehabit2.complete_status == 1
    assert timehabit2.streak_status == 1
    assert timehabit2.streak_count == 29

