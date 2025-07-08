from typing import Optional
from sqlalchemy import select
from src.error.exception_handling import *
from src.models.assetmodel import AssetMaster
from ..schemas.asset import *
from sqlalchemy.ext.asyncio import AsyncSession


async def create_asset(info,data:CreateAsset)->GetAsset:
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


async def get_asset(info,id: Optional[int] = None)->GetAsset:
    db:AsyncSession=info.context["db"]
    if id:
        results=await db.execute(select(AssetMaster).where(AssetMaster.id==id))
    else:
        results=await db.execute(select(AssetMaster))
    data=results.scalars().all()
    return data