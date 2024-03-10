#!/usr/bin/python3
"""Defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity"""

    def __init__(self, *args, **kwargs):
        """Initialize amenity"""
        super().__init__(*args, **kwargs)
