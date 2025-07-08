import strawberry
from ..schemas.asset import *
from strawberry.types import Info
from src.services.asset_service import *

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def Create_asset(self,info:Info,data:CreateAsset)->GetAsset:
        return await create_asset(info,data)
    