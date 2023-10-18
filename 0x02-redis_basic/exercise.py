#!/usr/bin/env python3
"""
This code will work us through redis operation using
its python module known as redis
"""


from redis import Redis
from functools import wraps
from uuid import uuid4
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """A function to count the number of time the class Cache was called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, *kwargs)
    return wrapper

def call_history(method: callable) -> Callable:
    """Keep track of input and output values from user input"""
    key_input = f'{method.__qualname__}:inputs'
    key_output = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(key_input, str(args))
        stdOut = method(self, *args, **kwargs)
        self._redis.rpush(key_output, str(args))
        return stdOut
    return wrapper
        


class Cache:
    """
    A class to define redis operation
    """

    def __init__(self) -> None:
        """A method for initialization"""
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """A method that returns a redit data casted to user desired type
        The Optional annotation implies that the argument is not compulsary
        to be called when calling the function.
        """
        value = self._redis.get(key)
        if value:
            if fn:
                return fn(value)
            else:
                return value
        else:
            return None
        
    def get_str(self, key: str):
        """An automated method that returns a string callable"""
        return self.get(key, str)
    
    def get_int(self, key: str):
        """An automated method that returns an int callable"""
        return self.get(key, int)
    