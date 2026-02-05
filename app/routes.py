from fastapi import APIRouter
from dal import *


router = APIRouter()


@router.get("/")
def hello_masege():
    return "Hello from MongoDB-Server 👋"


# @router.get("/employees/engineering/high-salary")