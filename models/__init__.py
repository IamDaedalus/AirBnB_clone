#!/usr/bin/python3

"""
This special script/module(?) holds the storage variable
which will glue both BaseModel and FileStorage together
to allow persistence
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
