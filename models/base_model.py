#!/usr/bin/python3

"""
This module contains the BaseModel class that all other classses
will inherit common attributes and methods from
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This is the base class for all other classes in the coming
    tasks. It is going to be the class from which every other
    class inherits from. This is the ADAM class
    """

    def __init__(self):
        """
        This is the constructor for the BaseModel class where
        we initialise some public instance attributes for use
        throughout the program
        """
        self.id = "{}".format(uuid4())
        self.created_at = datetime.now()
        # updated_at is datetime.now() because that was when
        # it was last updated
        self.updated_at = datetime.now()
        self.name = ""
        self.my_number = 0

    def save(self):
        """
        This method updates the 'updated_at' attribute to the
        current datetime or the current time and date
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary representation of the
        class for use in serialization to json objects
        """
        return {
                "my_number": self.my_number,
                "name": self.name,
                "__class__": type(self).__name__,
                "updated_at": self.updated_at.isoformat(),
                "id": self.id,
                "created_at": self.created_at.isoformat()
        }

    def __str__(self):
        """
        This returns a string representation of the class and its
        attributes. Helpful for debugging and such
        """
        return "[{:s}] ({:s}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )
