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
