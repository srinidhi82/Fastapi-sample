from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class Item(BaseModel):
    id: int = Field(..., json_schema_extra={"example": 1})
    name: str = Field(..., json_schema_extra={"example": "Sample"})
    description: Optional[str] = Field(None, json_schema_extra={"example": "A sample item"})

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Sample",
                "description": "A sample item"
            }
        }
    )
