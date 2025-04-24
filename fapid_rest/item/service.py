import uuid
from typing import Any, List

from fastapi import APIRouter, HTTPException
from pydantic import UUID4
from sqlalchemy import delete
from sqlmodel import Session, col, func, select

from fapid_rest.item.models import Item, ItemCreate


class ItemService:

    def create_item(self, *, db_session: Session, item_data: ItemCreate) -> Item:
        item = Item.model_validate(item_data)
        db_session.add(item)
        db_session.commit()
        db_session.refresh(item)
        return item

    def get_item(self, *, db_session: Session, item_id: UUID4) -> Item | None:
        item = db_session.get(Item, item_id)
        return item

    # def get_user_by_name(self, *, db_session: Session, username: str) -> Item | None:
    #     statement = select(Item).where(col(Item.username) == username)
    #     user = db_session.exec(statement).first()
    #     return user

    # def get_user_by_email(self, *, db_session: Session, user_email: str) -> Item | None:
    #     statement = select(Item).where(col(Item.email) == user_email)
    #     user = db_session.exec(statement).first()
    #     return user

    # def get_all_users(self, *, db_session: Session) -> List[Item]:
    #     statement = select(Item)
    #     users = db_session.exec(statement).all()
    #     return users  # type: ignore

    # def update_user(
    #     self, *, db_session: Session, user_update: UserUpdate, user: Item
    # ) -> Item | None:
    #     user_sata = user_update.model_dump(exclude_unset=True)
    #     user.sqlmodel_update(user_sata)
    #     db_session.add(user)
    #     db_session.commit()
    #     db_session.refresh(user)
    #     return user

    # def delete_user(self, *, db_session: Session, user_id: UUID4):
    #     statement = delete(Item).where(col(Item.id) == user_id)
    #     db_session.exec(statement)  # type: ignore
    #     db_session.commit()
