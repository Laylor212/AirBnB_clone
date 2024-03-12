#!/usr/bin/python3
"""The user module for the BaseModel program"""

from models.base_model import BaseModel

class User(BaseModel):
    """A class that defines the attributes for the user module"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
