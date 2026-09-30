from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
# Every variable in .env file will be loaded as a class to be used later; we need to define the data features 
# to enable pydatic lib to validate the data
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list 
    FILE_MAX_SIZE: str
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )
 

# A function to return an object of settings 
def get_settings():
    return Settings()
