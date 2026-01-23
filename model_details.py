from typing import List
from pydantic import BaseModel, Field


class ModelDetails(BaseModel):
    name: str = Field(description="The name of the model")
    version: str = Field(description="The version of the model")
    provider: str = Field(description="The provider of the model")
    capabilities:List[str] = Field(description="List of 3 capabilities of the model")
