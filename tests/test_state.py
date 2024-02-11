#!/usr/bin/python3
"""Unittests class state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_attributes(self):
        """Test the attributes of the State class"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
