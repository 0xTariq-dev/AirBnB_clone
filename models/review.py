#!/usr/bin/python3
""""Review Model: Defines Review class. """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review : Defines New Review.

    Public class attributes:
        place_id: (str) -> empty string: it will be the Place.id
        user_id: (str) -> empty string: it will be the User.id
        text: (str) -> empty string
    """
    user_id = ""
    place_id = ""
    text = ""

