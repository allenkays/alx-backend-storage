# 0x01. NoSQL

## Tasks
### 0. List all databases

Script that lists all databases in MongoDB.

### 1. Create a database 
Script that creates or uses the database my_db:

### 2. Insert document 
Script that inserts a document in the collection school:

    - The document must have one attribute name with value “Holberton school”
    - The database name is passed as an option of mongo command

### 3. All documents 
Script that lists all documents in the collection school:

    - The database name is passed as option of mongo command

### 4. All matches 
Script that lists all documents with name="Holberton school" in the collection school:

    - The database name will be passed as option of mongo command

### 5. Count 
Script that displays the number of documents in the collection school:
    - The database name will be passed as option of mongo command

### 6. Update 
Script that adds a new attribute to a document in the collection school:

    - The script updates only documents with name="Holberton school" (all of them)
    - Update adds the attribute address with the value “972 Mission street”
    - The database name will be passed as option of mongo command

### 7. Delete by match
 script that deletes all documents with name="Holberton school" in the collection school:

    - The database name will be passed as option of mongo command

### 8. List all documents in Python
Python function that lists all documents in a collection:

    - Prototype: def list_all(mongo_collection):
    - Returns an empty list if no document in the collection
    - mongo_collection is the pymongo collection object

### 9. Insert a document in Python
Python function that inserts a new document in a collection based on kwargs:

    - Prototype: def insert_school(mongo_collection, **kwargs):
    - mongo_collection is the pymongo collection object
    - Returns the new _id

### 10. Change school topics
Python function that changes all topics of a school document based on the name:

    - Prototype: def update_topics(mongo_collection, name, topics):
    - mongo_collection will be the pymongo collection object
    - name (string) is the school name to update
    - topics (list of strings) will be the list of topics approached in the school

### 11. Where can I learn Python? 
Python function that returns the list of school having a specific topic:

    - Prototype: def schools_by_topic(mongo_collection, topic):
    - mongo_collection is the pymongo collection object
    - topic (string) is topic searched

### 12. Log stats 
Python script that provides some stats about Nginx logs stored in MongoDB:

    - Database: logs
    - Collection: nginx
    - Display:
        - first line: x logs where x is the number of documents in this collection
        - second line: Methods:
        - 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
        - one line with the number of documents with:
            - method=GET
            - path=/status
