from typing import Union
"""Module for combining data types
"""
from math import sqrt, pi
"""Module for obtaining pi and calculating the root
"""


class TriangleException(Exception):
    """a class with a custom error for the triangle
    """
    def sometriangleexception(self):
        pass


class CircleException(Exception):
    """a class with a custom error for the circle
    """
    def somecircleexception(self):
        pass
    pass


class Triangle:
    """a class for creating and calculating triangle properties"""

    def __init__(self, a: Union[float, int], b: Union[float, int], c: Union[float, int]):
        """Creating a triangle

        Args:
            a (Union[float, int]): first side of the triangle
            b (Union[float, int]): second side of the triangle
            c (Union[float, int]): third side of the triangle
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2]
        """
        self.__sides = [a, b, c]
        self.checker(self.sides)

    def checker(self, sides):
        """Error checker for triangle

        Args:
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2]

        Raises:
            TriangleException: does not match the numeric data type
            TriangleException: checks the number of sides in a triangle
            TriangleException: does not conform to the rules of the triangle
            TriangleException: negative numbers cannot be the length of a side
        """
        if not isinstance(sides[0] or sides[1] or sides[2], Union[float, int]):
            raise TriangleException("Неверный формат данных")
        if len(sides) != 3:
            raise TriangleException("Не хватает сторон")
        if not (sides[0] + sides[2] > sides[1] and
                sides[1] + sides[2] > sides[0] and
                sides[2] + sides[0] > sides[1]):
            raise TriangleException("Такой треугольник не построить")
        if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
            raise TriangleException("Чумба, сходи попей колесики, а потом задавая отрицательные числа для сторон")

    @property
    def sides(self):
        """getter for sides"""
        return self.__sides

    @sides.setter
    def sides(self, sides):
        """setter for sides

        Args:
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2]
        """
        self.__sides = sides
        self.checker(sides)

    def perimetr(self):
        """calculating the rounded perimeter of a triangle

        Returns:
            float: perimetr of triangle
        """
        return round((self.__sides[0] + self.__sides[1] + self.__sides[2]), 2)

    def square(self):
        """calculating the rounded area of a triangle

        Returns:
            float: square of triangle
        """
        p = self.perimetr() * 0.5
        return round((sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))), 2)


class Circle:
    """a class for creating and calculating circle properties"""
    def __init__(self, radius: Union[float, int]):
        """Creating a circle

        Args:
            radius (Union[float, int]): radius of a circle
        """
        self.__radius = radius
        self.checker(self.radius)

    def checker(self, radius):
        """Error checker for circle

        Args:
            radius (Union[float, int]): radius of a circle

        Raises:
            CircleException: check for a negative number
            CircleException: data format check
        """
        if not isinstance(radius, Union[float, int]):
            raise CircleException("Неверный формат данных")
        if radius <= 0:
            raise CircleException("Такую окружность не построить")

    @property
    def radius(self):
        """getter for radius"""
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[float, int]):
        """setter for radius

        Args:
            radius (Union[float, int]): radius of a circle
        """
        self.checker(radius)
        self.__radius = radius

    def circumference(self):
        """rounded circle length calculation

        Returns:
            float: circle length
        """
        return round((2 * pi * self.__radius), 2)

    def square(self):
        """rounded circle area calculation

        Returns:
            float: circle area
        """
        return round((pi * self.__radius ** 2), 2)
