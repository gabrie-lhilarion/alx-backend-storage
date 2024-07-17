#!/usr/bin/env python3

"""
This module provides a function to update the topics
of a school document in a MongoDB collection using
the PyMongo library.

To use this module, you need to have the PyMongo
library installed:
    pip install pymongo

Example usage:
    from pymongo import MongoClient
    from this_module import update_topics

    client = MongoClient('your_connection_string')
    db = client['your_database']
    collection = db['your_collection']

    update_topics(
    collection, "Holberton School", ["Math", "Science", "Arts"]
    )
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
