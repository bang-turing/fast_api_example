from typing import Optional, List
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

from pydantic import BaseModel, validator
from enum import Enum

router = APIRouter()


class Entities(Enum):
    NAME = 1
    STREET = 2


class InputDoc(BaseModel):
    author: str
    content: str
    entities_type: List[Entities]
    description: Optional[str] = None

    @validator("content")
    def content_must_not_exceed_300_character_limit(cls, v, values):
        if len(v) > 300:
            raise ValueError("Content must not exceed 300 characters")
        return v


@router.post(
    "/simple_entities_extraction/",
    tags=["simple_search_entities"],
    summary="dummy summary feed str get dict",
    description=(
        "Get the list of Ranked Developers for the given parameters. "
        "This route generates the Query from the parameters passed."
    ),
)
async def simple_search_entities(item: InputDoc):
    return item

