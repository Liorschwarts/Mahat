from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Integer, String


# User model
class User(SQLModel, table=True):
    id: Optional[int] = Field(
        sa_column=Column(
            Integer, 
            primary_key=True,
            autoincrement=True
        )
    )
    username: str = Field(
        sa_column=Column(
            String(100),
            unique=True,
            index=True
        )
    )
    full_name: str
    hashed_password: str

# User creation model
class UserCreate(SQLModel):
    username: str
    full_name: str
    password: str

# User update model
class UserUpdate(SQLModel):
    username: Optional[str] = None
    full_name: Optional[str] = None

# User response model
class UserResponse(SQLModel):
    id: Optional[int] = None
    username: str
    full_name: str
