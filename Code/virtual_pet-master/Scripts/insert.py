from pymongo import MongoClient
import datetime

uri = "mongodb://test:test@localhost/mytable"

print (uri)

client = MongoClient(uri)
db = client["mytable"]

post = {"author": "mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymonogo"],
        "data": datetime.datetime.utcnow()}

collection = db.my_posts
collection.insert_one(post)

for x in db.my_posts.find():
    print(x)
