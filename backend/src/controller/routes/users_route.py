from typing import List
from fastapi import APIRouter, HTTPException, Depends
from modals import User, UserCreate, UserUpdate, UserResponse
from bl import UsersBL
import logging

logger = logging.getLogger("uvicorn")

users_route = APIRouter()

# Create
@users_route.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    logger.info(f"Creating user: {user.username}")
    return UsersBL().create_user(user)

# Read all
@users_route.get("/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 100):
    return UsersBL().get_users(skip=skip, limit=limit)

# Read one
@users_route.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return UsersBL().get_user(id=user_id)

# Update
@users_route.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    return UsersBL().update_user(user_id, user)

# Delete
@users_route.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    return UsersBL().delete_user(user_id)