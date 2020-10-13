#!/usr/bin/python3
"""
Unitest for models/reactangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle, __doc__ as mrdoc
import inspect
import pep8
from contextlib import redirect_stdout
from io import StringIO


class TestRectangle(unittest.TestCase):
    """
    This class tests the Rectangle class
    """
    def test_doctstring(self):
        """
        Checks doctstring for base class
        """
        self.assertTrue(len(mrdoc.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_rectangle_correct(self):
        """
        Checks correct instance of a Rectangle
        """
        r = Rectangle(4, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.x, 0)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_calling(self):
        """
        Checks the calling of Rectangle
        """
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_float_attributes(self):
        """
        Checks validation for attributes
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(2.0, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, 3.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, 4.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, 5.6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(float('inf'), 2)
            print(r.__dict__)

    def test_string_attributes(self):
        """
        Checks validation for attributes
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("Test", 2)

    def test_negative_numbers_attributes(self):
        """
        Checks validation for attributes
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1, 0, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """
        Checks for area of a Rectangle
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)
        r2 = Rectangle(123165465413468746521, 465465789798796846)
        self.assertEqual(r2.area(), 57329310634616626634639190709548272766)
        with self.assertRaises(TypeError):
            r2.area(1)

    def test_display(self):
        """
        Checks display function
        """
        r = Rectangle(2, 2)
        stout = StringIO()
        with redirect_stdout(stout):
            r.display()
        out = stout.getvalue()
        self.assertEqual(out, ("#" * 2 + "\n") * 2)
        r2 = Rectangle(5, 10)
        stout = StringIO()
        with redirect_stdout(stout):
            r2.display()
        out = stout.getvalue()
        self.assertEqual(out, ("#" * 5 + "\n") * 10)
        r3 = Rectangle(5, 2, 1, 2)
        stout = StringIO()
        with redirect_stdout(stout):
            r3.display()
        out = stout.getvalue()
        self.assertEqual(out, "\n" * 2 + (" " * 1 + "#" * 5 + "\n") * 2)

    def test_str(self):
        """
        Checks __str__ function
        """
        r = Rectangle(2, 5, 8, 2, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 8/2 - 2/5")
        r2 = Rectangle(1, 1, 0, 0, 3)
        self.assertEqual(r2.__str__(), "[Rectangle] (3) 0/0 - 1/1")


if __name__ == '__main__':
    unittest.main()
