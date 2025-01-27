import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fapid_rest import api
from fapid_rest.database.session import create_db_and_tables
from fapid_rest.settings import settings

logger = logging.getLogger(__name__)


tags_metadata = [
    {
        "name": "health",
        "description": "Health check for api",
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FastAPI app running...")
    logger.info("Initialize DDBB")
    create_db_and_tables()
    yield


app = FastAPI(
    title="example",
    description="base project for fastapi backend",
    version=settings.version,
    openapi_url=f"/{settings.version}/openapi.json",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

app.add_middleware(CORSMiddleware, allow_origins=["*"])

# app.include_router(routes.home_router)
app.include_router(api.api_router, prefix=f"/{settings.version}")
