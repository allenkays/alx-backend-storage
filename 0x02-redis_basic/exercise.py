#!/usr/bin/env python3
"""
This module defines a class with a store method
that initializes a redis db instancea and stores
some data to it
"""

import redis
import uuid
from functools import wraps
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method: The method to be decorated.

    Returns:
        The decorated method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Creates an instance of a redis database and stores input data into
    it
    """
    def __init__(self):
        """
        Initializes the cache object redis instance and flushes it
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method to store the input data in the redis db using a
        random key

        Args:
            data: The data to be stored can be any data type

        Returns:
            Random key for data stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(
            self, key: str,fn: Optional[Callable[[bytes], Union[str, int]]]
            = None) -> Union[bytes, str, int, None]:
        """
        Retrieve the data from Redis using the provided key.

        Args:
            key: The key used to retrieve the data from Redis.
            fn: optional callable that converts the data to the desired format.

        Returns:
            The retrieved data, converted  as per callable if specified.
            None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis with given key and convert it to a string.

        Args:
            key: The key used to retrieve the data from Redis.

        Returns:
            The retrieved data as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis with given key and convert it to an integer.

        Args:
            key: The key used to retrieve the data from Redis.

        Returns:
            Retrieved data as an integer, or None if key does not exist.
        """
        return self.get(key, fn=int)
