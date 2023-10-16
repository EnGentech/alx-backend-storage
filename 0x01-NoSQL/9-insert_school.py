#!/usr/bin/env python3
"""List all value in the collection"""


def insert_school(mongo_collection, **kwargs):
    """function to insert key value: data in mongo_collection"""
    mongo_collection.insert_one(kwargs)
    return mongo_collection._id
# Coded by EnGentech
