#!/usr/bin/python3
"""
Defines a class BaseModel that defines all common attributes/methods
for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """Creates a blueprint for the Base Model"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class"""

        if kwargs:
            for key,value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    value = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel class"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        obj_dict = {}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                obj_dict[key] = self.__dict__[key].isoformat()
            else:
                obj_dict[key] = self.__dict__[key]
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
