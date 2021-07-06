class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        if self.seconds + 1 == 60:
            if self.minutes + 1 == 60:
                if self.hours + 1 == 24:
                    return f"00:00:00"
                return f'{self.hours+1:02d}:00:00'
            return f"{self.hours:02d}:{self.minutes+1:02d}:00"
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds+1:02d}"