import pymongo
import hashlib
from typing import Optional

client = pymongo.MongoClient("mongodb://root:root@localhost:27017")
db = client["URLShortener"]
collection = db["URLs"]

class URLRepository:

    @staticmethod
    def save(url: str):
        hashed_url = hashlib.sha512(bytes(url, "utf8")).hexdigest()
        item = {
            "url": url,
            "hashed_url": hashed_url
        }
        collection.insert_one(item)
        return hashed_url

    @staticmethod
    def findOne(hashed_url: str) -> Optional[str]:
        item = collection.find_one({ "hashed_url": hashed_url })
        if item == None:
            return None

        return item["url"]
