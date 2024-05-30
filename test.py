import unittest
from main import Square, Rectangle, RightAngledTriangle, Circle

class TestShapeCalculations(unittest.TestCase):
    def test_square(self):
        square = Square(5)
        self.assertAlmostEqual(square.area(), 25)
        self.assertAlmostEqual(square.perimeter(), 20)

    def test_rectangle(self):
        rectangle = Rectangle(4, 6)
        self.assertAlmostEqual(rectangle.area(), 24)
        self.assertAlmostEqual(rectangle.perimeter(), 20)

    def test_rightAngledTriangle(self):
        triangle = RightAngledTriangle(3, 4)
        self.assertAlmostEqual(triangle.area(), 6)
        self.assertAlmostEqual(triangle.perimeter(), 12)

    def test_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 9 * 3.14159, places=4)
        self.assertAlmostEqual(circle.perimeter(), 6 * 3.14159, places=4)

if __name__ == '__main__':
    unittest.main()
