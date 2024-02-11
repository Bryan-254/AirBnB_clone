#!/usr/bin/python3
"""Module for FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    The file storage handling class
    """
    __file_path = "file.json"
    __objects = {}
    CLASSES = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        By importing BaseModel locally within the reload() method,
        you avoid the circular import issue.
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create instances based on class name
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                        self.__objects[key] = obj
                    # Add more elif statements for other model classes here
        except FileNotFoundError:
            pass
