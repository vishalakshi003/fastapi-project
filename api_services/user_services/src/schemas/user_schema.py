from sqlalchemy import select
import strawberry
from typing import Optional,List,Any
from src.config.database import create_session
from src.models.usermodel import CustomUser
from strawberry.scalars import JSON 

@strawberry.type
class SuccessResponse:
    status:str
    message:str


@strawberry.input
class UserInput:
    name: str
    email: str
    mobile_number: str
    password: str
    password1: str
@strawberry.federation.type(keys=["id"])
class UserResponse:
    id:strawberry.ID
    name:str
    email:str
    mobile_number:str
    
    @staticmethod
    async def resolve_reference(id: strawberry.ID) -> "UserResponse":
        async with create_session() as db:
            result = await db.execute(
                select(CustomUser).where(CustomUser.id == int(id))
            )
            user = result.scalar_one_or_none()
            if user:
                return UserResponse(id=user.id, name=user.name,email=user.email,mobile_number=user.mobile_number)
            return None
        

@strawberry.input
class LoginRequest:
    mobile_number:str
    password:str

@strawberry.type
class TokenResponse:
    token:str


@strawberry.input
class UserProfileInput:
    user_id:int
    firstname:str
    lastname:str
    profile_photo:Optional[JSON]=None

@strawberry.type
class UserprofileResponse:
    user_id:int
    firstname:str
    lastname:str
    profile_photo:Optional[JSON]=None


@strawberry.input
class ChangepasswordInput:
    old_password:str
    password:str
    password1:str
@strawberry.type
class changepasswordResponse:
    status:str
    message:str
    change_password:bool

