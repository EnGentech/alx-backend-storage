#!/usr/bin/env python3
"""
This code will work us through redis operation using
its python module known as redis
"""


from redis import Redis
from uuid import uuid4


class Cache:
    """
    A class to define redis operation
    """

    def __init__(self) -> None:
        """A method for initialization"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    