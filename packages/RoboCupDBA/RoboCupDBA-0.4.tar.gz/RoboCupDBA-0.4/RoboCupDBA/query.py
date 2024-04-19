import pymongo
from bson.json_util import dumps
##function##
# ex. Query
def Query(link="mongodb://localhost:27017/",db="",collection="",data={}):
    try:
        client = pymongo.MongoClient(link)
        # Access a specific database
        db = client[db]
        # Access a specific collection within the database
        collection = db[collection]
        query_result = collection.find_one(data)
        # Close the MongoDB connection
        client.close()
        return dumps(query_result)
    except:
        return False