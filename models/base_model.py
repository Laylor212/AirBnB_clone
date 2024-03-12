#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ A class that defines the attributes for all modules"""

    def __init__(self, *args, **kwargs):
        """A function that initializes the BaseModel class attributes"""

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """A function that returns the string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """A function that updates 'self.updated_at'"""
        
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """A function that returns a dictionary"""
        
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
