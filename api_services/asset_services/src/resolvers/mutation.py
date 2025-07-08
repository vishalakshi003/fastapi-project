from sqlalchemy import select
import strawberry
from src.error.exception_handling import *
from src.models.assetmodel import AssetMaster
from ..schemas.asset import *
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Create_asset(self,info:Info,data:CreateAsset)->GetAsset:
        db:AsyncSession=info.context["db"]
        results=await db.execute(select(AssetMaster).where(AssetMaster.name==data.name))
        asset_exists=results.scalar_one_or_none()
        if asset_exists:
            HttpError.already_exists()
        asset=AssetMaster(name=data.name)
        db.add(asset)
        await db.commit()
        await db.refresh(asset)
        return asset
    