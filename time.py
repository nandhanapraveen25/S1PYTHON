class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.normalize()

    def normalize(self):
        if self.__second >= 60:
            self.__minute += self.__second // 60
            self.__second = self.__second % 60

        if self.__minute >= 60:
            self.__hour += self.__minute // 60
            self.__minute = self.__minute % 60
    def __add__(self, other):
        new_hour = self.__hour + other.__hour
        new_minute = self.__minute + other.__minute
        new_second = self.__second + other.__second
        return Time(new_hour, new_minute, new_second)
    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")
print("Enter Time 1")
h1 = int(input("Hour: "))
m1 = int(input("Minute: "))
s1 = int(input("Second: "))
t1 = Time(h1, m1, s1)
print("\nEnter Time 2")
h2 = int(input("Hour: "))
m2 = int(input("Minute: "))
s2 = int(input("Second: "))
t2 = Time(h2, m2, s2)
print("\nTime 1: ", end="")
t1.display()
print("Time 2: ", end="")
t2.display()
t3 = t1 + t2
print("Sum of Time 1 and Time 2: ", end="")
t3.display()
