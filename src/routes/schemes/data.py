from pydantic import BaseModel
import typing

class ProcessRequest(BaseModel):
    file_id: str = None     #optional parameter
    chunk_size: typing.Optional[int] = 100
    overlap_size: typing.Optional[int] = 20
    do_reset: typing.Optional[int] = 0 
    
    
    