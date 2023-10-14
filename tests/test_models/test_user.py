#!/usr/bin/python3

import unittest

from models.user import User


class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_user_name(self):
        self.user.first_name = "Jack"
        self.assertEqual(self.user.first_name, "Jack")

    def test_user_password(self):
        self.user.password = "helloworld12345"
        self.assertEqual(self.user.password, "helloworld12345")

    def test_user_email(self):
        self.user.email = "hello@world.com"
        self.assertEqual(self.user.email, "hello@world.com")

    def test_user_last_name(self):
        self.user.last_name = "Sparrow"
        self.assertEqual(self.user.last_name, "Sparrow")

    def test_user_to_dict(self):
        m_dict = self.user.to_dict()
        self.assertEqual(self.user.to_dict(), m_dict)
