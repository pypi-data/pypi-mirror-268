import pymongo
##function##
# ex. Query
def Query(link="mongodb://localhost:27017/",db="",collection="",json={}):
    try:
        client = pymongo.MongoClient(link)
        # Access a specific database
        db = client[db]
        # Access a specific collection within the database
        collection = db[collection]
        query_result = collection.find_one(json)
        # Close the MongoDB connection
        client.close()
        return query_result
    except:
        return False