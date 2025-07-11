import strawberry
from ..schemas.asset import *
from strawberry.types import Info
from src.services.asset_service import *
from shared.core.context import CustomContext

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Create_asset(self,info:Info[CustomContext],data:CreateAsset)->GetAsset:
        return await create_asset(info,data)
    
    @strawberry.mutation
    async def Create_assetallocation(self,info:Info[CustomContext],data:CreateAssetAllocation)->GetAssetAllocated:
        return await create_allocation(info,data)
    