"""
@author: Shivani Taneja

This Python file contains a class to determine whether a triangle is scalene
, isosceles, right or equilateral.

"""


def classifyTriangle(a, b, c):
    """

    :param a: Length of the first side of triangle
    :param b: Length of the second side of triangle
    :param c: Length of third side of triangle
    :return: A String:

    'Equilateral' : If all three sides are equal
    'Isosceles' : If exactly two sides are equal
    'Scalene' : If no two sides are equal
    'Right': If sum of the squares of any two sides is equal to the third side
 """

    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0 or b == 0 or c == 0:
        result = "Invalid Input"
    elif a == b and b == c and c == a:
        result = "Equilateral"
    elif (a ^ 2) + (b ^ 2) == (c ^ 2):
        result = "Right"
    elif a != b and a != c and b != c:
        result = "Scalene"
    else:
        result = "Isosceles"
    return result
