#!/usr/bin/python3
"""Model console: Defines HBNHCommand class."""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand:
        The entry point of the command interperter.
    """
    prompt = "

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
            for key, val in kwargs.items():
                match key:
                    case "created_at" or "updated_at":
                        self.__dict__[key] = datetime.strptime(val, time_fmt)
                    case "__class__":
                        pass
                    case _:
                        self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
