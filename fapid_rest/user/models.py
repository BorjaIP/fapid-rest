import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from fapid_rest.common.models.base import BaseModel


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    username: str | None = Field(default=None, max_length=255)


class User(BaseModel, UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserResponse(UserBase):
    id: uuid.UUID
    created_at: datetime


class UserName(SQLModel):
    username: str | None = Field(default=None, max_length=255)
