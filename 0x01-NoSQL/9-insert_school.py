#!/usr/bin/env python3

"""
This module provides functions to interact with
a MongoDB collection using the PyMongo library.

To use this module, you need to have the PyMongo
library installed:
    pip install pymongo

Example usage:
    from pymongo import MongoClient
    from this_module import insert_school

    client = MongoClient('your_connection_string')
    db = client['your_database']
    collection = db['your_collection']

    new_id = insert_school(collection, name="Holberton School",
    address="972 Mission Street")
    print(f"Inserted document ID: {new_id}")
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The keyword arguments representing the
        document to be inserted.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
