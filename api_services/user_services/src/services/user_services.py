from sqlalchemy import and_, select
import strawberry
from strawberry.types import Info
from src.schemas.role_schema import *
from src.schemas.user_schema import *
from src.models.rolemodel import *
from src.models.usermodel import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.error.exception_handling import HttpError
from utils.validate_phonenumber import *
from utils.function import *


async def create_user(info,data)->UserResponse:
    try:
        db:AsyncSession=info.context["db"]
        exists_res=await db.execute(select(CustomUser).where(and_(CustomUser.email==data.email,CustomUser.mobile_number==data.mobilenumber)))
        email_exists = exists_res.scalar_one_or_none()
        if email_exists:
            raise HttpError.already_exists()    
        try:
            validate_phone(data.mobilenumber)
        except ValueError as e:
            raise HttpError.invalid_mobile_number(details=e)
        if data.password != data.password1:
            raise HttpError.verify_password()
        hash_password=password_context.hash(data.password)
        users=CustomUser(name=data.name,email=data.email,mobile_number=data.mobilenumber,password=hash_password)
        db.add(users)
        await db.commit()
        await db.refresh(users)
        return users
    except Exception as e:
        await db.rollback()
        raise HttpError.exception_handling(f"Something went wrong :{str(e)}")
    

async def create_role(info,data)->RoleResponse:
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
    
async def user_map(info,data):
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
