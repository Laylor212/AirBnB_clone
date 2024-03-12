#!/usr/bin/python3
"""The implementation of the Test Review module"""

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """A class that implements test cases against the review module"""

    def setUp(self):
		"""A function that tests the code to be executed before testing occurs"""
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_if_review_is_a_subclass_of_basemodel(self):
		"""A function that checks if review is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_if_attrs_are_class_attrs(self):
		"""A function that checks if the class attributes are present"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
		"""A function that checks if the class attributes are valid"""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))
