from pymongo import mongoClient
import datatime

import flask_starter.credentials import db_access


host = 'ds113925.mlab.com:13925'
db_name = 'rainbow'
uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

client = MongoClient(uri)
db = client[db_name]

post = {"author" "Mike"}
        "text": "My first blog post",
        "tags": ["mongodb", "python", "bymongo"]
        "data": datatime.datatie. utcnow()}

collection = db.my_posts
collection.insert_one(post)
