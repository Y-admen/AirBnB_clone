#!/usr/bin/python3
"""Tests for review"""
import unittest
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """This class represents the test class for State"""
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

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test that State has correct attributes"""
        state = State()
        self.assertEqual(state.name, "")

    def test_init(self):
        """Test that State is initialized correctly"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))


if __name__ == "__main__":
    unittest.main()
