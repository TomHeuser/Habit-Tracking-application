from OOP import history_class
from OOP.history_class import HabitHistory


def test_habithistory__init__() -> None:
    history_habit = HabitHistory(1,1,1,28,"2026-03-29")
    assert history_habit.habit_id == 1
    assert history_habit.complete_status == 1
    assert history_habit.streak_status == 1
    assert history_habit.streak_count == 28
    assert history_habit.date == "2026-03-29"

def test_habithistory__repr__() -> None:
    history_habit = HabitHistory(1, 1, 1, 28, "2026-03-29")
    returned_data = history_habit.__repr__()
    assert returned_data == history_habit.__repr__()

def test_habithistory_from_db() -> None:
    sim_row_obj = {"habit_id": 1, "date": "2026-03-29", "complete_status": 1,
                   "streak_status": 1, "streak_count": 28}
    history_habit = HabitHistory.from_db(sim_row_obj)
    assert history_habit.habit_id == 1
    assert history_habit.date == "2026-03-29"
    assert history_habit.complete_status == 1
    assert history_habit.streak_status == 1
    assert history_habit.streak_count == 28