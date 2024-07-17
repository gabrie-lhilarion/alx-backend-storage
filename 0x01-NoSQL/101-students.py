#!/usr/bin/env python3
"""
This module provides a function to find and
return all students sorted by their average score
using the PyMongo library.

To use this module, you need to have the PyMongo
library installed:
    pip install pymongo

Example usage:
    from pymongo import MongoClient
    from this_module import top_students

    client = MongoClient('your_connection_string')
    db = client['your_database']
    collection = db['your_collection']

    students = top_students(collection)
    for student in students:
        print(student)
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of students sorted by average score,
        with each student having an averageScore key.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))
