#!/usr/bin/env python3

import json
import os
from pymongo import MongoClient
import re
from textblob import TextBlob
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['tweets']
collection= db['AAPL']
os.chdir("/home/neeraj/Downloads/twitterstream-to-mongodb/Transfer/")
fileslist = os.listdir(".")
files = filter(os.path.isfile,fileslist)
for fl in files:
    json_data=open(fl)
    jayson=json_data.readlines()
    for jason in jayson:
        d=json.loads(jason)
        dText=TextBlob(d['text'])
        k= { "text": d["text"],  "retweets": d["retweet_count"] , "favorites" : d["favorite_count"], "name" :
            d["user"]["name"],"followers" : d["user"]["followers_count"],"screen_name" : d["user"]["screen_name"] ,
            "date" : d["created_at"], "sentiment": {"polarity": dText.sentiment.polarity , "subjectivity": dText.sentiment.subjectivity} 
           }
#         print(k)
        collection.insert_one(k)
    os.rename(fl , "InDB/"+fl)

    