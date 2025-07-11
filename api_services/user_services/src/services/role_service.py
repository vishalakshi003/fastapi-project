from sqlalchemy import select
from src.schemas.role_schema import *
from src.schemas.user_schema import *
from src.models.rolemodel import *
from src.models.usermodel import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.error.exception_handling import  HttpError
from utils.validate_phonenumber import *
from utils.function import *


async def create_role(info,data:Rolecreate)->RoleResponse:
    try:
        db:AsyncSession=info.context["db"]
        results=await db.execute(select(Rolemaster).where(Rolemaster.name==data.name))
        role_exists=results.scalar_one_or_none()
        if role_exists:
            raise HttpError.already_exists()

        new_role=Rolemaster(name=data.name)
        db.add(new_role)
        await db.commit()
        await db.refresh(new_role)
        return new_role
    except Exception as e:
        await db.rollback()
        raise HttpError.exception_handling(f"Something went wrong :{str(e)}") 
    
async def get_role(info,id:Optional[int] = None):
    db: AsyncSession = info.context["db"]
    if id:
        results=await db.execute(select(Rolemaster).where(Rolemaster.id==id))
    else:
        results=await db .execute(select(Rolemaster))
    roles=results.scalars().all()
    if not roles:
        raise HttpError.not_found()  
    return roles




async def user_map(info,data=RolemapInput):
    try:
        db:AsyncSession=info.context["db"]

        role_res=await db.execute(select(Rolemaster).where(Rolemaster.name.in_(data.rolename)))
        roles=role_res.scalars()
        if not roles:
            raise HttpError.not_found()

        for role in roles:
            mapping= db.add(Rolemapping(user_id=data.user_id,role_id=role.id))

        db.add(mapping)
        db.commit()
        db.refresh(mapping)
        return mapping
            
    except Exception as e:
        await db.rollback()
        raise HttpError.exception_handling(f"Something went wrong :{str(e)}")
