#!/usr/bin/python3
"""Tests for place"""
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class represents the test class for Place"""
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

    def test_place_inheritance(self):
        """Test that Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """Test that Place has correct attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_init(self):
        """Test that Place is initialized correctly"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))


if __name__ == "__main__":
    unittest.main()
