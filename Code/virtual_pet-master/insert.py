from pymongo import MongoClient
import datetime

from credentials import db_access

host= "ds113925.mlab.com:13925"
db_name = "rainbow"

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

print (uri)

client = MongoClient(uri)
db = client[db_name]

post = {"author": "mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymonogo"],
        "data": datetime.datetime.utcnow()}

collection = db.my_posts
collection.insert_one(post)

for x in db.my_posts.find():
    print(x)
