from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TEAM_PATH: str
    TOKEN: str
    HACKMD_API_URL: str = "https://api.hackmd.io/v1/"

    NOTE_DATA_PATH: str = "note_data/"
    OUTPUT_PATH: str = "output/"
    LOG_PATH: str = "log/"

    class Config:
        env_file = ".env"


settings = Settings()
