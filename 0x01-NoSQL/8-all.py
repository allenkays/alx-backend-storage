#!/usr/bin/env python3
"""
This script lists all documents in a mongo collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Script list all documents in the given collection

    Args:
        collection (list): Mongo collection

    Returns:
        docs (list): list of mongo documents in collection
    """
    cursor = mongo_collection.find({})
    document_list = list(cursor)

    if not document_list:
        return []
    else:
        return document_list
