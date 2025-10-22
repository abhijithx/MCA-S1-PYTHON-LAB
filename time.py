class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour      # Private attribute
        self.__minute = minute  # Private attribute
        self.__second = second  # Private attribute

    def display(self):
        print(f"Time: {self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

    # Simulated method overloading
    def set_time(self, hour=None, minute=None, second=None):
        if hour is not None:
            self.__hour = hour
        if minute is not None:
            self.__minute = minute
        if second is not None:
            self.__second = second

# Example usage
t = Time(10, 45, 30)
t.display()

# Using "overloaded" method with different number of arguments
t.set_time(12)             # Change only hour
t.display()

t.set_time(14, 20)         # Change hour and minute
t.display()

t.set_time(9, 15, 59)      # Change all
t.display()
