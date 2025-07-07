import strawberry
from typing import Optional

@strawberry.input
class Rolecreate:
    name:str
@strawberry.type
class RoleResponse:
    id:int
    name:str

@strawberry.input
class RolemapInput:
    user_id: int
    rolename: str

@strawberry.type
class RoleMappingType:
    id: int
    role_id: int
    user_id: int
    