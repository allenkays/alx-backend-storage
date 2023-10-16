#!/usr/bin/env python3
"""
This script updates topics based on name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a document in a collection based on the name

    :param mongo_collection: pymongo collection object
    :param name: School name (str) to update
    :param topics: List of strings representing the new topics
    :return: Number of documents updated:return: Number of documents update
    """
    result = mongo_collection.update_many(
                {"name": name},
                {"$set": {"topics": topics}}
            )
