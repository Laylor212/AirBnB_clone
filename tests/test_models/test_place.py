#!/usr/bin/python3
"""The implementation of the Test Place module"""

import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """A class that implements test cases against the place module"""

    def setUp(self):
        """A function that tests the code to be executed before testing occurs"""
        self.place = Place()
        self.attr_list = ["name", "user_id", "city_id", "description",
                          "number_bathrooms", "max_guest", "number_rooms",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_if_place_obj_is_a_subclass_of_basemodel(self):
        """A function that checks if place is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.place), BaseModel))
		
    def test_if_attrs_are_class_attrs(self):
        """A function that checks if the class attributes are present"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attrs(self):
        """A function that checks if the class attributes are valid"""
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))