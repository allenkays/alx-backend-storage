#!/usr/bin/env python3
"""
This module defines a class with a store method
that initializes a redis db instancea and stores
some data to it
"""

import redis
import uuid
from typing import Union


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
        self._redis.set(key. data)

        return key
