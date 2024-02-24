from math_functions import *

import arithmetic
import unittest
import math
import cmath
import geometric_calculations

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(arithmetic.add(1, 2), 3)
        self.assertEqual(arithmetic.add(0, 0), 0)
        self.assertEqual(arithmetic.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(arithmetic.subtract(1, 1), 0)
        self.assertEqual(arithmetic.subtract(0, 0), 0)
        self.assertEqual(arithmetic.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(arithmetic.multiply(1, 1), 1)
        self.assertEqual(arithmetic.multiply(0, 0), 0)
        self.assertEqual(arithmetic.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(arithmetic.divide(1, 1), 1)
        self.assertEqual(arithmetic.divide(0, 1), 0)
        
        self.assertEqual(arithmetic.divide(-1, -1), 1)
    
    def test_exponent(self):
        self.assertEqual(arithmetic.power(3, 0), 1)
        self.assertEqual(arithmetic.power(0, 0), 1)
    def test_nth_root(self):
        self.assertEqual(arithmetic.n_th_root(8, 3), 2)
    
    def test_factorial(self):
        self.assertEqual(arithmetic.factorial(3), 2)
        self.assertEqual(arithmetic.factorial(0.5), math.sqrt(math.pi))
    
    def test_ln(self):
        self.assertEqual(arithmetic.ln(1), 0)
        self.assertEqual(arithmetic.ln(math.e), 1)
        self.assertEqual(arithmetic.ln(-1), cmath.log(-1, math.e))
    
    def test_sin(self):
        
        self.assertEqual(arithmetic.sin(math.pi/2), 1)
    def test_cos(self):
        self.assertEqual(arithmetic.cos(0), 1, 0.0000001)
        self.assertEqual(arithmetic.cos(math.pi), -1)
    def test_tan(self):
        self.assertEqual(arithmetic.tan(0), 0)
        self.assertEqual(arithmetic.tan(math.pi/2), 'Undefined')
    
    def test_abs(self):
        self.assertEqual(arithmetic.absolute(0), 0)
        self.assertEqual(arithmetic.absolute(-1), 1)
        self.assertEqual(arithmetic.absolute(1), 1)
    
    def test_gcd(self):
        self.assertEqual(arithmetic.gcd(10, 5), 5)
        self.assertEqual(arithmetic.gcd(10, 0), 10)
        self.assertEqual(arithmetic.gcd(0, 0), 0)


class Test_Geometric(unittest.TestCase):
    def test_area_circle(self):
        circle = geometric_calculations.Circle(5)
        self.assertEqual(circle.area(), 78.53981633974483)
    def test_circumference_circle(self):
        circle = geometric_calculations.Circle(5)
        self.assertEqual(circle.circumference(), 31.41592653589793 )
    def test_area_rectangle(self):
        rectangle = geometric_calculations.Rectangle(5, 5)
        self.assertEqual(rectangle.area(), 25)
    def test_perimeter_rectangle(self):
        rectangle = geometric_calculations.Rectangle(5, 5)
        self.assertEqual(rectangle.perimeter(), 20)
    def test_area_triangle(self):
        triangle = geometric_calculations.Triangle(5, 5, 5, 60, 60, 60)
        self.assertEqual(triangle.area(), 10.825317547305483)
    def test_perimeter_triangle(self):
        triangle = geometric_calculations.Triangle(5, 5, 5, 60, 60, 60)
        self.assertEqual(triangle.perimeter(), 15)
    def test_pythagorean_theorem(self):
        triangle = geometric_calculations.Triangle(5, 5, 0, 90, 45, 45)
        self.assertEqual(triangle.pythagorean_theoream(), math.sqrt((5**2) + (5**2)))
    def test_diagonal_rectangle(self):
        rectangle = geometric_calculations.Rectangle(5, 5)
        self.assertEqual(rectangle.diagonal(), math.sqrt((5**2) + (5**2)))
    def test_perimeter_polygon(self):
        polygon = geometric_calculations.Polygon(5, 5)
        self.assertEqual(polygon.perimeter(), 25)
    def test_area_polygon(self):
        polygon = geometric_calculations.Polygon(5, 5)
        self.assertEqual(polygon.area(), 43.01193501472418)
    def test_apothem(self):
        polygon = geometric_calculations.Polygon(5, 5)
        self.assertEqual(polygon.apothem(), (5/ (2 * math.tan(math.pi/5))))
    
    


