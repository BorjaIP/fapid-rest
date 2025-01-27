from fastapi import APIRouter

from fapid_rest.user.routes import router as user_routes

api_router = APIRouter()
api_router.include_router(user_routes)
