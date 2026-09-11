from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "Content type not allowed"
    FILE_SIZE_EXCEEDED = "File size is too large"
    FILE_UPLOADED_SUCCESS = "File Upload Successful"
    FILE_UPLOADED_FAILED = "File Upload Failed"
    PROCESSING_FAILED = "processing_failed"
    PROCESSING_SUCCESS = "processing_success"
    NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"