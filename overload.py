class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()

l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))
r1 = Rectangle(l1, w1)
l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))
r2 = Rectangle(l2, w2)
print("\nArea of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())
if r1 < r2:
    print("Rectangle 2 has a larger area.")
elif r1 > r2:
    print("Rectangle 1 has a larger area.")
else:
    print("Both rectangles have the same area.")
