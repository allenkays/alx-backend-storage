#!/usr/bin/env python3
"""
This script returns list of school based on provided topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of school having a specific topic

    :param mongo_collection: pymongo collection object
    :topic: Topic (string) to search for
    :returns: List of school with given topic
    """
    result = mongo_collection.find({"topics": topic})
    results = list(result)

    return results
