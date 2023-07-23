from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TEAM_PATH: str
    TOKEN: str
    HACKMD_API_URL: str

    NOTE_DATA_PATH = "note_data/"
    OUTPUT_PATH = "output/"
    LOG_PATH = "log/"

    class Config:
        env_file = ".env"


settings = Settings()
