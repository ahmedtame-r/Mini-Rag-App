from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
import os

base_router = APIRouter(
    prefix= "/api/v1",
    tags=["api_v_1"]
)

@base_router.get("/")      #default route
async def welcome():       #async: make the code run in mixed flow
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "message": "hello world I am back!!",
        "app_name": app_name,
        "app_version": app_version,
    }
    