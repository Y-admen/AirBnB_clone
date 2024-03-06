#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
import  os

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
    def save(self):
        """Saves objects dictionary to file"""
        temp = self.__objects
        serialize = json.dumps(temp)
        with open(f'{self.__file_path}', 'w') as file:
            file.write(serialize)
    def reload(self):
        """Reloads objects dictionary from file"""
        if os.path.isfile(self.__file_path):
            with open(f"{self.__file_path}", "r") as file:
                self.__objects = json.load(file)
