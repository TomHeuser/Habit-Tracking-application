from database import db

def id_names():
    names = db.fetch_active_names()
    for habit in names:
        # print(type(names))
        # print(type(names[0]))
        habit_id = habit["habit_id"]
        habit_name = habit["name"]
        print(f"{habit_id} {habit_name}")