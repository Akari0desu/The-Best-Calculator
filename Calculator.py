# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:01:27 2025

@author: computershop.mn
"""

# Importing math for the use of mathematical functions
import math

class Calculator:

    # Function for addition
    @staticmethod
    def add(a, b):
        return a + b

    # Function for subtraction
    @staticmethod
    def subtract(a, b):
        return a - b

    # Function for multiplication
    @staticmethod
    def multiply(a, b):
        return a * b

    # Function for division
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    # Function for sine calculation (rounded)
    @staticmethod
    def sine(a):
        return round(math.sin(math.radians(a)), 10)

    # Function for cosine calculation (rounded)
    @staticmethod
    def cosine(a):
        return round(math.cos(math.radians(a)), 10)

    # Function for tangent calculation (rounded)
    @staticmethod
    def tangent(a):
        return round(math.tan(math.radians(a)), 10)

    # Function for arcsin calculation (inverse of sine, rounded)
    @staticmethod
    def arcsin(a):
        if -1 <= a <= 1:
            return round(math.degrees(math.asin(a)), 10)
        return "Error: Input out of range (-1 to 1)"

    # Function for arccos calculation (inverse of cosine, rounded)
    @staticmethod
    def arccos(a):
        if -1 <= a <= 1:
            return round(math.degrees(math.acos(a)), 10)
        return "Error: Input out of range (-1 to 1)"

    # Function for arctan calculation (inverse of tangent, rounded)
    @staticmethod
    def arctan(a):
        return round(math.degrees(math.atan(a)), 10)

    # Function for square of a number
    @staticmethod
    def square(a):
        return a ** 2

    # Function for the square root of a number
    @staticmethod
    def square_root(a):
        if a < 0:
            return "Error: Cannot calculate the root of a negative number"
        return math.sqrt(a)

    # Function for logarithm base 10
    @staticmethod
    def logarithm(a):
        if a <= 0:
            return "Error: Cannot be zero or negative"
        return math.log10(a)

    # Function for natural log base e
    @staticmethod
    def natural_log(a):
        if a <= 0:
            return "Error: Cannot be zero or negative"
        return math.log(a)

    # Function for the cube of a number
    @staticmethod
    def cube(a):
        return a ** 3

    # Function for the cube root of a number
    @staticmethod
    def cube_root(a):
        return a ** (1/3)