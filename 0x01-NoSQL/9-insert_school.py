#!/usr/bin/env python3
"""
This script inserts a new document in a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    This function returns documents in a collection based on kwargs

    :param mongo_collection: pymongo collection object
    :param kwargs: Keyword arguments for the new document
    :return: The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
