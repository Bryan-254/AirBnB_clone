#!/usr/bin/python3
"""
Unittest for base module
"""

import sys
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Testing the base class model.
    """
    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_save_reload(self):
        # Create a new BaseModel instance
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        # Check that the object is saved to the file
        objects_before_reload = storage.all()
        self.assertTrue(my_model.id in objects_before_reload)

        # Reload the objects from the file
        storage.reload()

        # Check that the object is reloaded correctly
        objects_after_reload = storage.all()
        self.assertTrue(my_model.id in objects_after_reload)
        reloaded_model = objects_after_reload[my_model.id]
        self.assertEqual(reloaded_model.name, "My_First_Model")
        self.assertEqual(reloaded_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
