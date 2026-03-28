from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[PydanticObjectId]] = Field(default_factory=list)

    class Settings:
        name = "users"


class UserSignIn(BaseModel):
    email: EmailStr
    password: str