#!/usr/bin/python3
"""Place Model that inherits from BaseModel"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Represents a place.

    Attributes:
        city_id (str): The City id 
        user_id (str): The User id of the owner
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests allowed
        price_by_night (int): The price by night of the place
        latitude (float): The latitude coordinate of the place
        longitude (float): The longitude coordinate of the place
        amenity_ids (list): A list of Amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a new Place"""
        super().__init__(*args, **kwargs)
