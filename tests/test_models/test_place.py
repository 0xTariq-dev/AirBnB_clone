import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    # Use the setUp method to create an instance of Place
    def setUp(self):
        # Creating instance.
        self.place = Place()
        # Setting class attributes.
        self.place.name = "Town House"
        self.place.description = "Town House with a lake view"
        self.place.city_id = "Amesterdam"
        self.place.user_id = "543"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 1
        self.place.max_guest = 5
        self.place.price_by_night = 20
        self.place.latitude = 52.370216
        self.place.longitude = 4.895168
        self.place.amenity_ids = ["TV", "Air condition", "Game room"]

    def tearDown(self):
        # Use the tearDown method to delete the instance of Place
        del self.place

    # Write a test method for the __init__ method of the Place class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.place, BaseModel)
        # Check that the instance has the city_id, user_id, name, description,
        # number_rooms, number_bathrooms, max_guest, price_by_night, latitude,
        # longitude, and amenity_ids attributes that are initialized
        # with default values.
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "Amesterdam")
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "543")
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "Town House")
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description,
                         "Town House with a lake view")
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 3)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 5)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 20)
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 52.370216)
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 4.895168)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids,
                         ["TV", "Air condition", "Game room"])

    # Write a test method for the __str__ method of the Place class
    def test_str(self):
        # Get the string representation of the instance
        place_str = str(self.place)
        # Check that the string representation contains the class name,
        # the id, and the dictionary of attributes.
        self.assertIn("[Place]", place_str)
        self.assertIn(self.place.id, place_str)
        self.assertIn(str(self.place.__dict__), place_str)

    # Write a test method for the to_dict method of the Place class
    def test_to_dict(self):
        # Call the to_dict method of the instance
        place_dict = self.place.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(place_dict, dict)
        # Check that the dictionary contains the __class__ key
        # with the class name as the value.
        self.assertEqual(place_dict["__class__"], "Place")
        # Check that the dictionary contains the id, created_at, updated_at,
        # city_id, user_id, name, description, number_rooms, number_bathrooms,
        # max_guest, price_by_night, latitude, longitude, and amenity_ids
        # keys with the corresponding values
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["created_at"],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         self.place.updated_at.isoformat())
        self.assertEqual(place_dict["city_id"], self.place.city_id)
        self.assertEqual(place_dict["user_id"], self.place.user_id)
        self.assertEqual(place_dict["name"], self.place.name)
        self.assertEqual(place_dict["description"], self.place.description)
        self.assertEqual(place_dict["number_rooms"], self.place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"],
                         self.place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], self.place.max_guest)
        self.assertEqual(place_dict["price_by_night"],
                         self.place.price_by_night)
        self.assertEqual(place_dict["latitude"], self.place.latitude)
        self.assertEqual(place_dict["longitude"], self.place.longitude)
        self.assertEqual(place_dict["amenity_ids"], self.place.amenity_ids)


if __name__ == "__main__":
    unittest.main()
