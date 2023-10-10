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
        my_dict = {}

        # simply iterate through the dictionary and extract the
        # datetime to convert to isoformat
        my_dict["__class__"] = "{}".format(type(self).__name__)
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict

    def _validate_value(self, name, value, Type):
        """
        This helper method will check to make sure that the user
        is assigning the right data type to the right variable or
        field. This method should help clean up our codebase by
        doing all the manual heavy lifting

        Args:
            name: the name of the value eg. name, my_number etc
            value: the value we are validating eg. 5, "my name" etc
            Type: this is the expected type of the value to validate

        Return:
            returns the value if it passes all checks and is validated
            correctly otherwise it will raise an appropriate error that
            the tests can catch
        """
        if not type(value) is Type:
            raise TypeError("{} must be of type {}".format(name, Type))

        return value

    def __str__(self):
        """
        This returns a string representation of the class and its
        attributes. Helpful for debugging and such
        """
        return "[{:s}] ({:s}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )
