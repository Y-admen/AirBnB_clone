#!/usr/bin/python3
"""
User model class that inherits from BaseModel.

Attributes:
  - email (str): Email address of the user
  - password (str): Hashed password for the user
  - first_name (str): First name of the user
  - last_name (str): Last name of the user

"""
from .base_model import BaseModel


class User(BaseModel):
    """
    A User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initial user attributes"""
        super().__init__(*args, **kwargs)
