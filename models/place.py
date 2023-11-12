#!/usr/bin/python3
""""Place Model: Defines Place class. """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place : Defines New Place.

    Attributes:
        name: (str) -> empty string
        city_id: (str) -> empty string: it will be the City.id
        user_id: (str) -> empty string: it will be the User.id
        description: (str) -> empty string
        number_rooms: (int) -> 0
        number_bathrooms: (int) -> 0
        max_guest: (int) -> 0
        price_by_night: (int) -> 0
        latitude: (float) -> 0.0
        longitude: (float) -> 0.0
        amenity_ids: list of string - empty list: list of Amenity.id.
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
