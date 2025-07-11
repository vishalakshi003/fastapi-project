from typing import Dict
from datetime import timedelta,datetime,timezone
from shared.utils.config import config
import jwt

def generate_access_token(data:Dict,expiry_time:timedelta=timedelta(config.TOKEN_EXPIRY))->str:
    token=jwt.encode(payload={
        **data,
        'exp':datetime.now(timezone.utc) +expiry_time
    },algorithm=config.JWT_ALGORITHM,key=config.JWT_SECRET)
    return token

def jwt_decode_payload(token: str) -> dict:
    return jwt.decode(token, config.JWT_SECRET, algorithms=config.JWT_ALGORITHM)