import unittest
import models
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    # Use the setUp method to create an instance of Amenity
    def setUp(self):
        # Creating instance.
        self.amenity = Amenity()
        # Setting class attribute.
        self.amenity.name = "Bob"
        self.amenity.number = "1"
        # Casting attributes to dictionary.
        amenity_dict = self.amenity.to_dict()

    # Use the tearDown method to delete the instance of Amenity
    def tearDown(self):
        del self.amenity

    # Test instance type.
    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_save(self):
        # Test that instance is saved correctly.
        self.assertIn(Amenity(), models.storage.all().values())

    # Write a test method for the __init__ method of the Amenity class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.amenity, BaseModel)
        # Check that the instance has a name attribute that is an empty string
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    # Write a test method for the __str__ method of the Amenity class
    def test_str(self):
        # Get the string representation of the instance.
        amenity_str = str(self.amenity)
        # Check that the string representation contains the class name, the id,
        # and the dictionary of attributes
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(self.amenity.id, amenity_str)
        self.assertIn(str(self.amenity.__dict__), amenity_str)

 
class TestAmenity_to_dict(unittest.TestCase):
    # Write a test method for the to_dict method of the Amenity class

    # Use the setUp method to create an instance of Amenity
    def setUp(self):
        # Creating instance.
        self.amenity = Amenity()
        # Setting class attribute.
        self.amenity.name = "Bob"
        self.amenity.number = "1"
        # Casting attributes to dictionary.
        amenity_dict = self.amenity.to_dict()

    def test_to_dict_type(self):
        # Test to_dict return type.
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_keys(self):
        # Test presence of correct keys in Amenity dict.
        self.assertIn("id", self.amenity.to_dict())
        self.assertIn("created_at", self.amenity.to_dict())
        self.assertIn("updated_at", self.amenity.to_dict())
        self.assertIn("__class__", self.amenity.to_dict())

    def test_to_dict_added_attributes(self):
        # Confirming added attributes.
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], self.amenity.name)
        self.assertEqual(amenity_dict["number"], self.amenity.number)

    def test_to_dict_attributes_type(self):
        amenity_dict = self.amenity.to_dict()
        # Check that the dictionary attributes the id, created_at,
        # updated_at, have the corresponding types.
        self.assertEqual(type(amenity_dict["id"], str))
        self.assertEqual(type(amenity_dict["created_at"], str))
        self.assertEqual(type(amenity_dict["updated_at"], str))

    def test_to_dict_output(self):
        # Comparing to_dict with a custom dict.
        dt = datetime.today()
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.amenity.id = "1-2-3-4"
        self.assertEqual(amenity_dict["created_at"],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], self.amenity.name)
