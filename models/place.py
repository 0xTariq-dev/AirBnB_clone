#!/usr/bin/python3
"""Model place: Defines Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class place: Defines New Places.

    Attributes:
        city_id: string - empty string (City id)
        user_id: string - empty string (User id)
        name: string - empty string (Place name)
        description: string - empty string (Place description)
        number_rooms: integer - 0 (Number of rooms)
        number_bathrooms: integer - 0 (Number of bathrooms)
        max_guest: integer - 0 (Max number of guests)
        price_by_night: integer - 0 (Night price)
        latitude: float - 0.0 (Latitude index)
        longitude: float - 0.0 (Longitude index)
        amenity_ids: list of string - empty list (List of amenity ids)
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
