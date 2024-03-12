#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """This class represents the test class for BaseModel"""
    def setUp(self):
        """
        Initialize class instance
        """
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Remove class instance
        """
        FileStorage._FileStorage__objects = {}

    def test_id_uniqueness(self):
        """Test that id is unique for each instance"""
        id1 = self.BaseModel.id
        id2 = BaseModel().id
        self.assertNotEqual(id1, id2)

    def test_save(self):
        """Test that save method saves the object to the storage"""
        prev_updated_at = self.BaseModel.updated_at
        self.BaseModel.save()
        self.assertNotEqual(prev_updated_at, self.BaseModel.updated_at)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary"""
        BaseModel_dict = self.BaseModel.to_dict()
        self.assertIsInstance(BaseModel_dict, dict)

    def test_instance_str(self):
        """Test that instance string representation is correct"""
        inst = self.BaseModel
        id = inst.id
        string = "[{}] ({}) {}".format(inst.__class__.__name__,
                                       id, inst.__dict__)
        self.assertEqual(inst.__str__(), string)

    def test_str(self):
        """Test that string representation is correct"""
        string_representation = str(self.BaseModel)
        self.assertIsInstance(string_representation, str)


if __name__ == '__main__':
    unittest.main()
