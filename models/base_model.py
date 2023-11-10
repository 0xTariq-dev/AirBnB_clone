#!/usr/bin/python3
"""Model base_model: Defines BaseModel class."""
import models
from uuid import uuid4
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
        time_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                    if k in ["created_at", "updated_at"]:
                        self.__dict__[k] = datetime.strptime(v, time_fmt)
                    else:
                        self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Saves objects and updates Updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns the string representation of Class instances"""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
    
    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
