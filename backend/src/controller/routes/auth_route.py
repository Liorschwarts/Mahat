from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from security import (
    get_current_user,
    create_access_token,
    authenticate_user,
    get_password_hash,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from modals import User
from datetime import timedelta
import logging

logger = logging.getLogger("uvicorn")
auth_route = APIRouter()

# fake_users_db = {}

# @auth_route.post("/register", response_model=User)
# async def register(form_data: OAuth2PasswordRequestForm = Depends()):
#     if form_data.username in fake_users_db:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     hashed_password = get_password_hash(form_data.password)
#     user = UserInDB(
#         username=form_data.username,
#         hashed_password=hashed_password,
#         email=None,
#         full_name=None,
#         disabled=False
#     )
#     fake_users_db[form_data.username] = user.dict()
#     return user

# @auth_route.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

# @auth_route.get("/users/me", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user