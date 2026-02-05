from dotenv import load_dotenv
from utils import *
import json
import os


load_dotenv()


uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
mongo_client = get_mongo_client(uri)
db_name = os.getenv("DB_NAME", "employees_data")
coll_name = "employees_data"
file_path = "./data/employee_data_advanced.json"


def ping_mongodb():
    try:
        mongo_client[db_name].command("ping")
        print("MongoDB Is Connected ✌️")
    except:
        raise Exception


def load_data_to_mongodb():
    with open(file_path) as file:
        file_data = json.load(file)
    try:
        ins_result = mongo_client[db_name][coll_name].insert_many(file_data)
        print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")
    except:
        raise Exception


def close_connection():
    mongo_client.close()
    print("Closed MongoClient")