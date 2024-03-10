#!/usr/bin/python3
"""Review model that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    def __init__(self, *args, **kwargs):
        """Initialize review"""
        super().__init__(*args, **kwargs)
