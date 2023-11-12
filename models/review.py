#!/usr/bin/python3
"""Model review: Defines Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review: Defines New Reviews.

    Attributes:
        place_id: string - empty string (Id of place reviewed)
        user_id: string - empty string (Id of User reviewing)
        text: string - empty string (The review body)
    """
    place_id = ""
    user_id = ""
    text = ""
