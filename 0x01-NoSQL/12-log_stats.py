#!/usr/bin/env python3
"""
Script to display logs
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to a MongoDB database and retrieves statistics about Nginx logs.

    This function connects to the 'logs' database and 'nginx' collection
    in MongoDB, and retrieves various statistics about the Nginx logs.

    The statistics include:
    - The total number of log documents
    - The number of documents with each HTTP method (
    GET, POST, PUT, PATCH, DELETE
    )
    - The number of documents with method=GET and path=/status

    The function prints these statistics to the console.
    """
    # Connect to MongoDB and select the 'logs' database
    client = MongoClient('localhost', 27017)
    db = client.logs

    # Select the 'nginx' collection
    collection = db.nginx

    # Calculate the total number of documents
    total_logs = collection.count_documents({})

    # Calculate the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Calculate the number of documents with method=GET and path=/status
    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"}
        )

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}:", count)
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
