# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify
triangles
@author: jrr
@author: rk
"""
def classifyTriangle(a, b, c):
    """Classify a triangle based on side lengths a, b, c."""
    # Input validation
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Right triangle
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    # Type
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isoceles'
    else:
        return 'Scalene'
