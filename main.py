import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class RightAngledTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming it's a right-angled triangle
        hypotenuse = (self.base ** 2 + self.height ** 2) ** 0.5
        return self.base + self.height + hypotenuse

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def calculate_shape():
    print("Shape Area and Perimeter Calculator")
    print("-----------------------------------")
    print("Available Shapes: Square, Rectangle, RightAngledTriangle, Circle")
    user_shape = input("Enter the name of the shape: ").lower()

    if user_shape == "square":
        top_right = input("Enter the coordinates of the top right corner (format: x y): ").split()
        side = float(input("Enter the length of a side: "))
        shape = Square(side)
    elif user_shape == "rectangle":
        top_right = input("Enter the coordinates of the top right corner (format: x y): ").split()
        bottom_left = input("Enter the coordinates of the bottom left corner (format: x y): ").split()
        length = abs(float(top_right[0]) - float(bottom_left[0]))
        width = abs(float(top_right[1]) - float(bottom_left[1]))
        shape = Rectangle(length, width)
    elif user_shape == "rightAngledTriangle":
        point1 = input("Enter the coordinates of the first point (format: x y): ").split()
        point2 = input("Enter the coordinates of the second point (format: x y): ").split()
        point3 = input("Enter the coordinates of the third point (format: x y): ").split()
        base = abs(float(point2[0]) - float(point1[0]))
        height = abs(float(point3[1]) - float(point1[1]))
        shape = RightAngledTriangle(base, height)
    elif user_shape == "circle":
        center = input("Enter the coordinates of the center (format: x y): ").split()
        radius = float(input("Enter the radius of the circle: "))
        shape = Circle(radius)
    else:
        print("Invalid shape! Please choose from Square, Rectangle, RightAngledTriangle, or Circle.")
        return

    print(f"Area of the {user_shape.capitalize()}: {shape.area()}")
    print(f"Perimeter of the {user_shape.capitalize()}: {shape.perimeter()}")


def main():
    calculate_shape()

    while True:
        choice = input("Would you like to calculate the area of another shape? (yes/no): ").lower()
        if choice != "yes":
            break
    calculate_shape()