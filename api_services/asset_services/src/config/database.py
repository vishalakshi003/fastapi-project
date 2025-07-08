from sqlalchemy.ext .declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from .settings import config
from fastapi import Depends
Base=declarative_base()

engine=create_async_engine(config.DATABASE_URL)

async_session=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)


async  def get_db():
    async with async_session() as session:
        yield session


async def get_context(db:AsyncSession=Depends(get_db)):
    return {"db":db}
