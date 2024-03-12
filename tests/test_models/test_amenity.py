#!/usr/bin/python3
"""Tests for amenity"""
import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """This class represents the test class for Amenity"""
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

    def test_amenity_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """Test that Amenity has name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_init(self):
        """Test that Amenity is initialized correctly"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))


if __name__ == "__main__":
    unittest.main()
