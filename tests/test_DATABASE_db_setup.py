import pytest
import sqlite3
from database.db import cursor

from database import db_setup as setup

def test_flush_habit_table() -> None:
    setup.flush_habit_table()
    with pytest.raises(sqlite3.OperationalError):
        cursor.execute("SELECT * FROM habit")

def test_flush_history_table() -> None:
    setup.flush_history_table()
    with pytest.raises(sqlite3.OperationalError):
        cursor.execute("SELECT * FROM history")

def test_setup_habit_table() -> None:
    with pytest.raises(sqlite3.OperationalError):
        setup.setup_habit_table()
    setup.flush_habit_table()
    setup.setup_habit_table()
    with pytest.raises(sqlite3.OperationalError):
        setup.setup_habit_table()

def test_setup_history_table() -> None:
    with pytest.raises(sqlite3.OperationalError):
        setup.setup_history_table()
    setup.flush_history_table()
    setup.setup_history_table()
    with pytest.raises(sqlite3.OperationalError):
        setup.setup_history_table()

def test_seed_predefined_habits() -> None:
    setup.flush_habit_table()
    setup.flush_history_table()
    setup.setup_habit_table()
    setup.setup_history_table()
    setup.seed_predefined_habits()

def test_database_setup_true() -> None:
    returned_value = setup.database_startup()
    assert returned_value is False

def test_database_setup_false() -> None:
    setup.flush_habit_table()
    setup.flush_history_table()
    returned_value = setup.database_startup()
    assert returned_value is True



