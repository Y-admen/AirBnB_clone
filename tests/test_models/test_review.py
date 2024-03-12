#!/usr/bin/python3
"""Tests for place"""
import unittest
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """This class represents the test class for Review"""
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

    def test_review_inheritance(self):
        """Test that Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test that Review has correct attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_init(self):
        """Test that Review is initialized correctly"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


if __name__ == "__main__":
    unittest.main()
