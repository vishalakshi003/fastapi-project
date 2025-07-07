import strawberry
from typing import Optional,List

import phonenumbers


@strawberry.input
class UserInput:
    name: str
    email: str
    mobilenumber: str
    password: str
    password1: str
@strawberry.type
class UserResponse:
    id:int
    name:str
    email:str
    mobilenumber:str
    roles:Optional[str]=None