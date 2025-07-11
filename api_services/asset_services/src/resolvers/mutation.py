import strawberry
from ..schemas.asset import *
from strawberry.types import Info
from src.services.asset_service import *

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Create_asset(self,info:Info,data:CreateAsset)->GetAsset:
        return await create_asset(info,data)
    
    @strawberry.mutation
    async def Create_assetallocation(self,info:Info,data:CreateAssetAllocation)->GetAssetAllocated:
        return await create_allocation(info,data)
    