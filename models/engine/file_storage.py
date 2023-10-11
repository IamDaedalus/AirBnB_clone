#!/usr/bin/python3

"""
Module that contains class for storage and persistence between
sessions which is vital for an application such as this
"""

import json
import os


class FileStorage:
    """
    FileStorage class contains methods and private class attributes
    that handle persistency and storage between sessions. There are
    methods for adding new json objects to a file, saving and
    retrieving
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This simply returns all objects that have been saved in the
        form of a dictionary. This is useful for passing between
        sessions
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new dictionary that will most likely be added to the
        __objects dictionary as a whole.

        Args:
            obj: the new obj to add which will be converted to a
                dictionary
        """
        key_name = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_name] = obj.to_dict()

    def save(self):
        """
        Write the new object to the file that stores all the dictionary
        entries as a way to save items and persistency
        """
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            # had troubles with json.dump and opted for dumps
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        This method reads from a file all serialised objects, converts
        them from json format to a dictionary and assigns the __objects
        attribute to them

        If the file doesn't exist, no errors or exceptions are raised
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                # read the contents of the file and pass it to json.loads
                # thing is will this be a permanent solution?
                data = file.read()
                FileStorage.__objects = json.loads(data)
        else:
            return
