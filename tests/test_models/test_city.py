import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    # Use the setUp method to create an instance of City
    def setUp(self):
        # Creating instance.
        self.city = City()
        # Setting class attributes.
        self.city.name = "Venice"
        self.city.state_id = "1"

    # Use the tearDown method to delete the instance of City
    def tearDown(self):
        del self.city

    def test_no_args(self):
        # Test instance type.
        self.assertEqual(City,type(City()))


    def test_new_instance_save(self):
        # Test that instance is saved correctly.
        self.assertIn(self.city, models.storage.all().values())

    # Write a test method for the __init__ method of the City class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.city, BaseModel)
        # Check that the instance has the state_id and name attributes that
        # are empty strings
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "1")
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "Venice")

    # Write a test method for the __str__ method of the City class
    def test_str(self):
        # Get the string representation of the instance
        city_str = str(self.city)
        # Check that the string representation contains the class name,
        # the id, and the dictionary of attributes
        self.assertIn("[City]", city_str)
        self.assertIn(self.city.id, city_str)
        self.assertIn(str(self.city.__dict__), city_str)

    # Write a test method for the to_dict method of the City class
    def test_to_dict(self):

        # Call the to_dict method of the instance
        city_dict = self.city.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(city_dict, dict)
        # Check that the dictionary contains the __class__ key with the
        # class name as the value
        self.assertEqual(city_dict["__class__"], "City")
        # Check that the dictionary contains the id, created_at, updated_at,
        # state_id, and name keys with the corresponding values
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         self.city.updated_at.isoformat())
        self.assertEqual(city_dict["state_id"], self.city.state_id)
        self.assertEqual(city_dict["name"], self.city.name)


if __name__ == "__main__":
    unittest.main()
