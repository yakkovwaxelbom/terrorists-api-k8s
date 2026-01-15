import os
from contextlib import contextmanager
from pymongo import MongoClient

@contextmanager
def get_mongo_db():
    host = os.getenv("HOST_MONGO")
    port = os.getenv("MONGO_PORT")
    username = os.getenv("MONGO_USERNAME")
    password = os.getenv("MONGO_PASSWORD")
    db_name = os.getenv("MONGO_DB")

    mongo_uri = f"mongodb://{username}:{password}@{host}:{port}"
    # mongo_uri = f"mongodb://{host}:{port}"

    client = MongoClient(mongo_uri)

    try:
        yield client[db_name]
    finally:
        client.close()
