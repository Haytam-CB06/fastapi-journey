from fastapi import APIRouter, HTTPException
from models.users import User, UserSignIn
from database.connection import Database

router = APIRouter(prefix="/user", tags=["Users"])
user_db = Database(User)


@router.post("/signup")
async def signup(user: User):
    existing_users = await user_db.get_all()
    for existing in existing_users:
        if existing.email == user.email:
            raise HTTPException(status_code=400, detail="User already exists")

    return await user_db.save(user)


@router.post("/signin")
async def signin(user: UserSignIn):
    users = await user_db.get_all()

    for existing in users:
        if existing.email == user.email and existing.password == user.password:
            return {"message": "Signin successful"}

    raise HTTPException(status_code=401, detail="Invalid email or password")