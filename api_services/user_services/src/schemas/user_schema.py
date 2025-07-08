import strawberry
from typing import Optional,List


@strawberry.input
class UserInput:
    name: str
    email: str
    mobile_number: str
    password: str
    password1: str
@strawberry.type
class UserResponse:
    id:int
    name:str
    email:str
    mobile_number:str