import unittest
from models.base_model import BaseModel
from models.state import State
import models

class TestState(unittest.TestCase):
    # Use the setUp method to create an instance of State
    def setUp(self):
        # Creating instance.
        self.state = State()
        # Setting class attributes.
        self.state.name = "California"

    # Use the tearDown method to delete the instance of State
    def tearDown(self):
        del self.state


    def test_no_args(self):
        # Test instance type.
        self.assertEqual(State,type(State()))


    def test_new_instance_save(self):
        # Test that instance is saved correctly.
        self.assertIn(self.state, models.storage.all().values())

    # Write a test method for the __init__ method of the State class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.state, BaseModel)
        # Check that the instance has a name attribute that is an empty string
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "California")

    # Write a test method for the __str__ method of the State class
    def test_str(self):
        # Get the string representation of the instance
        state_str = str(self.state)
        # Check that the string representation contains the class name,
        # the id, and the dictionary of attributes.
        self.assertIn("[State]", state_str)
        self.assertIn(self.state.id, state_str)
        self.assertIn(str(self.state.__dict__), state_str)

    # Write a test method for the to_dict method of the State class
    def test_to_dict(self):
        # Call the to_dict method of the instance
        state_dict = self.state.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(state_dict, dict)
        # Check that the dictionary contains the __class__ key
        # with the class name as the value
        self.assertEqual(state_dict["__class__"], "State")
        # Check that the dictionary contains the id, created_at, updated_at,
        # and name keys with the corresponding values
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["created_at"],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         self.state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], self.state.name)


if __name__ == "__main__":
    unittest.main()
