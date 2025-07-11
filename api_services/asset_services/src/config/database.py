from sqlalchemy.ext .declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from .settings import config
from fastapi import Depends
from shared.core.context import CustomContext
from fastapi import Request
from shared.utils.jwt import jwt_decode_payload
Base=declarative_base()

engine=create_async_engine(config.DATABASE_URL)

async_session=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)


async  def get_db():
    async with async_session() as session:
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