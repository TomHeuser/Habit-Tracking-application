## history class tree

##lvl1: History superclass
class HabitHistory:
    """Habit history class that is used to create habit history objects that hold habit_id, date, complete_status, streak_status and streak_count"""
    def __init__(self, habit_id, complete_status, streak_status, streak_count, date):
        self.habit_id = habit_id
        self.date = date
        self.complete_status = complete_status
        self.streak_status = streak_status
        self.streak_count = streak_count

    @classmethod
    def from_db(cls, row):
        """takes the contents from a table row and then returns the values necessary for __init__ to create a new Habit object"""
        return cls(habit_id=row["habit_id"], date=row["date"], complete_status=row["complete_status"], streak_status=row["streak_status"], streak_count=row["streak_count"])

    def __repr__(self):
        """manages how attributes are returned"""
        return f"HabitHistory(habit_id={self.habit_id},date={self.date}, complete_status={self.complete_status}, streak_status={self.streak_status}, streak_count={self.streak_count})"