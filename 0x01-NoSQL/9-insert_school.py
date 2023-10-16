#!/usr/bin/env python3
"""List all value in the collection"""


def insert_school(mongo_collection, **kwargs):
    """function to insert key value: data in mongo_collection"""
    for key, values in kwargs.items():
        mongo_collection.insert_one({key:values})
        return mongo_collection._id
# Coded by EnGentech
