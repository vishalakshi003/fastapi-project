from .settings import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
Base=declarative_base()

async_engine=create_async_engine(config.DATABASE_URL)

create_session=sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)

async def get_db():
    async with create_session() as session:
        yield session

async def get_context(db:AsyncSession=Depends(get_db)):
    return {"db":db}
