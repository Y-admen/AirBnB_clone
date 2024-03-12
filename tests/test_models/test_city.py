#!/usr/bin/python3
"""Tests for city"""
import unittest
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """This class represents the test class for City"""
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

    def test_city_inheritance(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """Test that City has correct attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_init(self):
        """Test that City is initialized correctly"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))


if __name__ == "__main__":
    unittest.main()
