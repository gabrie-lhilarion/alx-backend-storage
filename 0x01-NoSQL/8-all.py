#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection
using the PyMongo library.

To use this module, you need to have the PyMongo library installed:
    pip install pymongo

Example usage:
    from pymongo import MongoClient
    from this_module import list_all

    client = MongoClient('your_connection_string')
    db = client['your_database']
    collection = db['your_collection']

    documents = list_all(collection)
    for doc in documents:
        print(doc)
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection.
        Returns an empty list if no documents are found.
    """
    documents = list(mongo_collection.find())
    return documents
