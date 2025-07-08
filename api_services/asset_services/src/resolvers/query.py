import strawberry
from typing import List,Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from strawberry.types import Info
from src.models.assetmodel import AssetMaster
from src.schemas.asset import *

@strawberry.type
class Query:
    @strawberry.field
    async def get_asset(self,info:Info,id:Optional[int]=None)->List[GetAsset]:
        db:AsyncSession=info.context["db"]
        if id:
            results=await db.execute(select(AssetMaster).where(AssetMaster.id==id))
        else:
            results=await db.execute(select(AssetMaster))
        data=results.scalars().all()
        return data