from fastapi import FastAPI, Request

# Initialize the FastAPI app
app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


# TODO: Create a GET endpoint to retrieve a specific crew member by ID
# - The endpoint path should be "/members/{crew_id}"
# - The function should be async and named 'read_crew_member'
# - If the crew member is found, return their details in JSON format
# - If not found, return a message indicating the crew member was not found
@app.get("/members/{crew_id}")
async def read_crew_member(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return {"crew_member": member}
    return {"error": "Crew member not found"}


# TODO: Create a POST endpoint to add a new crew member
# - The endpoint path should be "/members/"
# - The function should be async and named 'add_crew_member'
# - Parse the incoming request to get 'name' and 'role'
# - Create a new crew member with a unique ID and add it to the crew list
# - Return the details of the new crew member
@app.post("/members/")
async def add_crew_member(request: Request):
    data = await request.json()
    name = data.get("name")
    role = data.get("role")

    if not name or not role:
        return {"error": "Name and role are required"}

    new_id = max([member["id"] for member in crew], default=0) + 1
    new_member = {"id": new_id, "name": name, "role": role}
    crew.append(new_member)

    return {"message": "Crew member added successfully", "crew_member": new_member}


# TODO: Create a PUT endpoint to update an existing crew member's details
# - The endpoint path should be "/members/{crew_id}"
# - The function should be async and named 'update_crew_member'
# - Parse the incoming request to get updated 'name' and 'role'
# - If the crew member is found, update their details
# - If not found, return a message indicating the crew member was not found
@app.put("/members/{crew_id}")
async def update_crew_member(crew_id: int, request: Request):
    data = await request.json()
    name = data.get("name")
    role = data.get("role")

    for member in crew:
        if member["id"] == crew_id:
            member["name"] = name if name else member["name"]
            member["role"] = role if role else member["role"]
            return {"message": "Crew member updated successfully", "crew_member": member}

    return {"error": "Crew member not found"}


# TODO: Create a DELETE endpoint to remove a crew member by ID
# - The endpoint path should be "/members/{crew_id}"
# - The function should be async and named 'delete_crew_member'
# - If the crew member is found, remove them from the crew list
# - If not found, return a message indicating the crew member was not found
@app.delete("/members/{crew_id}")
async def delete_crew_member(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            crew.remove(member)
            return {"message": "Crew member deleted successfully", "crew_member": member}

    return {"error": "Crew member not found"}