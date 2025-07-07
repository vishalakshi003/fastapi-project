import strawberry
from strawberry.types import Info
from ..schemas.role_schema import *
from ..schemas.user_schema import *
from src.services.user_services import create_user,create_role,user_map

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Createrole(self,info:Info,data:Rolecreate)->RoleResponse:
        return await create_role(info,data)
    @strawberry.mutation
    async def CreateUser(self,info:Info,data:UserInput)->UserResponse:
        return await create_user(info,data)
    @strawberry.mutation
    async def map_user_to_role(self,info:Info,data:RolemapInput)->RoleMappingType:
        return await user_map(info,data)