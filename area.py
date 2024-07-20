# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math
import unittest

#Легкость добавления других фигур. Добавил квадрат.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad
    def area(self):
        return math.pi * self.rad ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    #Проверку на то, является ли треугольник прямоугольным
    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        if (sides[0]**2+sides[1]**2 == sides[2]**2):
            print("Is right triangle!")
            return True
        print("Is not right triangle!")
        return False

#Добавление площади квадрата.
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

#Unit-тесты через unittest
class Test_shapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertEqual(circle.area(), math.pi * 25)
    
    def test_triangle(self):
        triangle = Triangle(1, 2, 3)
        self.assertEqual(triangle.area(), 0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_square(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)



#Вычисление площади фигуры без знания типа фигуры в compile-time
def calculate_area(shape: Shape):
    return shape.area()