#!/usr/bin/env python3

"""
This module provides a function to find schools in a
MongoDB collection that have a specific topic using
the PyMongo library.

To use this module, you need to have the PyMongo library installed:
    pip install pymongo

Example usage:
    from pymongo import MongoClient
    from this_module import schools_by_topic

    client = MongoClient('your_connection_string')
    db = client['your_database']
    collection = db['your_collection']

    schools = schools_by_topic(collection, "Math")
    for school in schools:
        print(school)
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents with the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
