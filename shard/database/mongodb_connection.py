from shard.utils.logger import log_event

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError


class MongoManager():
    def __init__(self, db_name:str, collection_name:str,mongo_uri:str = "mongodb://localhost:27017/") -> None:
        pass
        try:
            self.client = MongoClient(mongo_uri)
            self.db = self.client[db_name]
            self.coll = self.db[collection_name]
        except PyMongoError as e:
              log_event("ERROR", f"error when connected to mongo: {e}")
              
        try:
                # The ping command is cheap and does not require auth.
                self.client.admin.command('ping')
        except ConnectionFailure:
                log_event("ERROR", "mONGO DB Server not available")
                raise
        
    def insert_document(self, document:dict):
        try:
               self.coll.insert_one(document=document)
        except Exception as e:
              log_event("ERROR", F"error when insert doc {document} to mongodb:{e}")
            
          