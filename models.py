from pydantic import BaseModel, Field
from typing_extensions import Annotated, List

class TerroristModel(BaseModel):
    name: str
    location: str
    rate_danger: Annotated[int, Field(ge=0, le=10)]


class Response(BaseModel):
    count: int
    top: List[TerroristModel]