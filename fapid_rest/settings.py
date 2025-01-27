import secrets

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Postgres(BaseModel):
    host: str
    port: str
    collection_name: str
    embedding_model: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", validate_default=False, extra="ignore"
    )

    version: str = Field(default="v1")
    secret_key: str = secrets.token_urlsafe(32)
    port: int = Field(default=8000)

    # Database
    # chroma: Postgres
    # SQLALCHEMY_DATABASE_URI


settings = Settings()  # type: ignore
