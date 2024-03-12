#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances"""

import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """ A class that defines the attributes for the FileStorage modules"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A function that returns the dictionary __objects"""
        
        return self.__objects

    def new(self, obj):
        """A function that sets in __objects"""
        
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """A function that serializes __objects to the JSON file"""
        
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """A function that deserializes the JSON file to __objects"""
        
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
