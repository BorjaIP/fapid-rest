from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID4

from fapid_rest.database.session import DBsession
from fapid_rest.item.models import ItemCreate, ItemResponse
from fapid_rest.item.service import ItemService

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
def create_item(
    item_data: ItemCreate, db_session: DBsession, service: ItemService = Depends(ItemService)
):
    # if service.get_user_by_email(db_session=db_session, user_email=user_data.email):
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=f"Email {user_data.email} already registered",
    #     )
    user = service.create_item(db_session=db_session, item_data=item_data)  # type: ignore
    return user
