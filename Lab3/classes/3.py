import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = float(input("x1: "))
y1 = float(input("y1: "))
point1 = Point(x1, y1)

x2 = float(input("x2: "))
y2 = float(input("y2: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2)
print({distance})
