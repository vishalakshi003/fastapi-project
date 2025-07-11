import strawberry
from strawberry.types import Info
from ..schemas.role_schema import *
from ..schemas.user_schema import *
from src.services.user_services import *
from src.services.role_service import *
from shared.core.context import CustomContext
# from shared.core.errors.graphql_error import GraphQLHttpError

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Createrole(self,info:Info[CustomContext],data:Rolecreate)->RoleResponse:
        return await create_role(info,data)
    
    @strawberry.mutation
    async def register_user(self,info:Info[CustomContext],data:UserInput)->UserResponse:
        return await create_user(info,data)
    @strawberry.mutation
    async def user_profile(self,info:Info[CustomContext],data:UserProfileInput)->UserprofileResponse:
        return await create_profile(info,data)
    @strawberry.mutation
    async def map_user_to_role(self,info:Info[CustomContext],data:RolemapInput)->RoleMappingType:
        return await user_map(info,data)
    
    @strawberry.mutation
    async def authentication_user(self,info:Info[CustomContext],data:LoginRequest)->TokenResponse:
        return await token(info,data)
    @strawberry.mutation
    async def change_password(self,info:Info[CustomContext],data:ChangepasswordInput)->changepasswordResponse:
        return await password_change(info,data)