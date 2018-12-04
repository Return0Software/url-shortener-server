import pymongo
import hashlib
from typing import Optional

client = pymongo.MongoClient("mongodb://root:root@localhost:27017")
db = client["URLShortener"]
collection = db["URLs"]

class URLRepository:

    @classmethod
    def save(cls, url: str, title: str):
        item = {
            "url": url,
            "title": title
        }

        if cls.findOne(title) != None:
            raise RuntimeError()

        collection.insert_one(item)

    @classmethod
    def findOne(cls,title: str) -> Optional[str]:
        item = collection.find_one({ "title": title })
        if item == None:
            return None

        return item["url"]
