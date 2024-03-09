#!/usr/bin/python3
from base_model import BaseModel
from engine.file_storage import FileStorage

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
