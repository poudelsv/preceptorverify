from functools import lru_cache

from pydantic_setting import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    app_name : str = "PreceptorVerify API"
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/preceptorverify"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()