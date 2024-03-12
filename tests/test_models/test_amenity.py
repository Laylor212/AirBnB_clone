#!/usr/bin/python3
"""The implementation of the Test Amenity module"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """A class that implements test cases against the amenity module"""

    def setUp(self):
		"""A function that tests the code to be executed before testing occurs"""
        self.amenity = Amenity()

    def test_if_amenity_is_a_subclass_of_basemodel(self):
		"""A function that checks if amenity is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_if_attr_is_a_class_attr(self):
		"""A function that checks if the class attribute is present"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
		"""A function that checks if the class attribute is valid"""
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
