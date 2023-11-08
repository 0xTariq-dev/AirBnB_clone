#!/usr/bin/python3
"""Model base_model: Defines BaseModel class."""

import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel:
        Defines All common attributes/methods for other classes in this project
    """
    
    def __init__(self, *args, **kwargs):
        """
        Instatiation method for BaseModel class.

        Args:
            *args (list): list of unamed args.
            **kwargs (dict): dictionary of keyword args in a key/value pair.
        """
        if len(args) != 0:
            pass
        elif len(kwargs) != 0:
            for key, val in kwargs.items():
                match key:
                    case "id":
                        self.id = val
                    case "name":
                        self.name = val
                    case "created_at":
                        self.created_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    case "updated_at":
                        self.updated_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    case "__class__":
                        pass
                    case _:
                        self.key = val
                
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
