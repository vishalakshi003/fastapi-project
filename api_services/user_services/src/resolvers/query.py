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
@strawberry.type
class Query:
    @strawberry.field
    async def get_roles(self,info:Info,id:Optional[int]=None)-> List[RoleResponse]:
        db: AsyncSession = info.context["db"]
        if id:
            results=await db.execute(select(Rolemaster).where(Rolemaster.id==id))
        else:
            results=await db .execute(select(Rolemaster))
        roles=results.scalars().all()
        if not roles:
            raise HttpError.not_found()    
        return roles
    
    
    @strawberry.field
    async def get_user_details(self,info:Info,id:Optional[int]=None)->List[UserResponse]:
        db:AsyncSession=info.context["db"]
        if id:
            results = await db.execute(select(CustomUser).options(selectinload(CustomUser.role_mapping)).where((CustomUser.id == id) & (CustomUser.is_active == True)))
        
        else:
            results = await db.execute(select(CustomUser).options(selectinload(CustomUser.role_mapping)).where((CustomUser.is_active == True)))
        users=results.scalars().all()
        role_name=[]

        for user in users:
            role_name.append(user.role_mapping.name)
    
        return UserResponse(
                id=user.id,
                name=user.name,
                email=user.email,
                mobilenumber=user.mobile_number,
                roles=", ".join(role_name) if role_name else "consumer"
        )