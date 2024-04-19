from typing import Dict, Optional, Union, List
from pymongo import CursorType
from pymongo.mongo_client import MongoClient
from pymongo.database import Database
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
from pymongo.results import InsertOneResult

class DatabaseConnector(object):
    
    """
    @private
    """
    _uri = None

    def __new__(cls, atlas_db_uri=None, mongodb_user=None, mongodb_password=None, *args, **kwargs):
        """
        Singleton contructor
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseConnector, cls).__new__(cls, *args, **kwargs)
        return cls.instance
    
    def __init__(self, atlas_db_uri=None, mongodb_user=None, mongodb_password=None, *args, **kwargs):
        """
        Constuctor.
        Here, we'll instantiate a list of mongodb clients from one URI.
        This class is a singleton (because the base URI should be the same) and the
        only way to modify this behavior is by adding a database to connect to.
        """
        super().__init__(*args, **kwargs)
        if not (atlas_db_uri and mongodb_password and mongodb_user):
            raise Exception("Parameters atlas_db_uri, mongodb_user and mongodb_password are mandatory")
        try:
            self._uri = "mongodb+srv://"+mongodb_user+":"+mongodb_password+"@"+atlas_db_uri
            self._db_client = MongoClient(self._uri, server_api=ServerApi('1'))
            self._client_databases: Dict[str, Database] = {}
            self._active_db = None
        except Exception as ex:
            raise ex

    def connected(self) -> bool: 
        """
        Pings the DB to verify that it's connected
        """
        try:
            self._db_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return True
        except Exception as e:
            print(e)
            return False
    
    def register_database(self, database_name=None, set_active=False) -> Database:
        """
        Adds a new database to the list of databases. This is made for keeping 
        the compatibility of the first version. NLP needs to access different 
        databases on different moments

        Paramaters
        ----------
            database_name : string the name of the database to be registered
            set_active : boolean (by default false) indicates whether the newly registered 
            database is set to be the active database for operations 

        Returns
        -------
            The new MongoDB client

        Raises
        ------
            An exception if the base uri is not defined
            An exception if the database name is not specified

        """
        if not self._uri:
            raise Exception("the DB URI is not defined")
        if database_name is None:
            raise Exception("cannot rengister un unnamed database")
        self._client_databases[database_name] = self._db_client[database_name]
        if set_active:
            self._active_db = database_name
        return self._client_databases[database_name]

    def find(self, query_options: Optional[Dict] = None, database=None) -> Union[List[Dict], CursorType]: 
        """
        Builds a query for executing a find operation

        Parameters
        ----------
        query_options : Dict
            A dictionary contaning the parameters of the operation
            collection : str 
                the name of the collection to be queried
            query : dict 
                an object containing the query
            fields : dict 
                an object containing the specification of the fields on the projection
            sort : list 
                a list containig paris of (field, sort_order), for example [("campaign", 1), ("created", -1)],
            result_as : str 
                a string specifying if the result is expected as a MongoDB cursor or a list (cursor by default)
        database : str 
            the name of the database to be used. If not specified, the operation is done on the active database
        Returns
        -------
        A union of a list or a mongodb cursor

        Raises
        ------
        An exception if the required fields aren't defined
        An exception if the collection is not configured
        A PyMongoError if the operation doesn't work
        """
        # Verify that everything is there
        required_fields = ["collection", "query"]
        for entry in required_fields:
            if not (entry in query_options and query_options[entry]): # De Morgan's
                raise Exception("%s value is required but not present or empty" % (entry))
        
        # Active DB
        use_db = database if database else self._active_db
        # Get the collection
        collection = query_options["collection"]
        # Get the query
        query = query_options["query"]
        # Get the fields (opt)
        fields = query_options["fields"] if "fields" in query_options and query_options["fields"] else None
        # Get the sort (opt)
        sort = query_options["sort"] if "sort" in query_options and query_options["sort"] else None
        # Get the return type (opt)
        result_as = query_options["result_as"] if "result_as" in query_options and query_options["result_as"] else "cursor"
        # Build the query
        db_collection = self._client_databases[use_db][collection]
        if db_collection is None:
            raise Exception("The collection %s is not defined/configured for the database %s" % (collection, use_db))
        try:
            cursor = db_collection.find(filter=query, projection=fields, sort=sort)
            if result_as == "list":
                return [document for document in cursor]
            return cursor
        except PyMongoError as ex:
            raise ex
        
    def insert(self, insert_options: Dict, database=None) -> InsertOneResult: 
        """
        Inserts a document in the given/active database
        Parameters
        ----------
        insert_options : Dict
            collection : str
                the name of the collection to insert the document
            document : Dict
                The document to be inserted
        database : str (optional)
            the name of the database where the collection is located. The default is the active DB

        Returns
        -------
        A cursor with the document

        Raises
        ------

        """
        # Verify that everything is there
        required_fields = ["collection", "document"]
        for entry in required_fields:
            if not (entry in insert_options and insert_options[entry]): # De Morgan's
                raise Exception("%s value is required but not present or empty" % (entry))
        # Active DB
        use_db = database if database else self._active_db
        # Get the collection
        collection = insert_options["collection"]
        # Get the document
        document = insert_options["document"]
        # Build the query
        db_collection = self._client_databases[use_db][collection]
        if db_collection is None:
            raise Exception("The collection %s is not defined/configured for the database %s" % (collection, use_db))
        try:
            return db_collection.insert_one(document)
        except PyMongoError as ex:
            raise ex

    def aggregate(self, query_options: Dict, database=None) -> Union[List[Dict], CursorType]:
        """
        Builds an aggregation pipeline with the given parameters
        Parameters
        ----------
        query_options : Dict
            collection : str
                The name of the collection where we want to execute the aggregation pipeline
            pipeline : list 
                A list containing the steps of the aggregation in the form of objects
            allow_disk : boolean (optional)
                Indicates whether the aggregation can use the disk. False by default
            result_as : str (optional)
                a string specifying if the result is expected as a MongoDB cursor or a list (cursor by default)
        database : str (optional)
            the name of the database where the collection is? Use by default the active DB
        Returns
        -------
        A union of a list or a mongodb cursor

        Raises
        ------
        An Exception if the fields are not defined. Pipeline should not be an empty list!
        An exception if the collection is not configured
        A PyMongoError if the operation doesn't work
        """
        # Verify that everything is there
        required_fields = ["collection", "pipeline"]
        for entry in required_fields:
            if not (entry in query_options and query_options[entry]): # De Morgan's
                raise Exception("%s value is required but not present or empty" % (entry))
        # Active DB
        use_db = database if database else self._active_db
        # Get the collection
        collection = query_options["collection"]
        # Get the pipeline
        pipeline = query_options["pipeline"]
        # Can use the disk?
        allow_disk = query_options["allow_disk"] if "allow_disk" in query_options and query_options["allow_disk"] else False
        # Get the return type (opt)
        result_as = query_options["result_as"] if "result_as" in query_options and query_options["result_as"] else "cursor"
        # Build the query
        db_collection = self._client_databases[use_db][collection]
        if db_collection is None:
            raise Exception("The collection %s is not defined/configured for the database %s" % (collection, use_db))
        try:
            cursor = db_collection.aggregate(pipeline, allowDiskUse=allow_disk)
            if result_as == "list":
                return [document for document in cursor]
            return cursor
        except PyMongoError as ex:
            raise ex

    def update(self, query_options: Dict, database=None) -> Dict:
        """
        Updates a document

        Parameters
        ----------
        query_options : Dict
            collection : str
                The name of the collection where we want to execute the aggregation pipeline
            criteria : Dict
                The condititions to perform the update
            value : Dict
                The modifications
            result_as : str (optional)
                a string specifying if the result is expected as a MongoDB cursor or a list (cursor by default)
        database : str (optional)
            the name of the database where the collection is? Use by default the active DB

        Returns
        -------
            A list of objects or a MongoDB cursor

        Raises
        ------
        An Exception if the fields are not defined. Pipeline should not be an empty list!
        An exception if the collection is not configured
        A PyMongoError if the operation doesn't work
        """
        # Verify that everything is there
        required_fields = ["collection", "criteria", "value"]
        for entry in required_fields:
            if not (entry in query_options and query_options[entry]): # De Morgan's
                raise Exception("%s value is required but not present or empty" % (entry))
        # Active DB
        use_db = database if database else self._active_db
        # Get the collection
        collection = query_options["collection"]
        # Get the criteria
        criteria = query_options["criteria"]
        # Get the value and convert to $set
        value = { "$set": query_options["value"] }
        # Build the query
        db_collection = self._client_databases[use_db][collection]
        if db_collection is None:
            raise Exception("The collection %s is not defined/configured for the database %s" % (collection, use_db))
        try:
            return db_collection.find_one_and_update(criteria, value)
        except PyMongoError as ex:
            raise ex

    def close(self):
        """
        Closes the connection to the database and save resources
        """
        self._db_client.close()

    
    def switch_db(self, db_name: str) -> Database:
        """
        Changes the active database

        Parameters
        ----------
        db_name : str
            the name of the target database

        Returns
        -------
            The handler to the selected database

        Raises
        ------
            An exception if the db_name parameter is empty
            An exception id the db_name does not exists in the registered databases
        """
        if not db_name:
            raise Exception("The database name cannot be empty")
        if db_name not in self._client_databases:
            raise Exception("The database %s is not registered in the list" % (db_name))
        self._active_db = db_name
        return self._client_databases[self._active_db]
    
