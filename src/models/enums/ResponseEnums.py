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
    PROJECT_NOT_FOUND_ERROR = "project_not_found"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORBD_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vector_search_success"