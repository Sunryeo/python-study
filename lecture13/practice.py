# Practice 1
# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.gender == other.gender
#
#
# if __name__ == '__main__':
#     p1 = Person('James', 'Male')
#     p2 = Person('Nana', 'Female')
#
#     if p1 == p2:
#         print("Same gender!")
#     else:
#         print("Different gender!")
import math


# Practice 2
import math
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

if __name__ == '__main__':
    point1 = Coordinate(0, 0)
    point2 = Coordinate(10, 10)

    print(point1)
    print(point2)

    dist = point1 + point2
    print(f"Distance: {dist}")