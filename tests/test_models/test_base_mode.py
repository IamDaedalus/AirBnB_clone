#!/usr/bin/python3

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def test_name(self):
        self.base.name = "Roger"
        self.assertEqual(self.base.name, "Roger")

    def test_wrong_name_type_int(self):
        with self.assertRaises(TypeError):
            self.base.name = 55

    def test_wrong_name_type_list(self):
        with self.assertRaises(TypeError):
            self.base.name = [0, 2, 3]

    def test_my_number(self):
        self.base.my_number = 80085
        self.assertEqual(self.base.my_number, 80085)

    def test_wrong_number_type_str(self):
        with self.assertRaises(TypeError):
            self.base.my_number = "80085"

    def test_wrong_number_type_list(self):
        with self.assertRaises(TypeError):
            self.base.my_number = [8, 0, 0, 8, 5]

    def test_wrong_number_type_float(self):
        with self.assertRaises(TypeError):
            self.base.my_number = 800.85

    def tearDown(self):
        del self.base


if __name__ == '__main__':
    unittest.main()
