#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
import os
from ..base_model import BaseModel


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """""Returns objects dictionary"""""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        return self.__objects

    def save(self):
        """Saves objects dictionary to file"""
        str_objects = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                str_objects[key] = obj.to_dict()
            else:
                str_objects[key] = obj 
        with open(self.__file_path, 'w') as f:
            json.dump(str_objects, f)


    def reload(self):
        """Reloads objects dictionary from file"""
        if os.path.isfile(self.__file_path):
            with open(f"{self.__file_path}", "r") as file:
                read =  file.read()
                if read:
                    self.__objects = json.loads(read)
        else:
            self.save()
