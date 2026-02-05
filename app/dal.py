from connection import *


def get_engineering_high_salary_employees():
    query = {
        "job_role.department": "Engineering",
        "salary": {"$gt": 65000}
    }
    projection = {
        "_id": 0,
        "employee_id": 1,
        "name": 1,
        "salary": 1
    }
    return list(mongo_client[db_name][coll_name].find(query, projection))


def get_employees_by_age_and_role():
    query = {
        "age": {"$gte": 30, "$lte": 45},
        "job_role.title": {"$in": ["Engineer", "Specialist"]}
    }
    projection = {"_id": 0}
    return list(mongo_client[db_name][coll_name].find(query, projection))

def get_top_seniority_employees_excluding_hr():
    query = {
        "job_role.department": {"$ne": "HR"}
    }
    projection = {"_id": 0}
    
    cursor = mongo_client[db_name][coll_name].find(query, projection).sort("years_at_company", -1).limit(7)
    
    return list(cursor)


def get_employees_by_age_or_seniority():
    query = {
        "$or": [
            {"age": {"$gt": 50}},
            {"years_at_company": {"$lt": 3}}
        ]
    }
    projection = {
        "_id": 0,
        "employee_id": 1,
        "name": 1,
        "age": 1,
        "years_at_company": 1
    }
    return list(mongo_client[db_name][coll_name].find(query, projection))


def get_managers_excluding_departments():
    query = {
        "job_role.title": "Manager",
        "job_role.department": {"$nin": ["Sales", "Marketing"]}
    }
    projection = {"_id": 0}
    return list(mongo_client[db_name][coll_name].find(query, projection))


def get_employees_by_lastname_and_age():
    query = {
        "age": {"$lt": 35},
        "$or": [
            {"name": {"$regex": "Nelson$"}},
            {"name": {"$regex": "Wright$"}}
        ]
    }
    projection = {
        "_id": 0,
        "name": 1,
        "age": 1,
        "job_role.department": 1
    }
    return list(mongo_client[db_name][coll_name].find(query, projection))