from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4

from fapid_rest.common.models.base import Message
from fapid_rest.database.session import DBsession
from fapid_rest.user.models import UserCreate, UserName, UserResponse
from fapid_rest.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate, db_session: DBsession, service: UserService = Depends(UserService)
):
    user = service.create_user(db_session=db_session, user_data=user_data)  # type: ignore
    return user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID4, db_session: DBsession, service: UserService = Depends(UserService)):
    user = service.get_user(db_session=db_session, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# @router.get("/{username}", response_model=UserName)
# def get_user_by_name(
#     username: str, db_session: DBsession, service: UserService = Depends(UserService)
# ):
#     user = service.get_user_by_name(db_session=db_session, username=username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


@router.get("/", response_model=List[UserResponse])
def get_all_users(db_session: DBsession, service: UserService = Depends(UserService)):
    users = service.get_all_users(db_session=db_session)
    return users


@router.delete("/{user_id}", response_model=Message)
def delete_user(
    user_id: UUID4, db_session: DBsession, service: UserService = Depends(UserService)
) -> Message:
    service.delete_user(db_session=db_session, user_id=user_id)
    return Message(message="User deleted successfully")
