#!/usr/bin/python3
"""The review module for the BaseModel program"""

from models.base_model import BaseModel

class Review(BaseModel):
    """ A class that defines the attributes for the review module"""
    
    place_id = ""
    user_id = ""
    text = ""
