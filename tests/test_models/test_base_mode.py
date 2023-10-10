#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def test_name(self):
        self.base.name = "Roger"
        self.assertEqual(self.base.name, "Roger")

    def test_wrong_name_type(self):
        with self.assertRaises(ValueError):
            self.base.name = 55

    def tearDown(self):
        del self.base


if __name__ == '__main__':
    unittest.main()
