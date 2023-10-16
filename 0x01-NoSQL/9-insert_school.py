#!/usr/bin/env python3
"""List all value in the collection"""


def insert_school(mongo_collection, **kwargs):
    """function to insert key value: data in mongo_collection"""
    saveData = mongo_collection.insert_one(kwargs)
    return saveData.inserted_id
# Coded by EnGentech
