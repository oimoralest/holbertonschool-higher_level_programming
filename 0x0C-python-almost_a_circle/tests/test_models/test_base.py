#!/usr/bin/python3
"""
Unitest for models/base.py
"""
import unittest
from models.base import Base, __doc__ as mbdoc
import inspect
import pep8


class TestBase(unittest.TestCase):
    """
    This class tests the Base class
    """
    def test_doctstring(self):
        """
        Checks doctstring for base class
        """
        self.assertTrue(len(mbdoc.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_base_class(self):
        """
        1. Base class
        """
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_changeid(self):
        """
        Changing id for the instance
        """
        b2 = Base(3)
        self.assertEqual(b2.id, 3)
        self.assertEqual(Base._Base__nb_objects, 1)
        b2.id = 4
        self.assertEqual(b2.id, 4)
        b2.id = "Test"
        self.assertEqual(b2.id, "Test")

    def test_callingBase(self):
        """
        Call the class with more than 1 argument
        """
        with self.assertRaises(TypeError):
            b3 = Base(1, 2)


if __name__ == '__main__':
    unittest.main()
