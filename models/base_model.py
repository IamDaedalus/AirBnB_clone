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

        Keep everything private to control access rights just
        like we did in Almost A Circle
        """
        self.__id = "{}".format(uuid4())
        self.__created_at = datetime.now()
        # updated_at is datetime.now() because that was when
        # it was last updated
        self.__updated_at = datetime.now()
        self.__name = ""
        self.__my_number = 0

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

    # PUBLIC PROPERTIES STORED HERE
    # USEFUL FOR KEEPING ACCESS TO PRIVATE ATTRIUTES CLEAN
    # AND NICE
    @property
    def id(self):
        """
        This property returns the unique ID of the instance
        """
        return self.__id

    @property
    def name(self):
        """
        This property returns the name assigned to the instance

        Return:
            returns the number stored for the instance
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        This setter property gives access to re-assigning the
        name of the instance

        Args:
            value: the new value to store for the name
        """
        self.__name = self._validate_value("name", value, str)

    @property
    def my_number(self):
        """
        This property returns the number stored for the instance

        Return:
            returns the number stored for the instance
        """
        return self.__my_number

    @my_number.setter
    def my_number(self, value):
        """
        This property gives access to re-assigning the number
        stored for the instance

        Args:
            value: the new value to store
        """
        self.__my_number = self._validate_value("my_number", value, int)

    @property
    def created_at(self):
        """
        This property returns the datetime the instance was created

        Return:
            returns the datetime the instance was first created
        """
        return self.__created_at

    @property
    def updated_at(self):
        """
        This property returns the datetime the instance was created

        Return:
            returns the date the instance was updated at
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        """
        This property returns the datetime the instance was created

        Args:
            value: the value we are assigning the updated_at to
        """
        self.__updated_at = self._validate_value("updated_at", value, datetime)
