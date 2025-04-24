import uuid
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from fapid_rest.common.models.base import BaseModel


class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class Item(ItemBase, BaseModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    user: "User" = Relationship(back_populates="items")  # type: ignore


class ItemCreate(ItemBase):
    owner_id: uuid.UUID
 

# class ItemUpdate(ItemBase):
#     title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class ItemResponse(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
