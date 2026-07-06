from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, overridable via environment variables or a .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "SettleWise API"
    environment: str = "development"
    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
