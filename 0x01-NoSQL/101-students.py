#!/usr/bin/env python3
"""update many to affect changes"""


def schools_by_topic(mongo_collection):
    '''A function to find and sort items in the collection'''
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
    
# Coded by EnGentech