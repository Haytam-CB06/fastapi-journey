from fastapi import APIRouter, HTTPException
from models.events import Event, EventUpdate
from database.connection import Database

router = APIRouter(prefix="/event", tags=["Events"])
event_db = Database(Event)


@router.get("/")
async def get_all_events():
    return await event_db.get_all()


@router.get("/{id}")
async def get_event(id: str):
    event = await event_db.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/new")
async def create_event(event: Event):
    return await event_db.save(event)


@router.put("/{id}")
async def update_event(id: str, body: EventUpdate):
    updated = await event_db.update(id, body.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated


@router.delete("/{id}")
async def delete_event(id: str):
    deleted = await event_db.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}