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
        
    @classmethod
    # static function
    def get_indexes(cls):
        return[
            {
                "key": [
                    ("chunk_project_id", 1)  # 1 = Ascs // -1 = Decs
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]