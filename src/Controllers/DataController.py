import mimetypes
from fastapi import UploadFile
from src.Controllers.BaseController import BaseController
from src.models import ResponseSignal
from .ProjectController import ProjectController
import re
import os


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):
        print("CONTENT TYPE:", file.content_type)
        print("FILE SIZE:", file.size)

        content_type = file.content_type

        # Some clients send application/octet-stream for every file.
        # Detect the type from the filename in that case.
        if content_type == "application/octet-stream":
            content_type, _ = mimetypes.guess_type(file.filename or "")

        if content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED

        return True, ResponseSignal.FILE_UPLOADED_SUCCESS
    
    
    def generate_unique_filename(self, origin_file_name: str, project_id: str): 
        random_filename = self.generate_random_string()
        
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        cleaned_file_name = self.get_clean_file_name(origin_file_name=origin_file_name)
        
        new_file_path = os.path.join(
            project_path,
            random_filename + "_" + cleaned_file_name
        )
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_filename + "_" + cleaned_file_name
            )
        
        return new_file_path
        
    def get_clean_file_name(self, origin_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', origin_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
        
        
        