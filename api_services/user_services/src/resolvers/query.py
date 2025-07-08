import strawberry
from strawberry.types import Info
from typing import Optional,List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select
from src.error.exception_handling import HttpError
from src.models.rolemodel import *
from src.models.usermodel import *
from sqlalchemy.orm import selectinload
from src.schemas.role_schema import *
from src.schemas.user_schema import *
from src.services.role_service import *
from src.services.user_services import *
@strawberry.type
class Query:
    @strawberry.field
    async def get_roles(self,info:Info,id:Optional[int]=None)-> List[RoleResponse]:
        return await get_role(info,id)
    
    
    @strawberry.field
    async def get_user_details(self,info:Info,id:Optional[int]=None)->List[UserResponse]:
        return await get_users(info,id)