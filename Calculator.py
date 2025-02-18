# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:01:27 2025

@author: computershop.mn
"""
#importing math for the use of mathimatical functions
import math

class Calculator:

#function for addition
  def add(a, b):
    return a + b

#function for substraction
  def subtract(a, b):
    return a - b

#function for multiplying
  def multiply(a, b):
    return a * b

#function for deviding
  def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

#function for sine calculation
  def sine(a):
    return round(math.sin(math.radians(a)),10)

#fucntion for cosine calculation
  def cosine(a):
    return round(math.cos(math.radians(a)),10)

#function for tangent calculation
  def tangent(a):
    return round(math.tan(math.radians(a)),10)

#function for arcsin calculation, it is inverse of sine
  def arcsin(a):
    if -1 <= a <= 1:
        return round(math.degrees(math.asin(a)),10)
    return "Error: Input out of range (-1 to 1)"

#function for arccos calculation, it is inverse of cos
  def arccos(a):
    if -1 <= a <= 1:
        return round(math.degrees(math.acos(a)),10)
    return "Error: Input out of range (-1 to 1)"

#function for arctan calculation, it is inverse of tangent
  def arctan(a):
    return round(math.degrees(math.atan(a)),10)

#function for square of a number
  def square(a):
    return a ** 2

#function for the square root of a number
  def square_root(a):
    if a < 0:
        return "Error: Cannot calculate the root of negative number"
    return math.sqrt(a)

# to calculate logarithm base 10
  def logarithm (a):
    if a<= 0 :
        return "Error: cannot be zero or negative"
    return math.log(a)

#to find natural log base e
  def natural_log(a):
    if a <= 0:
        return "Error: cannot be zero or negative"
    return math.log(a)

#to find the cube of a number
  def cube(a):
    return a ** 3 

#to find cube root of a number
  def cube_root(a):
    return a **(1/3)

            










