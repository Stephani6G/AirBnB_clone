#!/usr/bin/python3
"""This module serializes and deserializes instances and JSON files"""

import json


class FileStorage:
    """
    This class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }
        try:
            temp = {}

            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
