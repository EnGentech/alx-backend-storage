#!/usr/bin/env python3
"""List all value in the collection"""


def list_all(mongo_collection):
    """function to list all data in mongo_collection"""
    return mongo_collection.find()

# Coded by EnGentech
