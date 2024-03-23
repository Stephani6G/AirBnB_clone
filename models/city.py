#!/usr/bin/python3
"""Creates a city class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Blueprint for city objects"""

    state_id = ""
    name = ""
