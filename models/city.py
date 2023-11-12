#!/usr/bin/python3
""""City Model: Defines State class. """

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City : Defines New City.

    Attributes:
        state_id: (str) -> empty string
        name: (str) -> empty string
    """
    state_id = ""
    name = ""
