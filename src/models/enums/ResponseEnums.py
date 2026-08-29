from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "Content type not allowed"
    FILE_SIZE_EXCEEDED = "File size is too large"
    FILE_UPLOADED_SUCCESS = "File Upload Successful"
    FILE_UPLOADED_FAILED = "File Upload Failed"
    