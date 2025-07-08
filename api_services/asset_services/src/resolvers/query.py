import strawberry
from typing import List,Optional
from sqlalchemy import select
from strawberry.types import Info
from src.schemas.asset import *
from src.services.asset_service import *
@strawberry.type
class Query:
    @strawberry.field
    async def get_assets(self,info:Info,id:Optional[int]=None)->List[GetAsset]:
        return await get_asset(info,id)