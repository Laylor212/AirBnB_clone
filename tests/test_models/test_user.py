#!/usr/bin/python3
"""The implementation of the Test User module"""

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """A class that implements test cases against the user module"""

	def setUp(self):
		"""A function that tests the code to be executed before testing occurs"""
        self.user = User()
		
    def test_if_user_is_a_subclass_of_basemodel(self):
		"""A function that checks if user is a subclass of basemodel"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
	
	def test_if_attrs_are_class_attrs(self):
		"""A function that checks if the class attributes are present"""
        u = User()
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
		"""A function that checks if the class attributes are valid"""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")
