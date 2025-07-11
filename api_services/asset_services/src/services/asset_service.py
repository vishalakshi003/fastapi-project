from typing import Optional
from sqlalchemy import select
from src.error.exception_handling import *
from src.models.assetmodel import AssetMaster,AssetAllocation
from ..schemas.asset import *
from sqlalchemy.ext.asyncio import AsyncSession
from shared.auth import decode_access_token

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
    auth_header = info.context.request.headers.get("authorization")
    if not auth_header:
        raise Exception("Missing Authorization header")
    token = auth_header.replace("Bearer ", "")
    payload = decode_access_token(token)  # Extracted from shared utils
    print('payload-------------------------------->',payload)
    if id:
        results=await db.execute(select(AssetMaster).where(AssetMaster.id==id))
    else:
        results=await db.execute(select(AssetMaster))
    data=results.scalars().all()
    return data


async def create_allocation(info,data:CreateAssetAllocation)->GetAssetAllocated:
    db:AsyncSession= info.context["db"]
    allocated_user= AssetAllocation(asset_id=data.assetid,user_id=data.userid,created_by=str(data.userid))
    db.add(allocated_user)
    await db.commit()
    await db.refresh(allocated_user)
    asset = await db.get(AssetMaster, data.assetid)

    return GetAssetAllocated(
            id=allocated_user.id,
            asset=GetAsset(id=asset.id, name=asset.name),
            users=UserResponse(id=str(allocated_user.user_id))
        )


async def get_assetallocate(info,id: Optional[int] = None)->GetAssetAllocated:
    db:AsyncSession=info.context["db"]
    if id:
        results=await db.execute(select(AssetAllocation).where(AssetAllocation.id==id))
    else:
        results=await db.execute(select(AssetAllocation))
    data=results.scalars().all()
    details=[]
    for asset in data:
        asset_res= await db.execute(select(AssetMaster).where(AssetMaster.id==asset.asset_id))
        asset_details=asset_res.scalar_one_or_none()
        if asset_details:
            details.append(GetAssetAllocated(
                id=asset.id,
                users=str(asset.user_id),
                asset=GetAsset(
                    id=asset_details.id,
                    name=asset_details.name
                )))
    return details