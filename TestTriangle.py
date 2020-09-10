"""
@author: Shivani Taneja

This file contains Python code to test Triangles
"""

import unittest

from HWAssignments.Triangles import Triangle


class TestTriangle(unittest.TestCase):

    def test_classifyTriangle(self):
        result = Triangle.classifyTriangle(1, 1, 1)
        self.assertEqual(result, "Equilateral")

        result1 = Triangle.classifyTriangle(1, 1, 2)
        self.assertEqual(result1, "Isosceles")

        result2 = Triangle.classifyTriangle(1, 2, 3)
        self.assertEqual(result2, "Scalene")

        result3 = Triangle.classifyTriangle(0, 0, 0)
        self.assertEqual(result3, "Invalid Input")

        result5 = Triangle.classifyTriangle(3, 3, 3)
        self.assertEqual(result5, "Equilateral")

        result6 = Triangle.classifyTriangle(3, 4, 5)
        self.assertEqual(result6, "Right")


if __name__ == '__main__':
    unittest.main()
