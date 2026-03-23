import sys
import sqlite3
import pytest
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from main_util.handle_dates import set_test_date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_path = os.path.join(BASE_DIR, "src", "database",'database.db')
JSON_PATH = os.path.join(BASE_DIR, "src", "database", "initial_data.json")
connection = sqlite3.connect(DB_path)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()



@pytest.fixture(autouse=True)
def reset_db():

    current_day = None
    set_test_date()

    yield
    cursor.execute("DROP TABLE IF EXISTS habit")
    cursor.execute("DROP TABLE IF EXISTS history")
    connection.commit()
    habit_table_create = """CREATE TABLE habit \
                            ( \
                                habit_id        INTEGER PRIMARY KEY AUTOINCREMENT, \
                                name            TEXT, \
                                desc            TEXT, \
                                active          INTEGER, \
                                interval        INTEGER, \
                                complete_status INTEGER, \
                                created_on      TEXT, \
                                streak_status   INTEGER, \
                                streak_count    INTEGER \
                            )"""
    cursor.execute(habit_table_create)
    connection.commit()
    history_table_create = """CREATE TABLE history \
                              ( \
                                  history_id      INTEGER PRIMARY KEY AUTOINCREMENT, \
                                  habit_id        INTEGER NOT NULL, \
                                  date            TEXT, \
                                  complete_status INTEGER, \
                                  streak_status   INTEGER, \
                                  streak_count    INTEGER, \
                                  FOREIGN KEY (habit_id) REFERENCES habit (habit_id) \
                              )"""
    cursor.execute(history_table_create)
    connection.commit()
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
    data.sort(key=lambda habit: habit["interval"])
    for habit in data:
        habit_data = {a: b for a, b in habit.items() if a != "history"}
        history_data = habit.get("history", [])
        cursor.execute(
            "INSERT INTO habit (name, desc, active, interval, complete_status, created_on, streak_status, streak_count) VALUES (?,?,?,?,?,?,?,?)",
            (
                habit_data["name"],
                habit_data["desc"],
                habit_data["active"],
                habit_data["interval"],
                habit_data["complete_status"],
                habit_data["created_on"],
                habit_data["streak_status"],
                habit_data["streak_count"]
            )
        )
        habit_id = cursor.lastrowid
        for entry in history_data:
            cursor.execute(
                "INSERT INTO history (habit_id, date, complete_status, streak_status, streak_count) VALUES (?,?,?,?,?)",
                (
                    habit_id,
                    entry["date"],
                    entry["complete_status"],
                    entry["streak_status"],
                    entry["streak_count"]
                )
            )
    connection.commit()


