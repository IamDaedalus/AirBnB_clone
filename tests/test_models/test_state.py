#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """
    Test case class for the State class, a subclass of BaseModel.
    """
    def test_instance_creation(self):
        """ Test if State object is successfully created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_inheritance(self):
        """ Test if State class inherits from BaseModel. """
        self.assertTrue(issubclass(State, BaseModel))

    def test_name_attribute(self):
        """ Test if name attribute is present in the State class."""
        self.assertTrue(hasattr(State, 'name'))

    def test_name_attribute_type(self):
        """ Test if name attribute in State is a string."""
        self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
