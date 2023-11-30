#!/usr/bin/python
"""Module to test base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Base class set up")
    def setUp(self):
        print("base set up")
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
    
    def tearDown(self):
        print("base tear down")
        Base._Base__nb_objects = 0

    def test_base(self):
        print("test base id")
        print(Base._Base__nb_objects)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

if __name__ == "__main__":
    unittest.main()
