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
from typing import Union, Callable, Optional
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method of the Cache class is called.

    Parameters
    ----------
    method : Callable
        The method to be decorated.

    Returns
    -------
    Callable
        The decorated method that increments the call count in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create the key using the qualified name of the method
        key = f"count:{method.__qualname__}"
        # Increment the call count for the method
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


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

    @count_calls
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

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieves data from the Redis cache and optionally
        converts it using the provided function.

        Parameters
        ----------
        key : str
            The key associated with the data in the cache.

        fn : Optional[Callable]
            A function to convert the data to the desired
            format. Default is None.

        Returns
        -------
        Optional[Union[str, bytes, int, float]]
            The retrieved data from the cache, optionally
            converted to the desired format.
            Returns None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from the Redis cache.

        Parameters
        ----------
        key : str
            The key associated with the data in the cache.

        Returns
        -------
        Optional[str]
            The retrieved data as a string from the cache.
            Returns None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from the Redis cache.

        Parameters
        ----------
        key : str
            The key associated with the data in the cache.

        Returns
        -------
        Optional[int]
            The retrieved data as an integer from the cache.
            Returns None if the key does not exist.
        """
        return self.get(key, fn=int)
