# This is a test case for the city_country.py file.

from city_country import city_country
import unittest

class test_country(unittest.TestCase):
    """A class to test the city_country file."""
    def test_city_country(self):
        """Checking the function"""
        joined = city_country("Beijing", "China")
        self.assertEqual(joined, "Beijing China")

if __name__ == "__main__":
    unittest.main()
