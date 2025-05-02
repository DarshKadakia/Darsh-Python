class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"
