#!/usr/bin/env python3
"""
Script to return averagaes
"""
from pymongo import DESCENDING


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: The pymongo collection object representing the students' data.

    Returns:
        List of students sorted by average score in descending order. Each student document includes an 'averageScore' key.
    """
    
    # Aggregate pipeline to calculate the average score for each student
    pipeline = [
        {
            '$project': {
                'name': 1,
                'scores': 1,
                'averageScore': {
                    '$avg': '$scores'
                }
            }
        },
        {
            '$sort': {
                'averageScore': DESCENDING
            }
        }
    ]

    # Execute the aggregation
    result = list(mongo_collection.aggregate(pipeline))

    return result
