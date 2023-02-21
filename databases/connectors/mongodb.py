import pymongo
from env import env

# MongoDB Client
MongoDBClient = pymongo.MongoClient(env("MONGODB_CONNECTION_STRING"))

# Databases
MongoDB_Base_R4_Database = MongoDBClient["baseR4"]

# Collections
MongoDB_Base_R4_Patient = MongoDB_Base_R4_Database["Patient"]
