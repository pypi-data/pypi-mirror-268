import unittest
from math import pi
from geometry_tool import Circle, Triangle
from utils import *

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
       circle = Circle(5)
       expected_area = pi * (5 ** 2)
       self.assertEqual(circle.calc_area(), expected_area)
       
    def test_circle_perimeter(self):
       circle = Circle(5)
       expexted_perimeter = 2* pi * 5
       self.assertEqual(circle.calc_perimeter(), expexted_perimeter)
       
    def test_triangle_perimeter_1(self):
       triangle = Triangle(3, 4, 5)
       expected_perimeter = 3 + 4 + 5
       self.assertAlmostEqual(triangle.calc_perimeter(), expected_perimeter)


    def test_triangle_area_rightangled(self):
       triangle = Triangle(6, 8, 9)
       expected_area = 23.525252389719434
       self.assertAlmostEqual(triangle.calc_area(), expected_area) 

    def test_triangle_is_rightangled(self):
        triangle_rightangled = Triangle(3, 4, 5)
        triangle_not_rightangled = Triangle(6, 7, 8)
        
        self.assertTrue(triangle_rightangled.is_rightangled())
        self.assertFalse(triangle_not_rightangled.is_rightangled())


if __name__ == '__main__':
   unittest.main()
