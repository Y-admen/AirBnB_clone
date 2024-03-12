#!/usr/bin/python3
"""A class to test code."""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""
    def setUp(self):
        """
        Initialize class instance
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        Remove class instance
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_default_dict(self):
        """ Ensure that default dictionary is empty """
        obj = self.file_storage.all()
        self.assertEqual(obj, {})

    def test_object_added_count(self):
        """ Ensure that default dictionary is has key/values """
        for _ in range(3):
            BaseModel()
        obj = self.file_storage.all()
        self.assertEqual(len(obj), 3)

    def test_all(self):
        """Test all method"""
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test new method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertIn(obj, objects.values())

    def test_save(self):
        """Test save method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            saved_data = json.load(f)
            self.assertIn(obj.to_dict(), saved_data.values())

    def test_reload(self):
        """Test reload method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        storage.reload()
        reloaded_objs = storage.all()
        self.assertIn(obj, reloaded_objs.values())

if __name__ == "__main__":
    unittest.main()
