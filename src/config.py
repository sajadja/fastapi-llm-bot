from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DATABASE_URL: str

    GEMINI_API_KEY: str

    # CORS_ORIGINS: list[str]
    # CORS_ORIGINS_REGEX: str | None = None
    # CORS_HEADERS: list[str]

    model_config = SettingsConfigDict(env_file=".env")

settings = Config()
