from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import Optional


class DataChunk(BaseModel):
    # Each chunk will contain these properties
    id: Optional[ObjectId] = Field(default=None, alias="_id")

    chunk_text: str = Field(..., min_length=1)

    chunk_metadata: dict

    chunk_order: int = Field(..., gt=0)

    chunk_project_id: ObjectId


    class Config:
        arbitrary_types_allowed = True