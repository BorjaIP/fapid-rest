from typing import List, Optional

from pydantic import UUID4
from sqlalchemy import delete
from sqlmodel import Session, col, select

from fapid_rest.security.hashes import get_password_hash
from fapid_rest.user.models import User, UserCreate, UserName


class UserService:

    def create_user(self, *, db_session: Session, user_data: UserCreate) -> User:
        user = User.model_validate(
            user_data, update={"hashed_password": get_password_hash(user_data.password)}
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user

    def get_user(self, *, db_session: Session, user_id: UUID4) -> User | None:
        user = db_session.get(User, user_id)
        return user

    def get_user_by_name(self, *, db_session: Session, username: str) -> User | None:
        # user = UserName(username=username)
        statement = select(User).where(col(User.username) == username)
        user = db_session.exec(statement).first()
        return user

    def get_all_users(self, *, db_session: Session) -> List[User]:
        statement = select(User)
        users = db_session.exec(statement).all()
        return users  # type: ignore

    def delete_user(self, *, db_session: Session, user_id: UUID4):
        statement = delete(User).where(col(User.id) == user_id)
        db_session.exec(statement)  # type: ignore
        db_session.commit()
