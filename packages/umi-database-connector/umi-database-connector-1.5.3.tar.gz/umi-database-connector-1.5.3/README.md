# UMI database connector
This is a python wrapper for streamlining the querying process for our python services. The idea of this package is for NLP service
to use different MongoDB databases on one cluster.

## Class DatabaseConnector
A singleton that manages the MongoDB client and connections to different databases on the same cluster.
Example:
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
```
Note that `cluster-uri` needs to be a valid cluster uri that resolves on DNS.

### Methods
#### `DatabaseConnector.register_database`
This method adds a database to the list of available databases.
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")

connector.register_database("test") # Registers the database test on the list

connector.register_database("test_active_db", setActive=True) # Registers the database test_active_db on the list and sets it as the active databse
```
The active database is the one used by default on find, update, agreggate and delete operations

#### `DatabaseConnector.switch_db`
Changes the active database to a new one that has been previously registered. 
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
connector.register_database("test")
connector.register_database("test_active_db", setActive=True)
connector.switch_db("test") # Switches to test
connector.switch_db("unseen") # Raises an error, the database hasn't been registered
```

#### `DatabaseConnector.find`
Creates and launches a find query.
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
connector.register_database("test_active_db", setActive=True)
query_options = {
    "collection": "test_collection",
    "query": { "name": "Find test insert" },
    "result_as": "list"
}
result = db_instance.find(query_options=query_options) # Use the active database
# or
result = db_instance.find(query_options=query_options, database="another_database") # Use the specified database to run the query
```

#### `DatabaseConnector.insert`
Executes an insert operation.
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
connector.register_database("test_active_db", setActive=True)
insert_options = {
    "collection": "test_collection",
    "document": { "name": "this is a test"}
}
result = db_instance.insert(insert_options=insert_options) # Use the active database
# or
result = db_instance.insert(insert_options=insert_options, database="another_database") # Use the specified database to run the insert
```

#### `DatabaseConnector.update`
Executes an update many operation on a collection.
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
connector.register_database("test_active_db", setActive=True)
query_options = {
    "collection": "test_collection",
    "criteria": { "name": "the name to match"},
    "value": { "$set": {"name": "matched value"} },
    "result_as": "list"
}
result = db_instance.update(query_options=query_options) # Use the active database
# or
result = db_instance.update(query_options=query_options, database="another_database") # Use the specified database to run the insert
```

#### `DatabaseConnector.aggregate`
Executes an aggregation pipleine on a collection.
```python
from umi.database.database_connector import DatabaseConnector

connector = DatabaseConnector(atlas_db_uri="cluster-uri", mongodb_user="user", mongodb_password="pwd")
connector.register_database("test_active_db", setActive=True)
query_options = {
    "collection": "test_collection",
    "pipeline": [{"$match":{"name":"the name to match"}},{"$project":"..."}],
    "allow_disk":true,
    "result_as": "list" # or cursor
}
result = db_instance.aggregate(query_options=query_options) # Use the active database
# or
result = db_instance.aggregate(query_options=query_options, database="another_database") # Use the specified database to run the insert
```
