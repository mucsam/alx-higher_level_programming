#!/usr/bin/python3
"""Testing the Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        print(" Rectangle set up")
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        print("Rectangle tear down")
        Base._Base__nb_objects = 0
    def test_id(self):
        print("id test Rectangle")
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_attrs_validation(self):
        print("attributes validation test")
        self.assertRaises(TypeError, Rectangle, "sa", "m")

        with self.assertRaises(ValueError):
            Rectangle(-1, -1, -1, -1)
        

if __name__ == "__main__":
    unittest.main()
