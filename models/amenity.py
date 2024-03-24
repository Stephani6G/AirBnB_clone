#!/usr/bin/python3
"""This module creates an amenity module that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Blueprint for amenity objects"""

    name = ""
