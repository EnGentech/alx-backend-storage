#!/usr/bin/env python3
"""update many to affect changes"""


def update_topics(mongo_collection, name, topics):
    """function update many columns in mongo db"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
    
# Coded by EnGentech
