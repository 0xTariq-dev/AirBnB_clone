# Import the unittest module and the BaseModel class
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    # Use the setUp method to create an instance of BaseModel
    def setUp(self):
        self.base = BaseModel()

    # Use the tearDown method to delete the instance of BaseModel
    def tearDown(self):
        del self.base

    # Write a test method for the __init__ method of the BaseModel class
    def test_init(self):
        # Check that the instance has an id attribute that is a string
        self.assertIsInstance(self.base.id, str)
        # Check that the instance has a created_at attribute that is
        # a datetime object.
        self.assertIsInstance(self.base.created_at, datetime)
        # Check that the instance has an updated_at attribute that
        # is a datetime object.
        self.assertIsInstance(self.base.updated_at, datetime)

    # Write a test method for the save method of the BaseModel class
    def test_save(self):
        # Save the current value of the updated_at attribute
        old_updated_at = self.base.updated_at
        # Call the save method of the instance
        self.base.save()
        # Check that the updated_at attribute has changed after the save method
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    # Write a test method for the __str__ method of the BaseModel class
    def test_str(self):
        # Get the string representation of the instance
        base_str = str(self.base)
        # Check that the string representation contains the class name, the id,
        # and the dictionary of attributes
        self.assertIn("[BaseModel]", base_str)
        self.assertIn(self.base.id, base_str)
        self.assertIn(str(self.base.__dict__), base_str)

    # Write a test method for the to_dict method of the BaseModel class
    def test_to_dict(self):
        # Call the to_dict method of the instance
        base_dict = self.base.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(base_dict, dict)
        # Check that the dictionary contains the __class__ key with
        # the class name as the value
        self.assertEqual(base_dict["__class__"], "BaseModel")
        # Check that the dictionary contains the id, created_at,
        # and updated_at keys with the corresponding values
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"],
                         self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"],
                         self.base.updated_at.isoformat())


# Run the tests if the file is executed as the main module
if __name__ == "__main__":
    unittest.main()
