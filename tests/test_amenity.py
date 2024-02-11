#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_attributes(self):
        """Test the attributes of the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()
