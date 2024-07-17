#!/usr/bin/env python3
"""
This module provides a Cache class for storing
data in a Redis cache.

The Cache class includes methods to initialize
the Redis client, flush the database,
and store data with a unique key.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class to represent a cache using Redis.

    Attributes
    ----------
    _redis : redis.Redis
        an instance of the Redis client

    Methods
    -------
    __init__():
        Initializes the Redis client and flushes
        the database.

    store(data: Union[str, bytes, int, float]) -> str:
        Stores data in the Redis cache and returns
        a unique key.
    """

    def __init__(self):
        """
        Initializes the Cache class by creating an
        instance of the Redis client
        and flushing the database to remove all data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the Redis cache and returns a unique key.

        Parameters
        ----------
        data : Union[str, bytes, int, float]
            The data to be stored in the cache. It can be
            a string, bytes, integer, or float.

        Returns
        -------
        str
            The key associated with the stored data in the cache.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
