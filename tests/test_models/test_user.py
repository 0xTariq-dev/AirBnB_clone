import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    # Use the setUp method to create an instance of User
    def setUp(self):
        # Creating instance.
        self.user = User()
        # Setting class attributes
        self.user.email = "Bob@HBNB.com"
        self.user.password = "****"
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"

    # Use the tearDown method to delete the instance of User
    def tearDown(self):
        del self.user


    def test_no_args(self):
    # Test instance type.
        self.assertEqual(User,type(User()))


    def test_new_instance_save(self):
        # Test that instance is saved correctly.
        self.assertIn(User(), models.storage.all().values())

    # Write a test method for the __init__ method of the User class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.user, BaseModel)
        # Check that the instance has the email, password, first_name,
        # and last_name attributes that are empty strings
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "Bob@HBNB.com")
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "****")
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "Bob")
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "Dylan")

    # Write a test method for the __str__ method of the User class
    def test_str(self):
        # Get the string representation of the instance
        user_str = str(self.user)
        # Check that the string representation contains the class name,
        # the id, and the dictionary of attributes
        self.assertIn("[User]", user_str)
        self.assertIn(self.user.id, user_str)
        self.assertIn(str(self.user.__dict__), user_str)

    # Write a test method for the to_dict method of the User class
    def test_to_dict(self):
        # Call the to_dict method of the instance
        user_dict = self.user.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(user_dict, dict)
        # Check that the dictionary contains the __class__ key
        # with the class name as the value
        self.assertEqual(user_dict["__class__"], "User")
        # Check that the dictionary contains the id, created_at,
        # updated_at, email, password, first_name, and last_name
        # keys with the corresponding values
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"],
                         self.user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)


if __name__ == "__main__":
    unittest.main()

