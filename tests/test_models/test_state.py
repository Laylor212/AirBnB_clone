#!/usr/bin/python3
"""The implementation of the Test State module"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """A class that implements test cases against the state module""""

    def setUp(self):
		"""A function that tests the code to be executed before testing occurs"""
        self.state = State()

    def test_if_state_is_a_subclass_of_basemodel(self):
		"""A function that checks if state is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_if_attr_is_a_class_attr(self):
		"""A function that checks if the class attribute is present"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
		"""A function that checks if the class attribute is valid"""
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
