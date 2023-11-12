import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    # Use the setUp method to create an instance of Review
    def setUp(self):
        # Creating instance.
        self.review = Review()
        # Setting class attributes.
        self.review.text = "Excellent, with a good view."
        self.review.place_id = "Amesterdam"
        self.review.user_id = "543"
        
    # Use the tearDown method to delete the instance of Review
    def tearDown(self):
        del self.review

    # Write a test method for the __init__ method of the Review class
    def test_init(self):
        # Check that the instance inherits from BaseModel
        self.assertIsInstance(self.review, BaseModel)
        # Check that the instance has the place_id, user_id,
        # and text attributes that are empty strings
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "Amesterdam")
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "543")
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "Excellent, with a good view.")

    # Write a test method for the __str__ method of the Review class
    def test_str(self):
        # Get the string representation of the instance
        review_str = str(self.review)
        # Check that the string representation contains the class name,
        # the id, and the dictionary of attributes
        self.assertIn("[Review]", review_str)
        self.assertIn(self.review.id, review_str)
        self.assertIn(str(self.review.__dict__), review_str)

    # Write a test method for the to_dict method of the Review class
    def test_to_dict(self):
        # Call the to_dict method of the instance
        review_dict = self.review.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(review_dict, dict)
        # Check that the dictionary contains the __class__ key
        # with the class name as the value.
        self.assertEqual(review_dict["__class__"], "Review")
        # Check that the dictionary contains the id, created_at, updated_at,
        # place_id, user_id, and text keys with the corresponding values.
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["created_at"],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         self.review.updated_at.isoformat())
        self.assertEqual(review_dict["place_id"], self.review.place_id)
        self.assertEqual(review_dict["user_id"], self.review.user_id)
        self.assertEqual(review_dict["text"], self.review.text)


if __name__ == "__main__":
    unittest.main()
