from dotenv import load_dotenv
import os 

load_dotenv()

class Config:
    def __init__(self):
        self.JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")
        self.JWT_SECRET=os.getenv("JWT_SECRET")
        self.TOKEN_EXPIRY=os.getenv("TOKEN_EXPIRY")
config=Config()