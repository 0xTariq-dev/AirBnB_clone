#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            pass
        elif len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'name':
                    self.name = val
                if key == 'created_at':
                    self.created_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
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
