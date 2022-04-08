"""
utils.py consists of functions/methods that are mainly used in views.py and each method plays a significant role in
getting the job done. Read the code and comments for better understanding.
"""
import pymongo
from inputs.config import username, password, atlas_cluster_name  # user uri credentials are accessed from config.py
from propreitary.proprietary_data.config_proprietary import username, password, atlas_cluster_name   # will be removed in production


def create_database(db_name):  # this method connects the framework to the MongoDB_Atlas and creates a Database.
    client = pymongo.MongoClient(
        f"mongodb+srv://{username}:{password}@{atlas_cluster_name}.net/{db_name}?retryWrites=true&w=majority")
    db_handle = client[db_name]  # or you can simply write  database_handle = client.db_name
    return db_handle, client


def local_host(db_name):  # localhost, added for testing purposes, connects to localhost in MongoDB_Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db_handle = client[db_name]  # or you can simply write  database_handle = client.db_name
    return db_handle, client


# This method creates collection under a collection_name and validates the Schema that you've pre-defined under
# schema.py
def create_collection_and_validate(db_handle, collection_name, schema):
    db_handle.collection_name.drop()  # Use this for testing purposes and is not intended to use in production and
    # is used to drop the previous collection

    db_handle.create_collection(collection_name)
    db_handle.command('collMod', collection_name, validator=schema, validationLevel='moderate')
    return db_handle[collection_name]   # make sure that collection_name here is same as above, else it'll create
    # another collection that will have no effect of the schema


