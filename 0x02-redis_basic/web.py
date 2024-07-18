#!/usr/bin/env python3

"""
This module provides a get_page function for
fetching and caching web page content.

The get_page function uses the requests module
to obtain the HTML content of a URL,
tracks how many times a URL was accessed,
and caches the result with an expiration time.
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def cache_page(fn: Callable) -> Callable:
    """
    Decorator to cache the result of the get_page function.

    Parameters
    ----------
    fn : Callable
        The function to be decorated.

    Returns
    -------
    Callable
        The decorated function with caching logic.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        cache_key = f"count:{url}"
        html_cache_key = f"html:{url}"

        # Increment the access count
        redis_client.incr(cache_key)

        # Check if the result is already cached
        cached_result = redis_client.get(html_cache_key)
        if cached_result:
            return cached_result.decode("utf-8")

        # Get the page content
        result = fn(url)

        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(html_cache_key, 10, result)

        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.

    Parameters
    ----------
    url : str
        The URL to fetch the HTML content from.

    Returns
    -------
    str
        The HTML content of the URL.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text
