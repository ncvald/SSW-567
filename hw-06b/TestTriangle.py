# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Valid triangle classifications
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', 'All sides equal should be Equilateral')

    def test_isosceles_cases(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    # Right triangles (Pythagorean)
    def test_right_triangle_345(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def test_right_triangle_543(self):
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right')

    def test_right_triangle_large(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')

    # Invalid triangles
    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(2, 3, 5), 'NotATriangle')

    # Invalid inputs
    def test_invalid_input_zero(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput')

    def test_invalid_input_negative(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput')

    def test_invalid_input_too_large(self):
        self.assertEqual(classifyTriangle(201, 5, 5), 'InvalidInput')

    def test_invalid_type(self):
        self.assertEqual(classifyTriangle("a", 2, 3), 'InvalidInput')
        self.assertEqual(classifyTriangle(3, 4.5, 5), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()
