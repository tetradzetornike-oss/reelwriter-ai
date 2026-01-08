from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "ReelWriter AI Backend"
    api_prefix: str = "/api"

    # API KEY

    openai_api_key: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
