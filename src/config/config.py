from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TEAM_PATH: str
    TOKEN: str
    HACKMD_API_URL: str = "https://api.hackmd.io/v1/"

    class Config:
        env_file = ".env"


settings = Settings()
