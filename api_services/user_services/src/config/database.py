from .settings import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import Depends, Request
from shared.core.context import CustomContext
from shared.utils.jwt import jwt_decode_payload


Base=declarative_base()

async_engine=create_async_engine(config.DATABASE_URL)

create_session=sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)

async def get_db():
    async with create_session() as session:
        yield session

# async def get_context(db:AsyncSession=Depends(get_db)):
#     return {"db":db}

async def get_context(request: Request,db: AsyncSession = Depends(get_db))-> CustomContext:
    user = None
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        user = jwt_decode_payload(token)
    return CustomContext(request=request, db=db, user=user)