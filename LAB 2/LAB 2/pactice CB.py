from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

crew=[
    {"id": 1, "name": "cosmo", "role": "Captain","experience": 10},
    {"id": 2, "name": "alice", "role": "Engineer","experience": 8},
    {"id": 3, "name": "Bob ", "role": "Scientist","experience": 5},
]

class CrewMember(BaseModel):
    name: str
    role: str
    experience: int

@app.get("/crew/{crew_id}", response_model=CrewMember)
async def get_crew(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"error": "Crew member not found"}
    