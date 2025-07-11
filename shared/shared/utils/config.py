from dotenv import load_dotenv
import os

from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)


class Config:
    def __init__(self):
        self.JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")
        self.JWT_SECRET=os.getenv("JWT_SECRET")
        self.PUBLIC_KEY_PATH=os.getenv("PUBLIC_KEY_PATH")
        self.PRIVATE_KEY_PATH=os.getenv("PRIVATE_KEY_PATH")
        self.TOKEN_EXPIRY = int(os.getenv("TOKEN_EXPIRY", "1"))
config=Config()