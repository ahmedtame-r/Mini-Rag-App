from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from src.helpers.config import get_settings, Settings
from src.Controllers.DataController import DataController


data_router = APIRouter(
    prefix= "/api/v1/data",
    tags=["api_v_1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings= Depends(get_settings)):
    
    #validate file 
    is_valid, result_signal = DataController().validate_uploaded_file(file= file)
    
    ## Request status value 
    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal.value
            }
        )
        
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "signal": result_signal.value
        }
    )
    





