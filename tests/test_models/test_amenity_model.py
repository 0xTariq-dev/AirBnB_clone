import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    # Use the setUp method to create an instance of Amenity
    def setUp(self):
        self.amenity = Amenity()

    # Use the tearDown method to delete the instance of Amenity
    def tearDown(self):
        del self.amenity

    # Write a test method for the __init__ method of the Amenity class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.amenity, BaseModel)
        # Check that the instance has a name attribute that is an empty string
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    # Write a test method for the __str__ method of the Amenity class
    def test_str(self):
        # Get the string representation of the instance
        amenity_str = str(self.amenity)
        # Check that the string representation contains the class name, the id,
        # and the dictionary of attributes
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(self.amenity.id, amenity_str)
        self.assertIn(str(self.amenity.__dict__), amenity_str)

    # Write a test method for the to_dict method of the Amenity class
    def test_to_dict(self):
        # Setting class attribute.
        self.amenity.name = "Bob"
        # Call the to_dict method of the instance
        amenity_dict = self.amenity.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(amenity_dict, dict)
        # Check that the dictionary contains the __class__ key with
        # the class name as the value
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        # Check that the dictionary contains the id, created_at, updated_at,
        # and name keys with the corresponding values
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["created_at"],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], self.amenity.name)
