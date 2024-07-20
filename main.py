# -*- coding: utf-8 -*-
from area import Circle, Triangle, Square, calculate_area, Test_shapes
import unittest

def main():
    shapes = [Circle(5), Triangle(1, 2, 3), Square(5)]
    for shape in shapes:
        print(f"Area: {calculate_area(shape)}")

    print("Unit-tests...\n")
    unittest.TextTestRunner().run(unittest.makeSuite(Test_shapes))

if __name__ == "__main__":
    main()