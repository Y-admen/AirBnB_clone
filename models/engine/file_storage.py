#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
            json.dump(str_object, f)

    def reload(self):
        """Reloads objects dictionary from file"""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if data:
                for key, obj in data.items():
                    if "BaseModel" in key:
                        self.__objects[key] = BaseModel(**obj)
                    if "User" in key:
                        self.__objects[key] = User(**obj)
                    if "State" in key:
                        self.__objects[key] = State(**obj)
                    if "City" in key:
                        self.__objects[key] = City(**obj)
                    if "Amenity" in key:
                        self.__objects[key] = Amenity(**obj)
                    if "Place" in key:
                        self.__objects[key] = Place(**obj)
                    if "Review" in key:
                        self.__objects[key] = Review(**obj)
