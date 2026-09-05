from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    
    project_id: str = Field(..., min_length = 1)
    
    @validator("project_id")
    # static function
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("project_id must be alpha-numeric")
        
        return value
    
    class Config: 
        arbitrary_types_allowed = True
    
    @classmethod
    # static function
    def get_indexes(cls):
        
        return[
            {
                "key": [
                    ("project_id", 1)  # 1 = Ascs // -1 = Decs
                ],
                "name": "project_id_index_1",
                "unique": True
            }
        ]