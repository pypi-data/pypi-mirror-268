import pymongo
##function##
# ex. RoboCupDBA.Insert(link="mongodb://root:6yHnmju%26@localhost:27017/",db="data",collection="data",name="1",x=0.0,y=0.0,theta=0.0,typeObj="A")
def Insert(link="mongodb://localhost:27017/", db="", collection="", name="", x=0.0, y=0.0, theta=0.0, typeObj=""):
    try:
        client = pymongo.MongoClient(link)
        db = client[db]
        collection = db[collection]

        # Check if a document with the same _id already exists
        existing_doc = collection.find_one({"id": str(name), "type": str(typeObj)})
        if existing_doc:
            # Update the existing document
            update_result = collection.update_one(
                {"id": str(name), "type": str(typeObj)},
                {"$set": {
                    "localtion.x": float(format(x, ".2f")),
                    "localtion.y": float(format(y, ".2f")),
                    "localtion.theta": float(format(theta, ".2f")),
                    "type": str(typeObj)
                }}
            )
            client.close()
            return True  # Return True if document was updated
        else:
            # Insert a new document
            data = {
                "id": str(name),
                "localtion": {
                    "x": float(format(x, ".2f")),
                    "y": float(format(y, ".2f")),
                    "theta": float(format(theta, ".2f"))
                },
                "type": str(typeObj)
            }
            insert_result = collection.insert_one(data)
            client.close()
            return True  # Return True if document was inserted
    except Exception as e:
        return False