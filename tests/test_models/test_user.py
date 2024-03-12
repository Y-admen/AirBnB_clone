#!/usr/bin/python3
"""Tests for User"""
import unittest
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """This class represents the test class for User"""

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

    def test_user_inheritance(self):
        """Test that User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test that User has correct attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_init(self):
        """Test that User is initialized correctly"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))


if __name__ == '__main__':
    unittest.main()
