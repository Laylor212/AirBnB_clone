#!/usr/bin/python3
"""The implementation of the Test City module"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """A class that implements test cases against the city module"""

    def setUp(self):
		"""A function that tests the code to be executed before testing occurs"""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_if_city_is_a_subclass_of_basemodel(self):
		"""A function that checks if city is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_if_attrs_are_class_attrs(self):
		"""A function that checks if the class attributes are present"""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))
