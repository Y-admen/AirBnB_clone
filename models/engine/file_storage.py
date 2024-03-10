#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
import os 
from models.base_model import BaseModel

class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        """initialize"""
        pass

    def all(self):
        """Returns objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves objects dictionary to file"""
        str_object = {}
        for key, obj in self.__objects.items():
            str_object[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json_rpr = json.dumps(str_object, f)

    def reload(self):
        """Reloads objects dictionary from file"""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if data:
                for key, obj in data.items():
                    if key.split('.')[0] == "BaseModel":
                        self.__objects[key] = BaseModel(**obj)
