#!/usr/bin/python3
"""This module inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class writes a User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
