#!/usr/bin/python3
"""Model file_storage: Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class FileStorage():
    """FileStorage:
        Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects by <class name>.id
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return: Dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Create a new entry in __objects for obj by <obj class name>.id"""
        obj_name = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[obj_name] = obj
        
    def save(self):
        """Serialize __objects dict to JSON file"""
        obj_dict = {
            obj: FileStorage.__objects[obj].to_dict()
            for obj in FileStorage.__objects.keys()
            }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects, only if file exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objects = json.load(f)
                for item in objects.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
