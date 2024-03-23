#!/usr/bin/python3
"""Creates a Review class inheriting from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Blueprint for review objects"""

    place_id = ""
    user_id = ""
    text = ""
