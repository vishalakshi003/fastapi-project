import strawberry


@strawberry.input
class CreateAsset:
    name:str

@strawberry.type
class GetAsset:
    id:int
    name:str

@strawberry.input
class CreateAssetAllocation:
    assetid:int
    userid:int

@strawberry.type
class GetAssetAllocated:
    id:int
    asset:GetAsset
    userid:int
    