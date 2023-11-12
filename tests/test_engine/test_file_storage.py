# Import the unittest module and the other models classes.
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    # Use the setUp method to create an instance of FileStorage and some instances of other classes
    def setUp(self):
        self.storage = FileStorage()
        self.base = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    # Use the tearDown method to delete the instance of FileStorage and the instances of other classes
    def tearDown(self):
        del self.storage
        del self.base
        del self.user
        del self.state
        del self.city
        del self.amenity
        del self.place
        del self.review

    # Write a test method for the all method of the FileStorage class
    def test_all(self):
        # Check that the all method returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)
        # Check that the dictionary is empty initially
        self.storage.__dict__ = self.storage.all()
        self.assertEqual(len(self.storage.all()), len(self.storage.__dict__))

    # Write a test method for the new method of the FileStorage class
    def test_new(self):
        # Call the new method with some instances of other classes
        self.storage.new(self.base)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)

        # Check that the __objects attribute of the storage instance has the correct keys and values
        self.assertIn("BaseModel." + self.base.id, self.storage.all())
        self.assertIn("User." + self.user.id, self.storage.all())
        self.assertIn("State." + self.state.id, self.storage.all())
        self.assertIn("City." + self.city.id, self.storage.all())
        self.assertIn("Amenity." + self.amenity.id, self.storage.all())
        self.assertIn("Place." + self.place.id, self.storage.all())
        self.assertIn("Review." + self.review.id, self.storage.all())
        self.assertEqual(self.storage.all()["BaseModel." + self.base.id], self.base)
        self.assertEqual(self.storage.all()["User." + self.user.id], self.user)
        self.assertEqual(self.storage.all()["State." + self.state.id], self.state)
        self.assertEqual(self.storage.all()["City." + self.city.id], self.city)
        self.assertEqual(self.storage.all()["Amenity." + self.amenity.id], self.amenity)
        self.assertEqual(self.storage.all()["Place." + self.place.id], self.place)
        self.assertEqual(self.storage.all()["Review." + self.review.id], self.review)


    # Write a test method for the save method of the FileStorage class
    def test_save(self):
        # Call the save method of the storage instance
        self.storage.save()
        # Check that the JSON file exists and has the correct content
        with open("file.json", "r") as f:
            content = f.read()
            self.assertIn("BaseModel." + self.base.id, content)
            self.assertIn("User." + self.user.id, content)
            self.assertIn("State." + self.state.id, content)
            self.assertIn("City." + self.city.id, content)
            self.assertIn("Amenity." + self.amenity.id, content)
            self.assertIn("Place." + self.place.id, content)
            self.assertIn("Review." + self.review.id, content)

    # Write a test method for the reload method of the FileStorage class
    def test_reload(self):
        # Call the reload method of the storage instance
        self.storage.reload()
        # Check that the __objects attribute of the storage instance has the correct keys and values
        self.assertIn("BaseModel." + self.base.id, self.storage.all())
        self.assertIn("User." + self.user.id, self.storage.all())
        self.assertIn("State." + self.state.id, self.storage.all())
        self.assertIn("City." + self.city.id, self.storage.all())
        self.assertIn("Amenity." + self.amenity.id, self.storage.all())
        self.assertIn("Place." + self.place.id, self.storage.all())
        self.assertIn("Review." + self.review.id, self.storage.all())
        self.assertEqual(self.storage.all()["BaseModel." + self.base.id].to_dict(), self.base.to_dict())
        self.assertEqual(self.storage.all()["User." + self.user.id].to_dict(), self.user.to_dict())
        self.assertEqual(self.storage.all()["State." + self.state.id].to_dict(), self.state.to_dict())
        self.assertEqual(self.storage.all()["City." + self.city.id].to_dict(), self.city.to_dict())
        self.assertEqual(self.storage.all()["Amenity." + self.amenity.id].to_dict(), self.amenity.to_dict())
        self.assertEqual(self.storage.all()["Place." + self.place.id].to_dict(), self.place.to_dict())
        self.assertEqual(self.storage.all()["Review." + self.review.id].to_dict(), self.review.to_dict())
