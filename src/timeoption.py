from datetime import datetime


class Time:
    """Processes the time based options"""

    def __init__(self, opt_time):
        self.opt_time = opt_time

    def isint(self):
        """Checks the given span valid or not"""
        num = self.opt_time
        if "-" in num or "+" in num:
            return len(num) >= 2 and num[1:].isdigit()
        return num.isdigit()

    def compare(self, a, b):
        """Sub funcion for 'compare_time' used to compare option and data"""
        if "-" in b:
            return a <= abs(int(b))
        elif "+" in b:
            return a >= int(b)
        return a == int(b)

    def compare_time(self, time):
        """Compares and matches the file with provided time"""
        if not self.isint():
            print("Invalid time provided")
            exit(1)
        current_date = datetime.now()
        timestamp_str = datetime.fromtimestamp(time)
        diff = current_date-timestamp_str
        return self.compare(diff.days, self.opt_time)
