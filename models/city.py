#!/usr/bin/python3
"""Model city: Defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City: Defines New Cities.

    Attributes:
        state_id: string - empty string
        name: string - empty string
    """
    state_id = ""
    name = ""
