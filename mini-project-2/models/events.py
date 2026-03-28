from typing import List, Optional
from beanie import Document
from pydantic import BaseModel, Field


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str] = Field(default_factory=list)
    location: str

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None