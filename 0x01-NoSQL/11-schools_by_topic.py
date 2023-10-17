#!/usr/bin/env python3
"""update many to affect changes"""


def schools_by_topic(mongo_collection, topic):
    '''A function to return an array containing a certain topic of interest'''
    return mongo_collection.find({'topics': {'$in':[topic]}})
    
# Coded by EnGentech
