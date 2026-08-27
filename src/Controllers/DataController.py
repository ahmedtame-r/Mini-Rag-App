import mimetypes

from fastapi import UploadFile

from src.Controllers.BaseController import BaseController


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
            print("❌ Content type not allowed")
            return False

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            print("❌ File size is too large")
            return False

        print("✅ File is valid")
        return True
