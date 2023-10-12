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
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        Write the new object to the file that stores all the dictionary
        entries as a way to save items and persistency
        """
        # FIX:  Noticed you were doing the conversion here in save so I
        #       my code to reflect that. Interesting approach there (y)
        my_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            for key, _ in FileStorage.__objects.items():
                my_dict[key] = FileStorage.__objects[key].to_dict()
            json.dump(my_dict, file)


    def reload(self):
        """
        This method reads from a file all serialised objects, converts
        them from json format to a dictionary and assigns the __objects
        attribute to them

        If the file doesn't exist, no errors or exceptions are raised
        """
        # TODO: FIND A BETTER WAY OF ORGANISING THIS
        from models.base_model import BaseModel

        # Store a key-pair value of each class and its string name
        cls_map = {
                "BaseModel" : BaseModel,
            }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for objs in data.values():
                    cls_key = objs["__class__"]
                    cls_name = cls_map[cls_key]
                    self.new(cls_name(**objs))
