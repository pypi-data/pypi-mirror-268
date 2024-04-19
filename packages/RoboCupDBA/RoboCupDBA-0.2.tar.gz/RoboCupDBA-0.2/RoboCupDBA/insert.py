import pymongo
##function##
# ex. RoboCupDBA.Insert(link="mongodb://root:6yHnmju%26@localhost:27017/",db="data",collection="data",name="1",x=0.0,y=0.0,theta=0.0,typeObj="A")
def Insert(link="mongodb://localhost:27017/",db="",collection="",name="",x=0.0,y=0.0,theta=0.0,typeObj=""):
    try:
        client = pymongo.MongoClient(link)
        # Access a specific database
        db = client[db]
        # Access a specific collection within the database
        collection = db[collection]
        # Insert a document into the collection
        data = {
            "_id": name,
            "localtion":{
                "x": (x),
                "y":(y),
                "theta":(theta)},
            "type":typeObj
        }
        insert_result = collection.insert_one(data)
        # Close the MongoDB connection
        client.close()
        return True
    except:
        return False