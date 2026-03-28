from typing import Type, Any
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, PydanticObjectId
from pydantic_settings import BaseSettings, SettingsConfigDict

from models.events import Event
from models.users import User


class Settings(BaseSettings):
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


async def initialize_database():
    settings = Settings()
    client = AsyncIOMotorClient(settings.DATABASE_URL)

    await init_beanie(
        database=client.get_default_database(),
        document_models=[Event, User]
    )


class Database:
    def __init__(self, document_model: Type[Any]):
        self.document_model = document_model

    async def save(self, document):
        await document.insert()
        return document

    async def get(self, id: str):
        try:
            return await self.document_model.get(PydanticObjectId(id))
        except Exception:
            return None

    async def get_all(self):
        return await self.document_model.find_all().to_list()

    async def update(self, id: str, body: dict):
        doc = await self.get(id)
        if not doc:
            return None

        for key, value in body.items():
            if value is not None:
                setattr(doc, key, value)

        await doc.save()
        return doc

    async def delete(self, id: str):
        doc = await self.get(id)
        if not doc:
            return False

        await doc.delete()
        return True