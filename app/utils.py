from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


def get_mongo_client(uri: str):
    try:
        mongo_client = MongoClient(uri)
        return mongo_client
    except:
        raise Exception
    

def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]



# def get_mongo_collection(coll_name, mongo_client=None):
#     if mongo_client is None:
#         mongo_client = get_mongo_client()
#     if db_name is None:
#         db_name = os.getenv("DB_NAME", "test-db")
#     coll = mongo_client[db_name][coll_name]
#     return coll