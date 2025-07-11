from pathlib import Path
from typing import Dict
from datetime import timedelta,datetime,timezone

from fastapi import HTTPException,status
from shared.utils.config import config
import jwt
import os 


BASE_DIR = Path(__file__).resolve().parent.parent.parent


PRIVATE_KEY_PATH = BASE_DIR / config.PRIVATE_KEY_PATH
PUBLIC_KEY_PATH = BASE_DIR / config.PUBLIC_KEY_PATH

with open(Path(PRIVATE_KEY_PATH), "rb") as f:
    PRIVATE_KEY = f.read()
def generate_access_token(data:Dict,expiry_time:timedelta=timedelta(config.TOKEN_EXPIRY))->str:
    payload = {
        **data,
        "exp": datetime.now(timezone.utc) + expiry_time
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")


# def generate_access_token(data:Dict,expiry_time:timedelta=timedelta(config.TOKEN_EXPIRY))->str:
#     payload = {
#         **data,
#         "exp": datetime.now(timezone.utc) + expiry_time
#     }
#     return jwt.encode(payload,config.JWT_SECRET,algorithm=config.JWT_ALGORITHM)

with open(Path(PUBLIC_KEY_PATH), "rb") as f:
        PUBLIC_KEY = f.read()

def jwt_decode_payload(token: str) -> dict:
    print('Token decode called')
    try:
        return jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# def jwt_decode_payload(token: str) -> dict:
#     print('Token decode called')
#     try:
#         print('algorithm',config.JWT_ALGORITHM,config.JWT_SECRET)
#         return jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])

#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    